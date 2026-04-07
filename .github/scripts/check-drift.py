#!/usr/bin/env python3
"""Check third-party artifacts against their upstream sources for drift.

Parses ``ATTRIBUTIONS.md``, extracts each entry's ``Source``,
``Upstream path``, and ``Upstream commit``, then uses the GitHub API to
compare the file's blob SHA at the recorded commit against its blob SHA
at the upstream repository's current default branch. Blob SHAs are
content hashes, so this is content-accurate: unrelated commits in the
upstream repo do not cause false positives.

If any file has drifted (or an entry errors out), a markdown drift
report is written to ``drift-report.md`` in the current directory. The
calling workflow decides what to do based on whether that file is
non-empty. The script itself always exits 0.

Requires only the Python standard library. Expects ``GITHUB_TOKEN`` in
the environment for authenticated API requests.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ATTRIBUTIONS_PATH = Path("ATTRIBUTIONS.md")
REPORT_PATH = Path("drift-report.md")

GITHUB_API = "https://api.github.com"
USER_AGENT = "doribd-skills-drift-check"


def parse_attributions(text):
    """Parse ATTRIBUTIONS.md into a list of entry dicts.

    Each level-3 heading (``### <type>/<name>``) starts a new entry.
    Subsequent lines of the form ``- <Field>: <value>`` are collected
    into the entry.
    """
    entries = []
    chunks = re.split(r"(?m)^### +", text)
    for chunk in chunks[1:]:  # first chunk is preamble
        lines = chunk.splitlines()
        if not lines:
            continue
        entry = {"name": lines[0].strip()}
        for line in lines[1:]:
            m = re.match(
                r"^\s*-\s*(Source|Upstream path|Upstream commit|Synced|License|Notes)\s*:\s*(.+?)\s*$",
                line,
            )
            if m:
                key = m.group(1).lower().replace(" ", "_")
                entry[key] = m.group(2)
        entries.append(entry)
    return entries


def parse_github_source(url):
    """Extract (owner, repo) from a github.com URL, or None if not GitHub."""
    m = re.match(r"^https://github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        return None
    owner = m.group(1)
    repo = m.group(2)
    if repo.endswith(".git"):
        repo = repo[:-4]
    return owner, repo


def github_request(url, token):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", USER_AGENT)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def fetch_blob_sha(owner, repo, path, ref, token):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}?ref={ref}"
    data = github_request(url, token)
    if not isinstance(data, dict) or "sha" not in data:
        raise RuntimeError(
            f"Unexpected response for {owner}/{repo}:{path}@{ref}"
        )
    return data["sha"]


def fetch_default_branch(owner, repo, token):
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    data = github_request(url, token)
    return data["default_branch"]


def check_entry(entry, token):
    name = entry.get("name", "<unknown>")
    source = entry.get("source")
    recorded_commit = entry.get("upstream_commit")
    path = entry.get("upstream_path")

    missing = [
        field
        for field in ("source", "upstream_commit", "upstream_path")
        if not entry.get(field)
    ]
    if missing:
        return {
            "name": name,
            "status": "error",
            "error": f"missing fields: {', '.join(missing)}",
        }

    parsed = parse_github_source(source)
    if not parsed:
        return {
            "name": name,
            "status": "error",
            "error": f"source is not a recognised GitHub URL: {source}",
        }
    owner, repo = parsed

    try:
        default_branch = fetch_default_branch(owner, repo, token)
        recorded_blob = fetch_blob_sha(owner, repo, path, recorded_commit, token)
        current_blob = fetch_blob_sha(owner, repo, path, default_branch, token)
    except urllib.error.HTTPError as e:
        return {
            "name": name,
            "status": "error",
            "error": f"HTTP {e.code} for {owner}/{repo}:{path}",
        }
    except (urllib.error.URLError, RuntimeError, KeyError) as e:
        return {"name": name, "status": "error", "error": str(e)}

    drifted = recorded_blob != current_blob
    return {
        "name": name,
        "status": "drifted" if drifted else "in_sync",
        "owner": owner,
        "repo": repo,
        "path": path,
        "recorded_commit": recorded_commit,
        "default_branch": default_branch,
        "recorded_blob": recorded_blob,
        "current_blob": current_blob,
    }


def render_report(results):
    drifted = [r for r in results if r["status"] == "drifted"]
    errors = [r for r in results if r["status"] == "error"]
    in_sync = [r for r in results if r["status"] == "in_sync"]

    if not drifted and not errors:
        return ""

    lines = ["# Upstream drift report", ""]
    lines.append(
        f"Checked {len(results)} third-party artifact(s): "
        f"**{len(in_sync)} in sync**, **{len(drifted)} drifted**, "
        f"**{len(errors)} error(s)**."
    )
    lines.append("")

    if drifted:
        lines.append("## Drifted")
        lines.append("")
        lines.append(
            "The following files have changed upstream since they were synced "
            "into `third-party/`. Review the upstream diff and re-sync if "
            "appropriate (copy the new upstream file over the local one and "
            "update `Upstream commit` + `Synced` in `ATTRIBUTIONS.md`)."
        )
        lines.append("")
        for d in drifted:
            owner = d["owner"]
            repo = d["repo"]
            path = d["path"]
            recorded = d["recorded_commit"]
            branch = d["default_branch"]
            recorded_url = f"https://github.com/{owner}/{repo}/blob/{recorded}/{path}"
            current_url = f"https://github.com/{owner}/{repo}/blob/{branch}/{path}"
            compare_url = f"https://github.com/{owner}/{repo}/compare/{recorded}...{branch}"
            lines.append(f"### `{d['name']}`")
            lines.append("")
            lines.append(f"- **Recorded**: [{recorded[:7]}]({recorded_url})")
            lines.append(f"- **Current ({branch})**: [{current_url}]({current_url})")
            lines.append(f"- **Compare**: [{recorded[:7]}...{branch}]({compare_url})")
            lines.append("")

    if errors:
        lines.append("## Errors")
        lines.append("")
        for e in errors:
            lines.append(f"- `{e['name']}` — {e['error']}")
        lines.append("")

    lines.append("---")
    lines.append(
        "_This report is generated by "
        "[`.github/workflows/check-drift.yml`](../blob/HEAD/.github/workflows/check-drift.yml)._"
    )
    return "\n".join(lines) + "\n"


def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not ATTRIBUTIONS_PATH.exists():
        print(f"{ATTRIBUTIONS_PATH} not found", file=sys.stderr)
        return 0

    text = ATTRIBUTIONS_PATH.read_text(encoding="utf-8")
    entries = parse_attributions(text)
    if not entries:
        print("No entries found in ATTRIBUTIONS.md; nothing to check.", file=sys.stderr)
        if REPORT_PATH.exists():
            REPORT_PATH.unlink()
        return 0

    results = [check_entry(e, token) for e in entries]
    report = render_report(results)

    if report:
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Drift or errors detected — report written to {REPORT_PATH}", file=sys.stderr)
    else:
        if REPORT_PATH.exists():
            REPORT_PATH.unlink()
        print("All third-party artifacts are in sync.", file=sys.stderr)

    # Print a compact JSON summary for the workflow logs.
    summary = [
        {k: v for k, v in r.items() if k in ("name", "status", "error", "default_branch")}
        for r in results
    ]
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

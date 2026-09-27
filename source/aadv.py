#!/usr/bin/python3
# giovanni
# Format a list of file paths (one per line on stdin) as Alfred items,
# optionally decorated with Finder label colors.

import sys
import json
import os
import subprocess

SHOWLABELS = os.getenv('showLabelColors')

COLORS = {'Gray': '⚪', 'Green': '🟢', 'Purple': '🟣',
          'Blue': '🔵', 'Yellow': '🟡', 'Red': '🔴', 'Orange': '🟠'}


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


def get_max_length():
    raw = os.getenv('MAXLENGTH', '').strip()
    try:
        return int(raw)
    except ValueError:
        return 100


def parse_tag_block(block):
    """Parse one `kMDItemUserTags = (...)` mdls block into a list of tag names."""
    if "(" not in block:
        return []
    inner = block.split("(", 1)[1].rsplit(")", 1)[0]
    if inner.strip() in ("", "null"):
        return []
    return [t.strip().strip('"') for t in inner.split(",") if t.strip()]


def finder_tags_batch(paths, chunk_size=200):
    """Finder tags for many files with one mdls call per chunk instead of
    one per file. Returns a list of tag lists aligned with paths."""
    all_tags = []
    for start in range(0, len(paths), chunk_size):
        chunk = paths[start:start + chunk_size]
        try:
            output = subprocess.run(
                ["mdls", "-name", "kMDItemUserTags"] + chunk,
                capture_output=True, text=True,
            ).stdout
        except OSError as e:
            log("mdls failed: %s", e)
            all_tags.extend([[]] * len(chunk))
            continue

        # one block per file, in argument order
        blocks = output.split("kMDItemUserTags")[1:]
        if len(blocks) == len(chunk):
            all_tags.extend(parse_tag_block(b) for b in blocks)
        else:
            # a missing/unreadable file breaks alignment: fall back per file
            for p in chunk:
                single = subprocess.run(
                    ["mdls", "-name", "kMDItemUserTags", p],
                    capture_output=True, text=True,
                ).stdout
                all_tags.append(parse_tag_block(single))
    return all_tags


def shorten(path, max_length):
    if max_length <= 0 or len(path) <= max_length:
        return path
    half = max(max_length // 2, 10)
    return path[:half] + " … " + path[-half:]


def main():
    paths = [line for line in sys.stdin.read().splitlines() if line.strip()]
    max_length = get_max_length()

    result = {"items": []}

    tags_per_path = None
    if SHOWLABELS == "1":
        tags_per_path = finder_tags_batch(paths)

    total = len(paths)
    for idx, path in enumerate(paths):
        tagString = ''
        if tags_per_path:
            tagString = "".join(COLORS[t] for t in tags_per_path[idx] if t in COLORS)

        fileName = os.path.basename(path)
        result["items"].append({
            "title": f"{fileName} {tagString}".rstrip(),
            "subtitle": f"{idx + 1}/{total}-{shorten(path, max_length)}",
            "type": "file",
            "icon": {"path": path, "type": "fileicon"},
            "valid": True,
            "arg": path,
        })

    if not result["items"]:
        result["items"].append({
            "title": "No matches",
            "subtitle": "Try a different query",
            "valid": False,
        })

    print(json.dumps(result))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Pick a meme from the catalog by tags, id or alias.

Usage:
  pick_meme.py <tag> [<tag> ...]   best match by tag overlap (random among ties)
  pick_meme.py --id <id|alias>     exact meme
  pick_meme.py --tags              list available tags
  pick_meme.py                     random meme
"""
import json
import random
import sys
import unicodedata
from pathlib import Path

MEMES_DIR = Path(__file__).resolve().parent.parent / "memes"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower().strip())
    return "".join(c for c in s if not unicodedata.combining(c))


def load():
    with open(MEMES_DIR / "catalog.json", encoding="utf-8") as f:
        return json.load(f)


def out(meme):
    print(json.dumps({
        "id": meme["id"],
        "path": str(MEMES_DIR / meme["file"]),
        "caption": meme.get("caption", ""),
        "tags": meme.get("tags", []),
    }, ensure_ascii=False))


def main(argv):
    catalog = load()
    if not catalog:
        sys.exit("catalog is empty")

    if argv[:1] == ["--tags"]:
        tags = sorted({norm(t) for m in catalog for t in m.get("tags", [])})
        print("\n".join(tags))
        return

    if argv[:1] == ["--id"]:
        if len(argv) < 2:
            sys.exit("--id needs a value")
        key = norm(" ".join(argv[1:]))
        for m in catalog:
            names = [m["id"], *m.get("aliases", [])]
            if key in (norm(n) for n in names):
                return out(m)
        sys.exit(f"no meme with id/alias '{key}'")

    wanted = {norm(t) for t in argv}
    if not wanted:
        return out(random.choice(catalog))

    scored = [(len(wanted & {norm(t) for t in m.get("tags", [])}), m) for m in catalog]
    best = max(s for s, _ in scored)
    if best == 0:
        sys.exit("no meme matches those tags")
    out(random.choice([m for s, m in scored if s == best]))


if __name__ == "__main__":
    main(sys.argv[1:])

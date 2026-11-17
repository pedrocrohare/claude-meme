# claude-meme 🦁🌹

A Claude skill that answers funny moments with reaction memes. When you're joking, shitposting, celebrating or sending memes yourself, Claude fires one back. When things are serious, it stays quiet.

## Install

**Claude Code**

```
/plugin marketplace add pedrocrohare/claude-meme
/plugin install claude-meme@claude-meme
```

**Claude app (claude.ai / desktop)**

Download [`web/meme-reply.zip`](web/meme-reply.zip) and upload it as a skill in Claude's settings. This version pulls memes live from this repo, so new memes show up without reinstalling. It needs a Claude session that can run commands and send files.

## Categories

42 reaction memes grouped by vibe: `risa`, `celebracion`, `fail`, `frustracion`, `sorpresa`, `confusion`, `ironia`, `decision`, `aliento`.

```
python3 skills/claude-meme/scripts/pick_meme.py --categories      # list everything
python3 skills/claude-meme/scripts/pick_meme.py --category fail   # random one from a category
```

## Add your own memes

1. Put the image in `skills/claude-meme/memes/`.
2. Add an entry to `skills/claude-meme/memes/catalog.json` with `id`, `file`, `caption`, `category`, `tags` and optional `aliases`.
3. Try it: `python3 skills/claude-meme/scripts/pick_meme.py <tag>`.

PRs with new memes welcome. Only submit images you have the right to share.

## Rules Claude follows

- Fires on jokes, laughter, celebrations, playful venting, memes, or when asked.
- Never on grief, health, money stress or real distress.
- Max one meme every few turns unless you ask for more.
- No meme that doesn't fit. A forced meme is worse than none.

## License

MIT

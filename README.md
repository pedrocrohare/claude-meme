# claude-meme 🦁🌹

A Claude skill that answers funny moments with reaction memes. When you're joking, shitposting, celebrating or sending memes yourself, Claude fires one back. When things are serious, it stays quiet.

## Install

**Claude Code**

```
/plugin marketplace add pedrocrohare/claude-meme
/plugin install claude-meme@claude-meme
```

**Claude app (claude.ai / desktop)**

Download `claude-meme.zip` from Releases (or zip the `skills/claude-meme` folder) and upload it in Settings → Capabilities → Skills.

## Add your own memes

1. Put the image in `skills/claude-meme/memes/`.
2. Add an entry to `skills/claude-meme/memes/catalog.json` with `id`, `file`, `caption`, `tags` and optional `aliases`.
3. Try it: `python3 skills/claude-meme/scripts/pick_meme.py <tag>`.

PRs with new memes welcome. Only submit images you have the right to share.

## Rules Claude follows

- Fires on jokes, laughter, celebrations, playful venting, memes, or when asked.
- Never on grief, health, money stress or real distress.
- Max one meme every few turns unless you ask for more.
- No meme that doesn't fit. A forced meme is worse than none.

## License

MIT

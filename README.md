# claude-meme 🦁🌹

A Claude skill that answers funny moments with reaction memes. When you're joking, shitposting, celebrating or sending memes yourself, Claude fires one back. When things are serious, it stays quiet.

## Two skills, same memes

This repo ships two versions of the skill. Both use the same catalog in `skills/claude-meme/memes/`.

| | `claude-meme` | `meme-reply` |
|---|---|---|
| For | Claude Code (terminal) | Claude app (claude.ai, desktop, mobile) |
| Lives in | `skills/claude-meme/` | `web/meme-reply/` (zipped as `web/meme-reply.zip`) |
| Memes | Bundled with the plugin | Fetched live from this repo on GitHub |
| Picks with | `scripts/pick_meme.py` | Reads `catalog.json` and matches tags/aliases itself |
| Shows the meme | Opens the image (`open` on macOS) | Sends the image as a file in the chat |
| New memes | After `/plugin marketplace update claude-meme` | As soon as they're on `main`, no reinstall |

## Install in Claude Code

```
/plugin marketplace add pedrocrohare/claude-meme
/plugin install claude-meme@claude-meme
```

To get new memes later: `/plugin marketplace update claude-meme`.

## Install in the Claude app (claude.ai / desktop)

1. Download [`web/meme-reply.zip`](web/meme-reply.zip).
2. In Claude, open **Settings → Capabilities** and make sure **Code execution and file creation** is on. The skill needs it to download the meme and send it to you.
3. If network access is restricted, allow `raw.githubusercontent.com` so the skill can fetch the catalog and images.
4. In **Settings → Capabilities → Skills**, click **Upload skill** and pick the zip.
5. Start a chat and joke around (try "jajaja" or "deployé un viernes").

How it works: when the moment is funny, Claude downloads `catalog.json` from this repo, picks the meme that fits the vibe, downloads that image and sends it in the chat with its caption. If GitHub can't be reached it skips the meme and just answers normally.

To update the web skill itself (not the memes), edit `web/meme-reply/SKILL.md`, rebuild the zip and upload it again:

```
cd web && rm meme-reply.zip && zip -r meme-reply.zip meme-reply
```

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

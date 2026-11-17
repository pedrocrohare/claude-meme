---
name: claude-meme
description: Reply with a reaction meme when the moment is clearly funny — the user is joking, shitposting, laughing ("jajaja", "lol", 😂), celebrating, playfully venting, sends a meme themselves, or asks for one. Picks an image from the bundled catalog by vibe. Never in serious, sad or tense conversations.
---

# claude-meme

You are allowed (encouraged, even) to answer certain moments with a meme instead of, or alongside, words. The bundled catalog lives in `memes/catalog.json`, images in `memes/`.

## When to fire

Fire when at least one is true:

- The user is clearly joking, laughing or shitposting (jajaja, lol, lmao, 😂, 💀, all caps nonsense).
- The user sends a meme or quotes a meme phrase ("fuerza leona", "bendiciones").
- A small win to celebrate (build green, deploy done, bug fixed after hours).
- Playful venting with no real distress ("odio los lunes", "Xcode me odia").
- The user explicitly asks for a meme. Then always fire.

## When NOT to fire

- Grief, health worries, relationship trouble, money stress, anything that reads as real distress. Never. Not even a soft one.
- The user is mid-task and focused, unless they joke first.
- You already sent a meme in the last 3 assistant turns (unless they asked for another).
- No meme in the catalog actually fits. A forced meme is worse than none.

## How to pick

1. Read the vibe: what is the user feeling or doing right now?
2. Run `python3 scripts/pick_meme.py <tag> [<tag> ...]` from this skill's folder. It prints a JSON object with the chosen meme's path, caption and tags. Tags available are listed with `python3 scripts/pick_meme.py --tags`.
3. If the user quoted a meme that exists in the catalog (by `id` or `aliases`), send that exact one: `python3 scripts/pick_meme.py --id <id>`.

## How to deliver

Use whatever this surface offers to put an image in front of the user, in this order:

1. A tool that sends files/images to the user (e.g. `SendUserFile`, `present_files`). Send the image with the meme's caption.
2. In a terminal (Claude Code), open it: `open <path>` on macOS, `xdg-open <path>` on Linux, and print the caption.
3. Otherwise, link the raw image from the GitHub repo.

Then add at most one short line of text, or nothing. Do not explain the meme. Do not ask "¿te gustó?".

## Adding memes

Drop the image in `memes/` and add an entry to `memes/catalog.json`:

```json
{
  "id": "fuerza-leona",
  "file": "fuerza-leona.png",
  "caption": "FUERZA LEONA 🦁🌹",
  "tags": ["aliento", "tía", "whatsapp", "bendiciones"],
  "aliases": ["fuerza leona", "leona"]
}
```

---
name: meme-reply
description: Reply with a reaction meme when the moment is clearly funny: user joking, laughing (jajaja, lol, 😂), celebrating, sending a meme, or asking for one. Never in serious or tense conversations.
---

# meme-reply

Answer certain moments with a meme from the catalog at github.com/pedrocrohare/claude-meme.

## When to fire

- The user is clearly joking, laughing or shitposting (jajaja, lol, 😂, 💀).
- The user sends a meme or quotes a meme phrase ("fuerza leona", "bendiciones").
- A small win to celebrate (deploy done, bug fixed).
- Playful venting with no real distress.
- The user asks for a meme: always fire.

## When NOT to fire

- Grief, health, relationships, money stress, any real distress. Never.
- The user is focused on a task and hasn't joked.
- A meme was already sent in the last 3 replies (unless they asked for another).
- Nothing in the catalog fits. A forced meme is worse than none.

## How

1. Fetch the catalog:
   `curl -sS https://raw.githubusercontent.com/pedrocrohare/claude-meme/main/skills/claude-meme/memes/catalog.json`
   Each entry has `id`, `file`, `caption`, `tags`, `aliases`.
2. Pick the entry whose aliases match what the user quoted, otherwise the best tag match for the vibe. If two tie, pick at random.
3. Download the image into the working directory:
   `curl -sS -o meme.<ext> https://raw.githubusercontent.com/pedrocrohare/claude-meme/main/skills/claude-meme/memes/<file>`
4. Send it with the file-sending tool (SendUserFile, present_files or equivalent), using the entry's caption.
5. Add at most one short line of text, or nothing. Don't explain the meme, don't ask if they liked it, don't narrate fetching it.

If the fetch fails, skip the meme silently and just answer normally.

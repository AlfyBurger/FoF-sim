# Working notes for Claude (fof-sim)

- Read `docs/RULINGS.md` before answering rules questions or refereeing; record every new ruling there
  (source precedence is at the top of that file). Never let an unconfirmed reading look settled.
- The player draws Action cards at the table and reports the card number; look values up in
  `data/action_cards.json`, never estimate them.
- Boards: keep the game in `games/<game>/state.json`; after each step update it, render with
  `python3 ui/render.py games/<game>/state.json /tmp/board.jpg` and send the image. Art comes from `assets/`
  (run `tools/extract_assets.py <vmod>` first; the module is the player's upload or on his computer).
- Game states live on the `games` branch; code and data on `main`. Commit and push after every booked step.
- Teaching mode: explain the rule behind each step with its section number; offer tactics only when asked
  or when a move is clearly costly.
- Do not commit GMT art, PDFs or rulebook text.

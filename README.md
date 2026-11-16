# fof-sim — Fields of Fire Deluxe referee and advisor

Private working repository for learning **Fields of Fire Deluxe** (GMT, Series Rules 3rd edition) with Claude,
following the `/boardgame-learning` process, adapted for a solo game:
the bot is a **referee** (keeps the game state, checks every move against the rules) and an **advisor**
(explains the options and rules at each step). Goal: the player's autonomy.

Scope: Deluxe Edition (Vol. I) only; focus on the Normandy campaign. The player draws the cards at the table
and reports card numbers.

## Layout
| path | content |
|---|---|
| `docs/RULINGS.md` | errata, clarifications, rulings settled with the player, open questions |
| `docs/SOURCES.md` | official sources (with URLs) and the Vassal module inventory |
| `docs/INVENTORY.md` | component checklist: procedures vs data |
| `data/action_cards.json` | the 50 Action cards (commands, word, icons, AT, combat table, hit effects, R# row) |
| `ui/render.py`, `ui/catalog.json` | renders a board image from a game's `state.json` with the Vassal art |
| `tools/extract_assets.py` | copies the needed images out of the Vassal module into `assets/` |
| `tools/ocr_action_cards.py` | helper used to read the action cards |
| `tests/` | data checks against the official worked examples (`python3 -m pytest tests`) |
| `games/` | game states (on the `games` branch) |

## Art and documents
GMT's card and counter art, rulebooks and mission books are **not** in this repository.
Render boards after extracting the art from your own copy of the official module:

    python3 tools/extract_assets.py FoF_All_Volumes_v5_0_2.vmod
    python3 ui/render.py games/<game>/state.json board.jpg

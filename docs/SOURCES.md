# Fields of Fire Deluxe — sources and component inventory (Stage 1.2–1.3 start)

Gathered 2026-11-16. Source precedence: user rulings > official clarifications/errata > Series Rules 3rd ed. text > rulebook examples > mission books / player aids > fan sources.

## Official sources (GMT, downloaded from the GMT support page links)
Base URL: https://gmtwebsiteassets.s3.us-west-2.amazonaws.com/FoF_Deluxe/

| File | Pages | Date in PDF | Notes |
|---|---|---|---|
| FoF_3rd_ed_series_rules_final(with+chapters).pdf | 96 | Sep 2024 | **Series Rules, 3rd Edition (final)**. Applies to all volumes. |
| FoF_Field_Manual_1-Basic_Training.pdf | 52 | Sep 2024 | Teaching: platoon and company training courses |
| FoF_Field_Manual_2-Advanced_Operations.pdf | 48 | Sep 2024 | Teaching: vehicles, air assault, defence, between missions |
| FoF_Deluxe-Keep_up_the_Fire(stand-alone+mission).pdf | 24 | Sep 2024 | Stand-alone mission + full example of play |
| FoF_Deluxe_Normandy_Campaign.pdf | 48 | Sep 2024 | Mission book |
| FoF_Deluxe-Naktong_River_Campaign.pdf | 44 | Sep 2024 | Mission book |
| FoF_Deluxe-Heartbreak_Ridge_Campaign.pdf | 48 | Sep 2024 | Mission book |
| FoF_Deluxe-Vietnam_Campaign.pdf | 56 | Sep 2024 | Mission book |
| FoF_PlayerAid_*.pdf (10 files) | 1–4 each | 2024 | Action Menus, Charts & Tables 1–2, Sequence of Play, Enemy Activity Check Hierarchy, Command Displays, Vehicle & AT chart, Air Assault Planner, Helicopter Control, Logsheets |
| FoF_Deluxe_Update_Kit_Counter_Guide_1016.pdf | 24 | Oct 2024 | Illustrated counter guide (Update Kit) |
| Drafts (superseded, kept apart): Series Rules 03-06-2024, Normandy 03-06-2024, Air Assault Planners | | Mar 2024 | Do not use for rulings |

**Missing:** "Rulebook & Mission Book Clarifications – May 2025" (listed on the GMT 2nd-printing product page, p-1197). The page could not be fetched from here and the file name could not be found. Needed before any ruling work. Also unknown: whether the 2nd printing changed the rulebook text beyond that file.

## Vassal module (user-supplied): FoF_All_Volumes_v5_0_2.vmod
Official GMT module, v5.0.2, maintained by Colin Parsons (series developer), Vassal 3.7.22. All art © GMT. 2,579 images.
- **Action deck:** A01–A50 + reshuffle card (A51), card images 274×384 (data printed on the image: R#, command/initiative numbers, Contact/Cover/Rally, combat table −4…+6, hit effects Vet/Line/Green, AT number, HQ radio icon, random-number row 2–12). Note: products list "Action Deck of 55 cards"; the module has 50 + reshuffle → open question.
- **Terrain decks:** Normandy N01–N55, Korea K01–K55, Vietnam V01–V55, Heartbreak Ridge cards, Keep Up the Fire, Staging Area and Fire Support Area cards; plus Vol II (Peleliu, Chosin, Hue), Bulge/Ardennes A01–A55, Long Tan, Vol 3 items. Terrain card data on image: cover modifier, vehicle traffic (No/Slow), burst modifier, cover draws, LOS/height values, LZ icon.
- **Counters:** 1,086 unit pieces (9th Infantry 279, Germans 149, North Koreans 102, NVA 82, VC 42, plus 5th Marines, 101st, 6RAR, Japanese, Chinese), markers (VOF, PDF, cover, ammo, commands, control, experience, skills, pyrotechnics, fire missions), many built from layered images.
- **Displays:** Command Displays (US Army / USMC, WWII-Korea and Vietnam), Deluxe Sequence of Play, Potential Contact draw piles (PC A/B/C), Fire Missions, Experience tracker, Pyrotechnics, Skills, transport load plans, helicopter staging areas, chart window (Command, Infantry combat, Vehicles & AT, Enemy contact, Enemy activity, Misc, Buildings cover, Urban LOS).

## Learning material (secondary)
- The Boardgames Chronicle (2025): Platoon Basics, Company Basics, Advanced Academy (video series following the Field Manuals), Keep Up the Fire playthrough, Normandy Mission 1 playthrough.
- Inside GMT: "Learning Fields of Fire", Deluxe news; Tony's Board Life playthroughs (Heartbreak Ridge, Keep Up the Fire).
- mtngrown.github.io: written Field Manual platoon runs (2025).
- Tabletop Simulator module for Deluxe (Steam workshop 3312602925) with an errata/clarification PDF added May 2025.

## Prior art (fan, code)
- **meatp-c/fof-ai-referee** (GitHub, MIT, updated 2026-11-14): Python "shadow board" referee for FoF Deluxe 3rd ed. ~19k lines, tests; validates each move, prints board changes, keeps game_state.json with undo; tested on Field Manual 1, full Normandy campaign, Naktong M1. Does not draw cards (player enters draws); no rule text or mission data included. Gaps: helicopters/air assault, urban combat, FPF/FPL, defensive setup. Candidate base or reference for our Stage 2 engine.
- **Jefferson1664/FOF** (GitHub, no licence shown): French browser turn assistant with mission tables; sources include "Errata & Clarifications — May 10, 2025".

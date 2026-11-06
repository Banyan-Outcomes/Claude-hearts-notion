# Troubleshooting

## Installing

**`render.py` says Python 3.11 is required.** It uses `tomllib` from the standard library. Install a newer Python (for example from python.org or Homebrew) and run it with `python3.12 scripts/render.py`.

**"Missing values" from `render.py`.** The list shows each key and the files that use it. `ID_` keys go in `ids.json` (without the `ID_` prefix); the rest come from `config.toml`. Use `"none"` for a module you skipped.

**Upload fails in the Claude app.** The zip must contain one folder named exactly like the skill's `name`, with `SKILL.md` inside. The zips in `dist/skills/` are built that way; don't re-zip the folder's contents directly.

**The installer created a second Organizer.** Move the newer one to the trash, then run `/cos-install` again; it reuses the existing pages by title.

## Daily use

**A skill can't find a page or database.** An ID in `ids.json` is wrong, or the item was moved to the trash or out of the workspace the connector can see. Open the page in Notion, copy the ID from its URL (the 32 characters at the end), fix `ids.json`, re-render and re-upload that skill.

**Notion query limit errors.** Some Notion plans limit SQL and rows-mode queries. The skills read through saved views (Projects Spreadsheet, To Do List, Time Entries Default, Daily Journal Recent) to stay under the limit. Check those views exist and haven't been filtered.

**Edits to the dashboard fail.** Notion's editing tool needs an exact text match. If you restyled a panel heavily, the skill may not find its text; it will say so. Re-run, or ask Claude to rewrite that panel once in the current style.

**notion-email misses mail.** Check the email connector in the Claude app. For Microsoft 365, reconnect if it was signed out; the connector sometimes needs re-authorizing.

**The evening report suggests time you already recorded.** It compares against Time Entries for the same project and date. Check the entry's Deal relation points at the right project.

**Captured to-dos you don't want.** Say "these aren't my to-dos" in the chat. Claude moves them to the trash after you confirm, and adds them to Not to-dos on the Skill Run Log so they never come back.

**Plans feel too full.** Tell day-plan so in the morning, and write it on the Energy Plan (for example "at most four things on days with more than two meetings"). The planners read it every run.

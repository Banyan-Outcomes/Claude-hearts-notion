# Working in this repo

This repo holds the Notion Chief of Staff: ten Claude skills, the Notion structure they depend on, and an installer.

- To install the system for the person you're working with, run the `cos-install` skill (`.claude/skills/cos-install/SKILL.md`).
- `skills/*/SKILL.md` are templates. `{{KEY}}` placeholders come from `config.toml`; `{{ID_KEY}}` placeholders come from `ids.json`. Never hand-edit files in `dist/`; edit the template and run `python3 scripts/render.py`.
- `templates/notion/structure.md` is the source of truth for page titles, database names, property names and option values. If you change a name there, change every skill that uses it, and the Notion Map template.
- `config.toml` and `ids.json` hold personal data and are git-ignored. Never commit them, and never put personal names, client names, email addresses or real Notion IDs into templates, docs or examples.
- Before committing, run `python3 scripts/scrub.py <your-terms-file>` with a list of names you never want published.
- Writing style for everything in this repo and everything the skills write: plain sentences in a middle register, dates as YYYY-MM-DD, no em dashes.

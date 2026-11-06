# Deploying the Notion Chief of Staff

This guide takes you from nothing to a working system. Plan on about an hour for the install and a week of light use before you turn on the planning layer.

There are two ways to install. Both end in the same place.

- **Path A, Claude Code (recommended).** Claude Code works in a clone of this repo. It can write `ids.json` and run the render script itself.
- **Path B, the Claude app only.** No terminal needed. You upload the installer as a skill, and Claude hands you the files to download.

Both paths install the daily skills into the **Claude app**, because that's where your Notion, email and calendar connectors live.

---

## Before you start (both paths)

### 1. Check your Claude plan

Skills need a Pro, Max, Team or Enterprise plan with code execution turned on.

- In the Claude app, open **Settings, Capabilities** and turn on **Code execution and file creation**.
- On Team and Enterprise, an owner may need to enable Skills for the organization first.

### 2. Connect the tools

In the Claude app, open **Settings, Connectors** and connect:

| Connector | Required? | Used by |
| --- | --- | --- |
| Notion | Required. Allow access to the workspace you'll use. | every skill |
| Gmail and Google Calendar, or Microsoft 365 (Outlook mail and calendar) | Required: at least one email and one calendar. Connect both if you use both. | notion-email, day-plan, week-plan, notion-eod |
| GitHub | Optional | notion-github |
| Slack | Optional | notion-email, for client channels you list |

Test them by opening a new chat and asking:

```text
Search my Notion for any page, list my meetings for tomorrow, and show the subject of the last email I received. Don't change anything.
```

If any part fails, reconnect that connector before going on.

### 3. Decide on a fresh workspace or your existing one

- **Starting fresh:** nothing to do. The installer creates a new `Organizer` page and builds everything under it.
- **You have lots of existing Notion content:** first run the prompt in [install/organize-prompt.md](install/organize-prompt.md) in a Claude chat. Claude proposes a tree and moves nothing until you approve. Do that before the install.

### 4. Fill in your config

Copy `config.example.toml` to `config.toml` and fill it in. Every field is explained in the file.

- **owner:** your name, your email addresses and your time zone.
- **company:** your company name and default hourly rate.
- **planning:** your lifelong goals, your life areas and the start date for the Daily Log.
- **todo:** your To Do categories and the one-sentence rule for choosing a category.
- **github, slack, meetups:** fill these in, or leave them empty to skip that module.

Path B users can skip this step; the installer asks you these questions in chat.

---

## Path A: install with Claude Code

### A1. Get the repo

```bash
git clone https://github.com/Banyan-Outcomes/Claude-hearts-notion.git
cd Claude-hearts-notion
cp config.example.toml config.toml
# edit config.toml
python3 --version    # must be 3.11 or newer
```

### A2. Connect Notion to Claude Code

Claude Code needs its own Notion connection for the install. Either:

- sign in to Claude Code with the same Claude account and enable your Claude app connectors in Claude Code (run `/mcp` and check that Notion is listed), or
- add Notion's MCP server to Claude Code:

  ```bash
  claude mcp add --transport http notion https://mcp.notion.com/mcp
  ```

  Then run `/mcp` inside Claude Code and sign in to Notion when prompted.

Email and calendar don't have to be connected in Claude Code. The installer only needs them for its optional smoke test, and you can run that in the Claude app.

### A3. Run the installer

```bash
claude
```

Then, inside Claude Code:

```text
/cos-install
```

The installer:

1. Reads `config.toml` and the templates.
2. Checks the connectors.
3. Builds every page, database, property and view in [templates/notion/structure.md](templates/notion/structure.md).
4. Writes the IDs to `ids.json`.
5. Runs `scripts/render.py`.
6. Fills in the dashboard, Notion Map, Goals, Energy Plan and Skill Run Log.

It asks you for your mantra, your lifelong goals and three questions about your energy, and it stops to ask before anything it can't undo.

If it stops partway, run `/cos-install` again. It finds what already exists by title and fills in only what's missing.

### A4. Check the render

```bash
python3 scripts/render.py --check   # prints "All placeholders have values."
python3 scripts/render.py           # writes dist/skills/*.zip and dist/pages/*.md
```

If `--check` lists missing keys:

- `ID_...` keys belong in `ids.json`. Put `"none"` for any module you skipped.
- Every other key belongs in `config.toml`.

Fix them and run it again.

### A5. Upload the skills to the Claude app

In the Claude app, open **Settings, Capabilities, Skills** and choose **Upload skill** once for each zip in `dist/skills/`. Turn each one on after it uploads.

Upload in this order, so the ones you start using first are there first:

1. `notion-update.zip`
2. `notion-inbox.zip`
3. `notion-librarian.zip`
4. `notion-email.zip`
5. `notion-github.zip` (skip if you don't use GitHub)
6. `notion-eod.zip`
7. `record-time.zip`
8. `month-plan.zip`
9. `week-plan.zip`
10. `day-plan.zip`

Each zip holds one folder named after the skill with its `SKILL.md` inside, which is the format the app expects.

To use the skills in Claude Code as well, run:

```bash
python3 scripts/render.py --install-claude-code
```

That copies them to `~/.claude/skills/`.

Then go to **After the install** below.

---

## Path B: install from the Claude app only

### B1. Download the repo

Download this repo as a ZIP from GitHub (**Code, Download ZIP**) and unzip it.

### B2. Build and upload the installer skill

The installer has to be uploaded as its own skill. If you have Python 3.11 or newer on any computer, run:

```bash
python3 scripts/package_installer.py    # writes dist/cos-install.zip
```

Without Python, build the zip by hand: make a folder named `cos-install`, copy `.claude/skills/cos-install/SKILL.md` into it, and zip that folder. On a Mac, the `.claude` folder is hidden in Finder; press Cmd+Shift+. to show it.

Then upload `cos-install.zip` under **Settings, Capabilities, Skills, Upload skill**, and turn it on.

### B3. Run it in a chat

Start a new chat in the Claude app. Attach these files from the unzipped repo:

- `README.md`
- `templates/notion/structure.md`
- every file in `templates/pages/`
- every `SKILL.md` in `skills/`
- `config.example.toml` (or your filled-in `config.toml`)
- `scripts/render.py`

Then type:

```text
/cos-install
```

Claude asks for your settings if there's no `config.toml`, checks your connectors, and builds the Notion structure. It then gives you three things to download: `ids.json`, the ten rendered skills as zips, and the filled-in page bodies.

### B4. Upload the rendered skills

Upload the ten zips under **Settings, Capabilities, Skills**, in the order listed in step A5. Keep `ids.json` and `config.toml` somewhere safe; you'll need them to re-render after any change.

---

## After the install (both paths)

### 1. Smoke test

In a new chat in the Claude app, run these and check each result:

| Run | You should see |
| --- | --- |
| `/notion-update` | An Activity line on the Chief of Staff Harness page about the install |
| Add "Buy printer paper this week" to the Inbox from your phone, then `/notion-inbox` | A To Do row with Status This Week, and an empty Inbox |
| `/notion-email` | A short report of notes made and People added; its line on the Skill Run Log now shows a time |
| `/notion-eod` | One combined report and a new row in the Daily Journal |

### 2. Use it lightly for a week

Follow [install/first-week.md](install/first-week.md). Start with `/notion-update` at the end of working chats and the Inbox for phone notes. Add the evening routine after a couple of days.

### 3. Schedule the evening routine

In the Claude app, ask:

```text
Create a scheduled task that runs /notion-eod every weekday at 9 PM my time.
```

Scheduled runs never stop to ask questions. They leave questions in the Inbox and on the Skill Run Log, and the report waits for you.

### 4. Run the planning kickoff

After a few days, run the three sittings in [install/kickoff.md](install/kickoff.md): a 20-question survey, a current-state review, then `/month-plan` and `/week-plan`. From the next morning on, start with `/day-plan`.

### 5. Optional: point Claude Projects at their pages

For each Claude Project you use for a client or project, add a line like this to the Project instructions:

```text
This project's Notion page is "Client A - Website Rebuild" (page ID 0123456789abcdef0123456789abcdef). Run /notion-update at the end of working sessions.
```

---

## Updating

**When you change `config.toml`, for example to add a category or a Slack channel:**

1. Run `python3 scripts/render.py`.
2. Re-upload the skills that changed. Uploading a skill with the same name replaces it; if the app doesn't let you, remove the old one first.

**When you change the Notion structure:**

1. Tell Claude what you changed and ask it to update the Notion Map.
2. If a page or database ID changed, update `ids.json` and re-render.

**When this repo gets a new version:**

1. Pull it with `git pull`.
2. Read the changes to `skills/`.
3. Re-render and re-upload.

Your `config.toml` and `ids.json` are git-ignored, so pulling never overwrites them.

## Uninstalling

1. Turn off or delete the skills under **Settings, Capabilities, Skills**.
2. Delete the scheduled task.
3. In Notion, move Organizer to the trash or keep it. The skills never stored anything outside Notion.

---

## Troubleshooting

See [docs/troubleshooting.md](docs/troubleshooting.md). The most common problems:

| Problem | Fix |
| --- | --- |
| A skill doesn't show up when you type `/` | Check it's turned on under Settings, Capabilities, Skills, and that code execution is on. |
| "Missing values" from `render.py` | Fill in the keys it lists in `config.toml` or `ids.json`; use `"none"` for skipped modules. |
| A skill says a page or database can't be found | An ID in `ids.json` is wrong or the item was moved to the trash. Fetch the page, copy its ID, re-render, re-upload. |
| Notion query limit errors | Make sure the views in the structure spec exist; the skills use them to stay under the limit. |
| notion-email finds nothing | Check that the email connector is connected in the Claude app, not only in Claude Code. |
| Duplicate to-dos or journal bullets | Two evening runs probably overlapped. Keep one scheduled task, and don't run /notion-eod by hand while the scheduled one is running. |

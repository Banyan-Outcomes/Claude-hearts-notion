---
name: cos-install
description: "Install the Notion Chief of Staff system: check the connectors, build the Notion pages and databases, record their IDs in ids.json, render the skills with config.toml, and set up the dashboard, Notion Map and page bodies. Use on /cos-install, or when someone asks to set up or install the chief-of-staff system."
---

# Install the Notion Chief of Staff

This skill builds the system described in this repository's README. It runs in two places:

- **Claude Code** in a clone of the repo (recommended): it can read the templates, write `ids.json` and run `scripts/render.py` itself.
- **Claude chat** with this skill uploaded and the repo files attached (or pasted): it does the same steps, but hands `ids.json` and the rendered files back to the person as downloads instead of writing them to disk.

Work through the steps in order. Use a task list so the person can see progress. Ask before anything that can't be undone; never delete anything.

## Step 0: Read the repo

Read `README.md`, `templates/notion/structure.md`, every file in `templates/pages/`, and `config.toml`. If `config.toml` doesn't exist, copy `config.example.toml` to `config.toml`, then ask the person for the values it needs, a few at a time: their first name, their email addresses, time zone, company name and default rate, To Do categories, lifelong goals and life areas, whether they use GitHub, Slack or a meetups list, and the date to count as Day 1 of the Daily Log (default: tomorrow). Write the answers into `config.toml`.

## Step 1: Check the connectors

Make one small, read-only call to each and report the result in a short table:

| Connector | Test | Needed for |
| --- | --- | --- |
| Notion | `notion-search` for "Organizer" | everything |
| Email (Gmail and/or Microsoft 365) | search the last day of mail | notion-email, notion-eod |
| Calendar (Google and/or Outlook) | list today's events | day-plan, notion-email |
| GitHub | `get_me` | notion-github (optional) |
| Slack | search channels | notion-email's client channels (optional) |

If Notion fails, stop and explain how to connect it (Claude settings, Connectors, Notion, then allow access to the workspace). If email or calendar fails, continue, and note which skills will be limited.

## Step 2: Existing workspace or fresh start

Search Notion for an existing `Organizer` page and for databases named Clients, Projects, People and To Do List.

- **Nothing found:** build everything fresh in Step 3.
- **An Organizer exists from a previous run:** reuse every page and database whose title matches the spec, and create only what's missing. Never create a second Organizer.
- **The person has other Notion content:** ask whether to run the organize prompt first (`install/organize-prompt.md`). If they say yes, stop here and do that; it is a separate conversation with its own approvals. If they say no, build the new structure alongside their content and leave their pages alone.
- **They already have Clients, Projects or People databases elsewhere:** ask whether to move them under the new work area and add the missing properties, or to create fresh ones.

## Step 3: Build the structure

Follow `templates/notion/structure.md` exactly: page titles, database names, property names, types and option values, relations and views. The skills depend on those names.

1. Create the pages top-down: a parent must exist before its children. Create Organizer as a private top-level page.
2. Create each database under its parent with all of its properties. Create relations after both ends exist. Create the rollup and formula properties last.
3. Create the views listed in the spec (Projects Spreadsheet, To Do List List, Time Entries Default, Daily Journal Recent, Meetup Events Upcoming). The skills query rows through these views, which avoids the query limits some Notion plans place on SQL and rows-mode queries.
4. Skip any optional module the person turned off in `config.toml` (GitHub means Code and Repositories; meetups means Meetups and Meetup Events). Ask about the Daily Log, Home and AI News if config doesn't say.
5. After each item, fetch it once to read its ID, and record it under the key the spec gives. Page IDs are the 32 hex characters from the URL. For a database, record the data source UUID from its `collection://` URL, without the prefix. For a view, the UUID from its `view://` URL. Use `"none"` for modules that were skipped.

## Step 4: Write ids.json

Write every key from `ids.example.json` into `ids.json` at the repo root, with the IDs from Step 3. In chat, show the finished JSON in a code block and offer it as a file to download.

## Step 5: Render the skills and pages

In Claude Code, run:

```bash
python3 scripts/render.py --check
python3 scripts/render.py
```

Fix anything `--check` reports as missing, then render. The result is `dist/skills/<name>/SKILL.md`, one zip per skill in `dist/skills/`, and page bodies in `dist/pages/`.

In chat without a shell, do the same substitution yourself: for every `{{KEY}}` in each `skills/*/SKILL.md` and `templates/pages/*.md`, put the value from `config.toml` or `ids.json` (an `ID_` prefix means the key comes from `ids.json`). `scripts/render.py` shows how list values are joined. Then give the person each rendered skill as a file.

## Step 6: Fill the pages

Using the rendered bodies in `dist/pages/`:

- **Skill Run Log**: `skill-run-log.md`.
- **Inbox**: `inbox.md`.
- **Chief of Staff Harness**: `harness.md`.
- **Goals**: `goals.md`. Ask the person for their mantra and lifelong goals and put them in; this is their page, so write only what they give you.
- **Vision**: `vision.md`, one heading per life area.
- **Energy Plan**: `energy-plan.md`. Ask the three questions in "What works" (when they're sharpest, what resets them, what motivates them) and fill in their answers.
- **Meetups**: `meetups.md`, if the module is on.
- **Organizer**: the dashboard from `dashboard.md` at the top, with today's date and the mantra in the green callout, then the page links in two columns as the spec describes.
- **Notion Map**: `notion-map.md`, last. Then fetch it once and check that every ID in its tables is a real ID, not a placeholder.

## Step 7: Install the skills

Tell the person how to install the rendered skills where they'll use them:

- **Claude (web, desktop or mobile):** upload each zip in `dist/skills/` under Settings, Capabilities, Skills. Upload `notion-update` first.
- **Claude Code:** run `python3 scripts/render.py --install-claude-code` to copy them to `~/.claude/skills/`.

They need to be installed where the Notion, email and calendar connectors are also connected; for most people that's the Claude app.

## Step 8: Smoke test

Run these, in this order, and show the result of each in one line:

1. `/notion-update` on this conversation. It should add an Activity line to Chief of Staff Harness.
2. Ask the person to add one test note to the Inbox from their phone ("Buy printer paper this week"), then run `/notion-inbox`. A To Do row should appear and the Inbox should be clear.
3. `/notion-email`. It should report notes made and People rows added, and stamp its line on the Skill Run Log.

## Step 9: Next steps

Finish with a short summary: what was built (with a link to Organizer), what was skipped, and these next steps:

1. Use `/notion-update` at the end of working chats for a few days.
2. Follow `install/first-week.md`.
3. Run the planning kickoff in `install/kickoff.md`, then `/month-plan` and `/week-plan`.
4. Schedule `/notion-eod` for weekday evenings (ask Claude: "Schedule a task that runs /notion-eod every weekday at 9 PM").

Record the install on the Chief of Staff Harness page under `## Activity` and `## Decisions` (which modules were turned on or off).

## Rules

- Never delete. Archive instead, and only with a yes.
- Never change text the person wrote; only add and move with approval.
- Never copy passwords, tokens or account numbers into Notion or into `config.toml`.
- Write plain sentences, dates as YYYY-MM-DD, and never use em dashes.

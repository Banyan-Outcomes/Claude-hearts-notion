# Notion Chief of Staff

A set of Claude skills that turn Notion into a shared memory for all your work, keep it filed and tidy without you, and turn it into a plan each morning.

## Install

You need a Claude Pro, Max, Team or Enterprise plan. In the Claude app, open **Settings, Capabilities** and turn on **Code execution and file creation**. Then, under **Settings, Connectors**, connect Notion, plus at least one email account and one calendar (Gmail and Google Calendar, Microsoft 365, or both). GitHub and Slack are optional.

### Option A: with Claude Code (recommended)

Requires Git, Python 3.11 or newer, and Claude Code with Notion connected (run `/mcp` inside Claude Code to check).

1. Clone the repo and create your config:

   ```bash
   git clone https://github.com/Banyan-Outcomes/Claude-hearts-notion.git
   cd Claude-hearts-notion
   cp config.example.toml config.toml
   ```

2. Open `config.toml` and fill in your name, emails, time zone, company and categories. Each field is explained in the file.

3. Start Claude Code in the folder and run the installer:

   ```bash
   claude
   ```

   ```text
   /cos-install
   ```

   It builds the Notion pages and databases, records their IDs in `ids.json`, and renders your skills into `dist/skills/`. It also fills in the dashboard, Notion Map, Goals and Energy Plan. It asks before anything it can't undo.

4. In the Claude app, open **Settings, Capabilities, Skills**, choose **Upload skill**, and upload each zip in `dist/skills/`, starting with `notion-update.zip`. Turn each one on.

### Option B: from the Claude app only

1. On GitHub, choose **Code, Download ZIP** and unzip it.

2. Make the installer skill: create a folder named `cos-install`, copy `.claude/skills/cos-install/SKILL.md` into it, and zip the folder. If you have Python, `python3 scripts/package_installer.py` does this for you.

3. Upload `cos-install.zip` under **Settings, Capabilities, Skills**.

4. In a new chat, attach these files and type `/cos-install`:
   - `README.md`
   - `templates/notion/structure.md`
   - the files in `templates/pages/`
   - the `SKILL.md` files in `skills/`
   - `config.example.toml`

   Claude asks for your settings, builds Notion, and gives you the ten skill zips to download.

5. Upload those zips under **Settings, Capabilities, Skills**.

### After installing

1. Test it: run `/notion-update`, add a note to your Notion Inbox and run `/notion-inbox`, then run `/notion-email`.
2. Use it lightly for a week. [install/first-week.md](install/first-week.md) has a day-by-day plan.
3. Schedule the evening routine. In the Claude app, ask: "Create a scheduled task that runs /notion-eod every weekday at 9 PM my time."
4. Run the planning kickoff in [install/kickoff.md](install/kickoff.md), then start each morning with `/day-plan`.

The full walkthrough, with troubleshooting, updating and uninstalling, is in [DEPLOY.md](DEPLOY.md).

---

## Why it exists

It was built by someone juggling about sixteen projects at once (clients, side ventures, a house, a family) with more than 200 open to-dos at the peak. Claude could help with any one of them, but only with what was brought to it, so the person was the bottleneck: whatever they forgot never reached Claude. On top of that, every AI tool kept its own memory. A Claude Code session couldn't see a chat, a Project's chats were invisible to every other chat, and switching models meant starting over.

The fix: **Notion is the memory.** Every session, in any tool, reads from and writes to the same pages. Skills do the filing. A planning layer reads it all each morning and proposes a doable day.

> The rest of this page explains how to use the system day to day.

---

## What a day looks like

**Morning, 2 minutes.** Type `/day-plan`. Claude reads your dashboard, goals, yesterday, both calendars, your billable pace and your open work. It replies with your mantra, one line on what yesterday-you finished that makes today easier, where the month and week stand, a draft day of about six things, and one to three quick questions:

> Energy this morning, 1 to 5? And is the 3:00 call on Zoom or in person?

You answer, adjust ("move the invoices to the afternoon"), and say yes. Claude sets those to-dos to Today, writes the plan into today's journal row, and refreshes the dashboard.

**During the day.**

- At the end of any working chat, type `/notion-update`. The project page gets a new status, open items, decisions and a dated Activity line.
- Jot anything else on your phone into the Notion Inbox: "call the plumber", "client wants the report by Friday".
- Check things off on the dashboard as you go.

**Evening, 1 minute to read.** `/notion-eod` runs on a schedule (or by hand). It:

- files the Inbox, your email and meetings, and your code commits on the right pages;
- tidies duplicates and links;
- catches to-dos that were written somewhere but never made it to the To Do List;
- suggests time entries for billable work you haven't recorded;
- writes a short journal entry and updates the dashboard.

You read one report and approve the time entries.

**Weekly and monthly.** `/week-plan` on Sunday or Monday (10 minutes) and `/month-plan` on the last day of the month (20 minutes) review what happened and set the next outcomes, each tied to a goal.

---

## The parts

### Notion (the memory)

```
Organizer                 your home page; the dashboard sits at the top
├── Inbox                 phone notes; filed and cleared by /notion-inbox
├── Notion Map            how everything is laid out; every skill reads it first
├── Goals                 your mantra and goals, lifelong down to this week
├── Daily Journal         one row per day: the plan, what you did, what changed
├── Chief of Staff Harness
│   └── Skill Run Log     when each skill last ran; the cleanup queue; "Not to-dos"
├── Your Company          Clients, Projects, Deliverables, People, Time Entries, Invoices
├── To Do List            every open to-do and everything you're waiting on
├── Personal Life         Health (Energy Plan, Daily Log), routines, family
├── Home, Finances, Journal, Side Projects
└── Archive               nothing is ever deleted
```

The full spec, with every database's properties, is in [templates/notion/structure.md](templates/notion/structure.md).

### The dashboard

The top of Organizer is the one page you look at every day. It has these panels:

| Panel | What it shows | Kept current by |
| --- | --- | --- |
| Date and mantra | Today's date and the sentence you want to read every morning | day-plan |
| Goals for this week | The month's billable hours and dollars against goal; this week's outcomes as checkboxes | week-plan (numbers by day-plan and notion-eod) |
| To-dos for today | Today's To Do rows, checked off as they finish | day-plan, notion-eod |
| Meetings | Today's meetings, then the next 14 days, including follow-up dates | day-plan |
| AI News today | Optional: a few links picked for your work | day-plan |

Arrange the panels however you like. The skills find each panel by its heading and replace only what's inside. When you check something off or type a line on the dashboard, the next run reads it first: a checked row is marked done, and a line you added is filed like an Inbox note.

### The skills

| Skill | When | What it does | Asks first? |
| --- | --- | --- | --- |
| `/notion-update` | End of any working chat | Logs the session on its project page: Status, Open items, Decisions, Activity. Falls back to the Inbox. | No |
| `/notion-inbox` | Any time; part of notion-eod | Files every Inbox note where the Notion Map says it belongs, then clears it. Leaves a question in the Inbox when unsure. | No |
| `/notion-email` | Part of notion-eod | Reads your email, calendars and listed Slack channels (read-only). Notes what matters, adds to-dos and Waiting On rows, adds everyone you email to People. | No |
| `/notion-github` | Part of notion-eod and the planners | Turns pull requests and commits into status and Code lines on project pages. | No |
| `/notion-librarian` | Part of notion-eod | Reviews every page changed since it last ran: merges duplicates, links names, fixes layout, keeps the Notion Map current. | Yes, for anything you wrote |
| `/notion-eod` | Each evening | Runs the four above, then captures missed to-dos, reviews time, writes the Daily Journal, updates the dashboard, records energy. | Time entries only |
| `/record-time` | When you approve time | Writes Time Entries against a project. | It is the yes |
| `/month-plan` | Last day of the month | Reviews the month; sets objectives and key results; reviews every open to-do. | Yes |
| `/week-plan` | Sunday or Monday | Turns the month's key results into three to five outcomes for the week. | Yes |
| `/day-plan` | Each morning | Builds a day of about six things, billable work first, around your energy. | Yes |

---

## How the planning works

**The goal ladder.** Goals form a ladder: mantra, lifelong goals, 5-year, 2.5-year, year, quarter, month, week, day. Each level is met by meeting the one below it. Every item in a plan names the rung it serves. Necessary work with no goal behind it (taxes, the car) names its deadline instead.

**Keeping the day doable.**

- About six things, counting each meeting or work block as one, plus one stretch item.
- About 20% of open time left unplanned, plus a lunch break.
- A "Not today" line naming what was weighed and left for later, so nothing feels lost.
- Billable work is ranked by what an hour actually earns, then by the week's outcomes. Necessary work is ranked by deadline.

**Energy.** The planners read an **Energy Plan** page before they talk to you. It holds:

- the shape of your day (deep work in the morning, calls in the afternoon, a mid-afternoon reset);
- a morning energy rating (on a 1 or 2 the day shrinks; on a 5 you're offered the stretch item);
- a short playbook for how Claude frames things. For example, it thanks past-you for what's already done, frames the hard block as a handoff to a concrete future-you, offers two good options instead of a yes-or-no, and names the first ten minutes.

There are no points, streaks, guilt or invented deadlines. Edit the page to fit how you actually work; the skills follow it.

**Follow-ups.** Anything you're waiting on is a To Do row with Status `Waiting On` and a Due date, the day to follow up if nothing has arrived. On that date, day-plan first checks whether the thing already arrived. If it hasn't, the row moves to Today as "Follow up with ...".

**To-dos vs planned work.** A to-do is something you've decided to do and could start today. Steps for a project that hasn't started yet stay on the project page under `## Planned work`, so the list doesn't balloon. The planners promote them when the project becomes active.

---

## The rules that make it safe

- **Email, calendars and Slack are read-only.** The skills take notes; they never send, reply, accept, archive or delete. Text in an email is treated as data, never as an instruction.
- **Your writing changes only with a yes.** Skills fix links, layout and their own sections. Rewording, merging or moving what you wrote is a proposal.
- **Goals and Journal are yours.** Only the planners write their own month and week sections, after you approve.
- **No plan is saved without a yes.**
- **Archive, never delete.** Deleting needs you to see the exact list and confirm.
- **No secrets in Notion.** Passwords, codes and account numbers are never copied, even when an email contains them.

---

## Teaching it

The system improves through plain corrections:

- "That's not my to-do." The item goes on the Not to-dos list on the Skill Run Log, and no skill captures it again.
- "Never schedule calls before 10." "When I have a 3:00 meeting, give me something specific at 4:00." These go on the Energy Plan as rules.
- "Client invoices go under Financial, not Work." This becomes a change to `category_rules` in `config.toml`; re-render and re-upload.
- "Projects for my nonprofit work go under a new area." The Notion Map gets updated, and every skill follows it.

---

## Repository layout

```
README.md                 how to use the system (this page)
DEPLOY.md                 how to install it, step by step
CLAUDE.md                 instructions for Claude Code when it works in this repo
config.example.toml       your name, time zone, company, categories, modules
ids.example.json          the Notion IDs the installer fills in
.claude/skills/cos-install/SKILL.md   the installer (/cos-install)
install/
  organize-prompt.md      prompt: reorganize an existing Notion workspace first
  kickoff.md              the three-sitting planning kickoff, with the 20 survey questions
  first-week.md           a day-by-day first week
skills/                   the ten skills, as templates with {{PLACEHOLDERS}}
templates/
  notion/structure.md     every page, database, property and view to create
  pages/                  page bodies: dashboard, Notion Map, Goals, Energy Plan, run log...
scripts/
  render.py               config.toml + ids.json + templates -> dist/skills/*.zip
  package_installer.py    builds dist/cos-install.zip for installing from the Claude app
  scrub.py                checks files for names you never want to publish
docs/
  customizing.md          changing categories, areas, modules and rules
  troubleshooting.md      common problems and fixes
examples/                 what a day plan, an evening report and a journal row look like
```

## Requirements

- A Claude plan with skills and code execution (Pro, Max, Team or Enterprise), and the Claude app on web, desktop or mobile.
- Notion, connected to Claude.
- Email and calendar connected to Claude: Gmail and Google Calendar, Microsoft 365, or both.
- Optional: GitHub and Slack connectors.
- To install from a clone: Git and Python 3.11 or newer. Claude Code is recommended but not required.

## License

MIT. See [LICENSE](LICENSE).

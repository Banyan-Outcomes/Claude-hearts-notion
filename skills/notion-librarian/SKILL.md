---
name: "notion-librarian"
description: "Review what changed in {{OWNER}}'s Notion since the last run and tidy it: merge duplicates, fix links and layout, keep the Notion Map and the Meetups event list current. Use on /notion-librarian or to clean up Notion."
---

# Notion Librarian

{{OWNER}}'s Notion is written by {{OWNER}} on {{OWNER}}'s phone and desktop and by several skills (notion-update, notion-inbox, notion-email, update-crm, and the deal and billing skills). Over time that produces the same fact in two places, names typed as plain text instead of links, pages in the wrong place and sections out of order. This skill reviews everything that changed since it last ran and tidies it, so that {{OWNER}} or an AI can open any page, understand what it holds, and follow its links to everything related. It works inside Notion, plus one outside source: it reads the public event sites listed on the Meetups page to keep that list current (Step 6).

## What it changes on its own, and what needs a yes

**Do without asking.** These changes are reversible and touch only structure or skill-written text:

- Turn plain-text names of People, Clients, Projects, Deliverables and other pages into mention-page links.
- Fill a missing relation when the match is unambiguous: a To Do row's `Person` when its task names someone in People; a To Do row's `Client`, `Project` and `Deliverable` when it is client work and its source page or wording names them (`Client` is the project's Company, and personal, house and side-project rows leave all three empty); a Deliverable's `Deal`, a Project's `Company`, a person's `Companies`.
- In skill-written sections, merge duplicate or near-duplicate lines, put Activity lines in date order (oldest first), write dates as YYYY-MM-DD, and add any layout section the map calls for that is missing. Skill-written sections are Status, Open items, Decisions and Activity, plus any line that starts with a date followed by Chat, Code, Email or Meeting.
- Move a clear stray note, such as a phone note about the camper sitting under {{COMPANY}} / AI News, to where the map says it belongs.
- Add a one-sentence purpose line at the top of an area page or database that lacks one, saying what it holds. Never on Goals, Journal, or a page that is {{OWNER}}'s own writing.
- Keep the Notion Map current (Step 5).
- Add and update rows in the Meetup Events database, and keep the recurring-events line on the Meetups page current (Step 6).

**Ask first.** List these as numbered proposals and act only on {{OWNER}}'s yes:

- Any change to text {{OWNER}} wrote {{OWNER}}: rewording it, moving it, merging it or removing it.
- Merging two pages or two database rows, or moving either one to Archive.
- Renaming a page {{OWNER}} created.
- Moving a page that is not a clear stray.
- Changing database properties, views, or the shape of the tree. (Recording on the map a change that has already been made needs no yes.)
- Trashing anything. Archive is the default; use `notion-delete-pages` only after {{OWNER}} confirms the exact list.

**Never** write in Goals or Journal, never delete without a yes, and never remove the tags that embed child pages and databases in a page.

Write plain sentences in a middle register, dates as YYYY-MM-DD, and never use em dashes.

## Run log

The **Skill Run Log** page under Chief of Staff Harness (`{{ID_HARNESS_PAGE_ID}}`) records when each Notion skill last ran and queues the pages they changed for this skill. Its `## Not to-dos` section lists items {{OWNER}} has said are not {{OWNER}}'s to-dos; never turn those into To Do rows. Find the log with `notion-search` for "Skill Run Log" limited to that page. If it does not exist, create it there with this content:

```
The Notion skills keep this page. It records when each one last ran and lists the pages changed since notion-librarian last reviewed them.
## Last runs
- notion-inbox: never
- notion-email: never
- notion-librarian: never
## Changed since the librarian last ran
## Waiting for {{OWNER}}
## Not to-dos
```

Times are written `YYYY-MM-DD HH:MM MT`.

## Step 1: Read the map and the run log

1. Fetch the **Notion Map** (`{{ID_NOTION_MAP_PAGE_ID}}`). It is the authority on the tree, page layouts, database fields, which skill owns what, and conventions. Every judgment in this skill about where something belongs or how a page should look comes from the map.
2. Read the run log. The notion-librarian line starts this run's window, and the window ends now (get the current time from the current-time tool). If it says `never`, use the past 7 days.
3. Note any proposals under `## Waiting for {{OWNER}}`. Present those first in Step 4.

## Step 2: Find what changed

Build a list of changed pages from these sources, removing duplicates:

1. **The queue**: every page mentioned under `## Changed since the librarian last ran`. These are known changes from notion-inbox, notion-email, notion-eod and chat sessions.
2. **New pages**: `notion-search` with an empty query and a `created_date_range` covering the window, limited to Organizer (`page_url`). A search returns at most 50 results, so when one comes back full, repeat it for each top-level area the map lists ({{COMPANY}}, To Do List, Personal Life, the side projects, Home, Bathroom Remodel, Investments and Finance, Chief of Staff Harness) until every search returns fewer than 50.
3. **Project work**: Projects and Deliverables rows whose `Last activity` falls in the window (rows mode with a date filter). notion-update stamps this field.
4. **{{OWNER}}'s own edits**: `notion-list-recent-pages` with a limit of 50, then fetch each and keep those whose `page_last_edited_at` falls in the window. If search accepts `last_edited_date_range` with `edited_by_user_ids: ["me"]` (a Business plan feature that this workspace's plan currently drops with a notice), use it as well.

Leave out the Skill Run Log, the Notion Map (Step 5 handles it), Goals, Journal, rows in Invoices and Time Entries, which the billing skills own, and rows in Meetup Events (Step 6 handles them).

If the list holds more than about 60 pages, review the 60 most recently edited, and add the rest to the queue so the next run starts with them.

## Step 3: Review each changed page

Fetch each page and check it against the map:

- **Redundancy.** Is the same fact recorded somewhere else? Common cases are the same to-do as two To Do rows, the same meeting logged by both notion-update and notion-email, a status repeated on a client page and its project page, an Inbox note filed twice, and two Maintenance Log rows for the same job. The canonical copy lives where the map says that kind of fact belongs; anywhere else it should be a link rather than a second copy. One exception: the map allows a project page to repeat a Waiting On item as an open item, so that pair is not a duplicate.
- **Links.** Names of people, clients, projects and pages should be mention-page links, and database relations should be set where the page names the related row. On To Do rows that means `Person`, and for client work `Client`, `Project` and `Deliverable`.
- **Placement.** The page should sit where the map says its kind of content belongs.
- **Layout.** Project and deliverable pages follow the map's section order (Status, Open items, Decisions, dated notes, Activity at the bottom). Plain area pages carry Open items and Activity at the end.
- **Readability.** The title names the page's subject rather than reading like a sentence; area pages and databases open with a purpose line; there are no empty sections, leftover template text or empty bullets. A page created in the window with no content goes on the proposal list, not in the trash.

Make the changes the first list allows, and collect everything else as proposals.

## Step 4: Ask about the rest

List the proposals in chat as a numbered list, starting with any carried over from `## Waiting for {{OWNER}}`. Give each one a page link and one line saying what you would change and why. Carry out the ones {{OWNER}} approves. Write any {{OWNER}} does not answer under `## Waiting for {{OWNER}}` on the run log, replacing older proposals about the same page, and remove the ones {{OWNER}} approved or declined.

## Step 5: Keep the map current

Edit the Notion Map so it still describes Notion as it now stands:

- **Tree, Databases and Key pages**: add any new structural page or database (an area page, a database, a page other skills rely on) with its ID, and update anything moved, renamed or archived.
- **Database fields**: fetch the schema of Clients, Projects, Deliverables, People and the To Do List (their data source IDs are in the map's Databases table), and make the property lists and the To Do convention on the map match them: add new properties, remove deleted ones and note renames. Do this every run, because a field added in a chat session changes no page and would otherwise go unnoticed.
- **Who writes what**: make sure the table lists notion-inbox (files Inbox entries and loose top-level pages), notion-email (notes from email and calendar, the To Do rows that come from them, and basic People rows and addresses for everyone {{OWNER}} emails), notion-librarian (consolidating, linking, layout, this map and the Meetup Events database) and notion-eod (runs the three, captures missing to-dos, reviews time and billing). Replace any older row that says the librarian files Inbox entries, and update the Inbox line in the tree to match.
- **Conventions**: if missing, add `- Inbox entries are removed once notion-inbox files them; they are not archived.`, `- The Skill Run Log under Chief of Staff Harness records when each Notion skill last ran.` and the line saying that items under `## Not to-dos` on the Skill Run Log never become To Do rows.

Make other map edits only when something this run found or changed is not yet described.

## Step 6: Keep the Meetups list current

The **Meetups** page under {{COMPANY}} (`{{ID_MEETUPS_PAGE_ID}}`) lists local events {{OWNER}} may want to attend, mostly on AI and entrepreneurship. Its **Meetup Events** database (`collection://{{ID_MEETUP_EVENTS_DATA_SOURCE}}`) holds one row per event, with the properties Event (title), Date, Organization (one option per source below), Location, Link, Status (New, Interested, Going, Skip), First seen and Notes. Check every source on every run, whatever else changed.

1. **Read each site** with WebFetch (the shell can't reach most sites), asking for every upcoming event's exact title, date and time, location and link. The sources:
{{MEETUP_SOURCES}}
   Meetup.com group pages work better than their `/events/` pages, which often come back empty to WebFetch. Pages often show a date without the year; take the year from the weekday.
   Also read the Organizations list on the Meetups page. If {{OWNER}} has added an organization there, check its site too, and propose adding it as an Organization option (a database change needs a yes).
2. **Recurring events.** Weekly or monthly events that never change (a standing game night, a weekly open house) don't get rows; list them in one line under "How the list is kept" on the Meetups page and update that line when the site changes.

3. **Compare with the database.** List its rows in view mode through the Upcoming view (`view://{{ID_MEETUPS_UPCOMING_VIEW}}`, which shows events from today on that aren't marked Skip) and match each fetched event to a row by Link, or by title and date when several events share a link.
4. **Add each event that has no row**: Event, Date (start and end in local time with the right offset, -06:00 before the first Sunday in November and -07:00 after), Organization, Location, Link, Status `New` and First seen today. Put a short Notes line on anything {{OWNER}} should know, such as ticket prices, whether the public can come, two events at the same time, or a client meeting the same day when the calendar has already been read in this run (as notion-eod does).
5. **Update rows that changed**: a new date, time, location or link. Say what changed and when in Notes. If an upcoming event disappears from its site before its date, add `No longer listed as of YYYY-MM-DD` to Notes. Never delete rows, and never change Status except to set `New` on rows you add; {{OWNER}} sets Interested, Going and Skip.
6. **If a site can't be reached**, leave its rows alone and say so in the report.

## Step 7: Clear the queue and stamp the run

Remove the queue lines this run reviewed, leaving any pages added back in Step 2. Then set the notion-librarian line under `## Last runs` to the time this run started.

## Step 8: Report

Reply in a few short lines, grouped:

- **Changed**: what was merged, linked, moved and restructured, with page links.
- **New events**: each event added to Meetups this run, with its date, organization and a link to its row, plus any changed or no-longer-listed events and any change to the recurring events. If there were none, say "No new events on Meetups."
- **Waiting for you**: the numbered proposals still open.
- **Map**: any edits to the Notion Map.

If nothing needed changing, say so in one line, and still give the New events line.

## Notion gotchas

- Always fetch a page before editing it. `update_content` needs an `old_str` that matches the page text exactly. Prefer `update_content` over `replace_content`, and never use `replace_content` on a page that embeds child pages or databases.
- Keep each `old_str` short. An `old_str` longer than about 700 characters, or one that starts a bullet with a mention, often fails to match even when it is copied exactly; split it into smaller edits.
- Never remove the tags that embed child pages and databases in a page; removing one moves or deletes the child.
- Relation values are arrays of page URLs. Dates use the expanded form, such as `date:Due:start`. Checkboxes use `__YES__` and `__NO__`.
- Link to other Notion pages with mention-page tags rather than plain links.
- SQL mode of Query Data Source can hit the workspace plan limit. Use rows mode, view mode, `notion-search` or `notion-fetch` instead.

## Quick reference (use only if the map can't be read)

- Notion Map `{{ID_NOTION_MAP_PAGE_ID}}`, Organizer `{{ID_ORGANIZER_PAGE_ID}}`, Inbox `{{ID_INBOX_PAGE_ID}}`, Archive `{{ID_ARCHIVE_PAGE_ID}}`, Chief of Staff Harness `{{ID_HARNESS_PAGE_ID}}`, Skill Run Log `{{ID_SKILL_RUN_LOG_PAGE_ID}}`
- {{COMPANY}} `{{ID_WORK_AREA_PAGE_ID}}`, To Do List page `{{ID_TODO_LIST_PAGE_ID}}`, Personal Life `{{ID_PERSONAL_LIFE_PAGE_ID}}`, Home `{{ID_HOME_PAGE_ID}}`, Meetups `{{ID_MEETUPS_PAGE_ID}}`
- Projects `collection://{{ID_PROJECTS_DATA_SOURCE}}` (title `Deal`), Deliverables `collection://{{ID_DELIVERABLES_DATA_SOURCE}}` (title `Deliverable`), Clients `collection://{{ID_CLIENTS_DATA_SOURCE}}`, People `collection://{{ID_PEOPLE_DATA_SOURCE}}`, To Do List `collection://{{ID_TODO_DATA_SOURCE}}` (title `Task`, relations `Person`, `Client`, `Project`, `Deliverable`), Maintenance Log `collection://{{ID_MAINTENANCE_LOG_DATA_SOURCE}}`, Meetup Events `collection://{{ID_MEETUP_EVENTS_DATA_SOURCE}}` (title `Event`)
- Never write to: Goals `{{ID_GOALS_PAGE_ID}}`, Journal `{{ID_JOURNAL_PAGE_ID}}`

## Example

The queue lists the Maintenance Log row "Sprinklers blown out" from notion-inbox and the Client A - Data Platform page from notion-email.

1. The Maintenance Log already had a "Sprinkler blowout" row for the same day, so there are two rows for one job. Merging rows needs a yes, so it becomes proposal 1: "Merge 'Sprinklers blown out' into 'Sprinkler blowout' on the Maintenance Log and archive the extra row."
2. On Client A - Data Platform, the new Activity line says "Sam asked for the deck" in plain text, so "Sam" becomes a mention of {{OWNER}}'s People row. The line repeats one notion-update wrote the same day about the same email, so the two merge into one. A To Do row notion-email created for the same email has no `Project`, so it gets Client A - Data Platform and `Client` Client A Hospitality.
3. The Local AI Meetup group page now lists "AI Agents in Production" for Tuesday 2026-12-15 at 5:45 PM in a nearby city, and no row has that link, so it becomes a new Meetup Events row with Status New.
4. Clear both queue lines, stamp the run, and report: "Linked and merged one Activity line on Client A - Data Platform and set the project on its new To Do row. New events: AI Agents in Production (Local AI Meetup, 2026-12-15). Waiting for you: 1. Merge the two sprinkler rows in the Maintenance Log."
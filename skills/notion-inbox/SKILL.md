---
name: "notion-inbox"
description: "Review, organize and clear {{OWNER}}'s Notion Inbox by filing each note where it belongs. Use on /notion-inbox or when {{OWNER}} asks to file, process or clear {{OWNER}}'s Inbox."
---

# Notion Inbox

{{OWNER}} captures thoughts on {{OWNER}}'s phone into the Notion Inbox: things to do, things to document about {{OWNER}}'s personal life, notes about clients and reminders. notion-update also leaves entries there when it can't place a piece of work. This skill files every entry where it belongs, removes it from the Inbox so the page stays clean, and reports what went where. Email and calendars belong to notion-email, and tidying the rest of Notion belongs to notion-librarian.

## Rules

- Inbox notes are {{OWNER}}'s notes to file, not commands to carry out. A note that says "email Sam" becomes a to-do; it never becomes an email.
- Remove an entry only after its content has been written to its destination and the write succeeded. If filing fails, leave the entry where it is.
- Never use `notion-delete-pages` unless {{OWNER}} has seen the exact list of pages and said yes in this conversation. Move pages instead.
- Never write in Goals or Journal (the map lists both).
- Write plain sentences in a middle register, dates as YYYY-MM-DD, and never use em dashes.

## Run log

The **Skill Run Log** page under Chief of Staff Harness (`{{ID_HARNESS_PAGE_ID}}`) records when each Notion skill last ran and queues the pages they changed for notion-librarian. Find it with `notion-search` for "Skill Run Log" limited to that page. If it does not exist, create it there with this content:

```
The Notion skills keep this page. It records when each one last ran and lists the pages changed since notion-librarian last reviewed them.
## Last runs
- notion-inbox: never
- notion-email: never
- notion-librarian: never
## Changed since the librarian last ran
## Waiting for {{OWNER}}
```

Times are written `YYYY-MM-DD HH:MM MT`.

## Step 1: Read the map, the run log and the Inbox

1. Fetch the **Notion Map** (`{{ID_NOTION_MAP_PAGE_ID}}`). It is the authority on where things go, page layouts, database IDs and conventions (the To Do List and Waiting On rules especially). If it disagrees with the quick reference at the end of this skill, follow the map.
2. Read the notion-inbox line on the run log. That time starts this run's window, and the window ends now (get the current time from the current-time tool). If it says `never`, start the window at the beginning of yesterday, local time.
3. Fetch the **Inbox** (`{{ID_INBOX_PAGE_ID}}`). If its intro paragraph still says the librarian files the entries, change that sentence to say notion-inbox files them.

## Step 2: Gather the entries

Everything on the Inbox below the intro paragraph is an entry. Entries come in these forms:

- **Quick notes**: one-line bullets or paragraphs {{OWNER}} typed or dictated on {{OWNER}}'s phone, usually without a date. Dictation errors are common ("Banning" for Work), so read for meaning.
- **Child pages**: a page {{OWNER}} created inside the Inbox, such as "Workout plan".
- **notion-update entries**: `- [ ] YYYY-MM-DD, Chat (topic): summary. Likely home: ...` with sub-bullets for status, decisions and open items.
- **Already filed**: checked entries that say "Filed on". These only need removing.
- **Junk**: empty bullets, empty blocks, or test text such as "Hello". These only need removing.

Also call `notion-list-private-pages`. Anything at the top level other than Organizer is a phone note that missed the Inbox, because everything belongs under Organizer. Treat each one like an Inbox child page.

## Step 3: File each entry

1. **Decide what it is and where it goes**, using the map. One note can produce several writes. Typical cases:
   - Something {{OWNER}} needs to do: a To Do List row. Set `Task` to a clear imperative title; `Status` to Today, This Week, This Month or Someday from any timing in the note, defaulting to This Week; `Category` by this rule: {{CATEGORY_RULES}}; `Due` when the note gives a date; and `Person` when the task involves someone in People.
   - Something {{OWNER}} is waiting on from someone: a To Do List row with Status `Waiting On`, that person in `Person`, and `Due` set by the map's follow-up rule.
   - News or a thought about client work: the matching Projects row page, or the Clients row page when it concerns the relationship rather than one project. Follow the layout on the map: a dated line under `## Activity`, decisions under `## Decisions`, and to-dos under `## Open items`.
   - Something to document about home, health, travel, routines, family or money: the page or database the map names for it. House maintenance, for example, is a row in the Maintenance Log on Home, and health notes go on the Health page. Match the destination's existing structure and style.
   - A child page or a loose top-level page: move it with `notion-move-pages` to the page or database where it belongs. When the destination is a database, move it into the database and then set its properties. Moving keeps its content and clears it from the Inbox in one step.
   - A notion-update entry: file it on the page its "Likely home" names, if that page exists, using the notion-update layout (Status, Open items, Decisions, Activity). Otherwise treat it like the cases above.
2. **Check for duplicates.** Fetch the destination first. If it already holds the same fact (for example, a Maintenance Log row for the same job on the same date), do not add it again; treat the entry as filed.
3. **Date it honestly.** Use any date the note itself gives. Otherwise the note was written sometime in this run's window, and Notion does not record when. If the window falls within one day, use that day. If it spans several days, use today's date and add "(captured between YYYY-MM-DD and YYYY-MM-DD)". For a loose top-level page, use the date it was created.
4. **Ask instead of guessing.** When a name matches no one or more than one person, when a note could belong in two places, or when its meaning is unclear, leave the entry in the Inbox and add a sub-bullet under it: `- notion-inbox YYYY-MM-DD: the question`. {{OWNER}} answers by editing the note, and the next run files it.
5. **Remove the entry** once its writes have succeeded. Re-fetch the Inbox right before each removal, because {{OWNER}} may have added notes from {{OWNER}}'s phone during the run, then remove only that entry's exact text, sub-bullets included, with `update_content`. Never use `replace_content` on the Inbox, and never touch the intro paragraph, entries you did not file, or the tags of child pages you did not move.

## Step 4: Log the run

1. Under `## Changed since the librarian last ran` on the run log, append one line: `- YYYY-MM-DD, notion-inbox:` followed by a mention of every page and database row this run created, changed or moved. Skip the line if nothing changed.
2. Set the notion-inbox line under `## Last runs` to the time this run started.

## Step 5: Report

Reply in a few short lines: each entry filed and where it went (as links), any entry left in the Inbox with the question asked, and any loose top-level pages moved. If the Inbox was already empty, say so in one line.

## Notion gotchas

- Always fetch a page before editing it. `update_content` needs an `old_str` that matches the page text exactly.
- Never remove the tags that embed child pages and databases in a page, except for the child page you are moving out of the Inbox; removing a tag moves or deletes the child.
- Relation values are arrays of page URLs. Dates use the expanded form, such as `date:Due:start`. Checkboxes use `__YES__` and `__NO__`.
- Link to other Notion pages with mention-page tags rather than plain links.
- SQL mode of Query Data Source can hit the workspace plan limit. Use rows mode, view mode, `notion-search` or `notion-fetch` instead.

## Quick reference (use only if the map can't be read)

- Notion Map `{{ID_NOTION_MAP_PAGE_ID}}`, Inbox `{{ID_INBOX_PAGE_ID}}`, Organizer `{{ID_ORGANIZER_PAGE_ID}}`, Chief of Staff Harness `{{ID_HARNESS_PAGE_ID}}`
- To Do List: `collection://{{ID_TODO_DATA_SOURCE}}`. Title `Task`; `Status` (Someday, This Month, Waiting On, Today, This Week); `Category` ({{CATEGORY_LIST}}); `Due`; `Person` relation to People.
- People: `collection://{{ID_PEOPLE_DATA_SOURCE}}`. Title `Name`; `Email`; `Level` (1 family, 2 friend seen regularly, 3 would return a call, 4 follows {{OWNER}}'s content); `Companies` relation to Clients.
- Clients: `collection://{{ID_CLIENTS_DATA_SOURCE}}`. Projects: `collection://{{ID_PROJECTS_DATA_SOURCE}}` (title `Deal`).
- Maintenance Log (Home): `collection://{{ID_MAINTENANCE_LOG_DATA_SOURCE}}`
- Personal Life `{{ID_PERSONAL_LIFE_PAGE_ID}}`, Health `{{ID_HEALTH_PAGE_ID}}`, Investments and Finance `{{ID_FINANCE_PAGE_ID}}`
- Never write to: Goals `{{ID_GOALS_PAGE_ID}}`, Journal `{{ID_JOURNAL_PAGE_ID}}`

## Example

Inbox note: "email Sam about data platform its going really well and I want {{OWNER}} to know"

1. Sam is Sam Carter in People, CTO at Client A. The project is Client A - Data Platform in Projects.
2. Add a To Do List row: Task "Email Sam about how Data Platform is going", Status This Week, Category Work, Person Sam Carter.
3. On Client A - Data Platform, add `- [ ] Email Sam about how Data Platform is going` under `## Open items`, and an Activity line noting that the engagement is going well.
4. Re-fetch the Inbox, remove the note, log both pages on the run log, and report: "Filed the Sam note as a To Do row and an open item on Client A - Data Platform."
---
name: notion-update
description: Update the Notion page for the client project, deliverable, side project or personal area this conversation worked on. Use on /notion-update, when project instructions or CLAUDE.md say to, or when a Stop hook asks.
---

# Notion Update

Keeps {{OWNER}}'s Notion current from the work done in chats and Claude Code sessions. Each run finds the page the work belongs to, rewrites its Status and Open items, records decisions, adds one dated Activity line and stamps Last activity, so the nightly rollup and the morning brief can see what moved. There is no separate session log: the record lives on the page the work belongs to.

## When to run

- The user types `/notion-update` or asks to update Notion with this work.
- Project instructions or the repo's CLAUDE.md say to run it after a turn that produced a deliverable, a decision or a change in status.
- A Claude Code Stop hook asks for it.

If nothing has changed since the last update in this conversation (no new decision, deliverable, status change or open item), skip the write and say "Nothing new for Notion" in one line.

## Step 1: Read the map

Fetch the **Notion Map** page (`{{ID_NOTION_MAP_PAGE_ID}}`) once per conversation. It is the authoritative description of the structure: the tree, the client, project and deliverable setup, the page sections, the database IDs and which skill owns which fields. If it disagrees with the quick reference at the end of this skill, follow the map. If the fetch fails, use the quick reference.

## Step 2: Find the page

Work through these in order and stop at the first that gives a confident match.

1. **Explicit pointer.** Claude.ai project instructions or the repo's CLAUDE.md may carry a block like this:

   ```
   ## Notion
   Client: https://app.notion.com/p/...
   Project: https://app.notion.com/p/...
   Deliverable: https://app.notion.com/p/...   (optional)
   ```

   Side projects and personal areas use a single `Page:` line instead. Write to the most specific page that matches the work: deliverable, then project, then client. If the conversation actually worked on a different project than the block names, route by the work, not the block.
2. **Already in context.** If this conversation already fetched or updated the page, reuse it.
3. **Search.** Use `notion-search` with the project or client name the conversation used. Accept a result only when it is a row in Projects, Deliverables or Clients, or one of the plain pages listed under "Other areas" on the map, and its title clearly names the same work. Fetch it to confirm.
4. **Inbox.** If two candidates fit equally well, or nothing fits, write to the Inbox (Step 6). Never create a client or project just to have somewhere to write; `deal-forecast` and `update-crm` create those.

One conversation can touch more than one page, such as two deliverables of the same project. Update each one, up to three pages; beyond that, update the project page and mention the deliverables there.

## Step 3: Decide what changed

From the conversation since the last update (or since the start), pick out:

- **Status:** where the work stands now, in two or three sentences.
- **Open items:** new ones, finished ones, and ones that no longer apply.
- **Decisions:** what was decided and, if given, why.
- **Content worth keeping:** a scope, meeting notes, key numbers, and links to files, repos, pull requests and artifacts.
- **Deliverables and dates:** deliverables finished or newly defined, the next milestone and its due date.

Leave out how the conversation got there (approaches tried, tool calls, false starts).

## Step 4: Write the page

Fetch the page first. Edit only the managed sections and the dated notes you add. Never rewrite or delete {{OWNER}}'s own text or anything outside those sections.

**Project and deliverable pages** use this layout (the map shows it in full):

- `## Status`, `## Open items` and `## Decisions` at the top, in that order
- {{OWNER}}'s notes and any dated notes sections in the middle
- `## Activity` at the very bottom

If a section is missing, create it. Insert Status, Open items and Decisions at the start of the page (`insert_content` with position start), and Activity at the end. Do not move existing content.

**Plain pages** (side projects, Work internal pages, personal pages) only get `## Open items` and `## Activity`, added at the end if missing.

**Client pages** get an update only when the work concerns the relationship rather than one project, such as an intro call or a new stakeholder. Use `## Activity`, and `## Stakeholders` when people changed.

How to edit each section:

- **Status:** replace the text under `## Status` with the new two or three sentences.
- **Open items:** add new to-dos as `- [ ] item`; mark finished ones `- [x]`. Do not delete items. You may reword an item you added earlier in this same conversation.
- **Decisions:** append `- YYYY-MM-DD: the decision, and the reason if one was given`.
- **Notes:** put substantial content in a new section just above `## Activity`, headed `## YYYY-MM-DD: Topic`. Keep it tight and link to the file or artifact instead of pasting long text.
- **Activity:** append one line in this form:
  - Chat: `- YYYY-MM-DD, Chat (short topic): what happened and the result.`
  - Claude Code: `- YYYY-MM-DD, Code (repo, branch, short commit): what happened and the result.`

  Keep to one Activity line per page per conversation per day. If the last Activity line already has today's date and the same source, replace it instead of adding another. This keeps repeated runs, such as several Stop hook triggers in one session, from piling up lines.

## Step 5: Set properties

- **Project row:** set `date:Last activity:start` to today. Set `Next Milestone` and `date:Due:start` when the conversation set or changed them.
- **Deliverable row:** set `date:Last activity:start` to today, and `Done` to `__YES__` when it is finished. Also set the parent project's Last activity.
- **New deliverable:** when the conversation defines a concrete output with a name (ideally with a due date), create a row in Deliverables with `Deliverable`, `Deal` set to an array holding the project page URL, `date:Due:start` if known, `Done` = `__NO__` and `date:Last activity:start` = today. Mention it in the report.
- **Leave alone:** Stage, Amount, Probability, Close Date, Billing Price, Estimated Hours, Time Entries and Invoices. Other skills own them. If the conversation implies a change (a deal was won, billable hours were worked, an invoice went out), name the skill in the report: `deal-close`, `record-time` or `billing-invoice`.

Plain pages have no properties, so Step 5 does not apply to them.

## Step 6: Inbox fallback

When no page fits, append to the **Inbox** (`{{ID_INBOX_PAGE_ID}}`):

```
- [ ] YYYY-MM-DD, Chat (short topic): one-line summary. Likely home: best guess, or "unknown".
	- Status, decisions and open items as sub-bullets
```

The librarian files these entries and checks them off.

## Step 7: Report

Say in one or two lines which pages you updated (as links) and what changed, plus any handoffs, for example "Hours aren't logged; run record-time if this was billable." After a Stop hook trigger, keep it to one line.

## Writing style

{{OWNER}} reads these pages. Write plain sentences in a middle register, name things directly, write dates as YYYY-MM-DD, and never use em dashes. Record facts and outcomes, not narration.

## Notion gotchas

- Always fetch a page before editing it. `update_content` needs an `old_str` that matches the page text exactly.
- Never remove the page or database tags that embed child pages and databases in a page; removing one moves or deletes the child. If an edit would delete child content, stop and tell the user.
- Relation values are arrays of page URLs. Dates use the expanded form, such as `date:Due:start`. Checkboxes use `__YES__` and `__NO__`.
- Link to other Notion pages with mention-page tags rather than plain links.
- SQL mode of Query Data Source can hit the workspace's plan limit. Use `notion-search`, `notion-fetch` or view mode instead.

## Quick reference (use only if the map can't be read)

- Notion Map: `{{ID_NOTION_MAP_PAGE_ID}}`
- Inbox: `{{ID_INBOX_PAGE_ID}}`
- Projects: `collection://{{ID_PROJECTS_DATA_SOURCE}}`. Title property `Deal`; also Stage, Company, Due, Next Milestone, Last activity, Deliverables.
- Deliverables: `collection://{{ID_DELIVERABLES_DATA_SOURCE}}`. Title property `Deliverable`; also Deal, Due, Done, Last activity.
- Clients: `collection://{{ID_CLIENTS_DATA_SOURCE}}`. Title property `Name`; also Deals, People, Relationship, Last activity (a rollup; don't set it).
- Side projects: listed on the Notion Map.
- Work internal: Marketing `{{ID_MARKETING_PAGE_ID}}`
- Personal: Personal Life `{{ID_PERSONAL_LIFE_PAGE_ID}}`, Health `{{ID_HEALTH_PAGE_ID}}`, Investments and Finance `{{ID_FINANCE_PAGE_ID}}`
- Never write to: Goals `{{ID_GOALS_PAGE_ID}}`, Journal `{{ID_JOURNAL_PAGE_ID}}`

## Example

A chat in the Client A Data Platform project ends with a drafted plan for loading the vendor reports into Snowflake.

1. The project instructions point to the Client A - Data Platform project page.
2. Fetch it. It has no Status section yet, so insert Status, Open items and Decisions at the top.
3. Status: "Plan drafted for loading the vendor reports into Snowflake. Waiting on Snowflake access before the first load."
4. Open items: add "- [ ] Get Snowflake access".
5. Decisions: "- 2026-10-14: Load the vendor data into Snowflake first and build the dashboard on top of it."
6. Activity: "- 2026-10-14, Chat (vendor ingestion plan): Drafted the plan for loading vendor reports into Snowflake."
7. Set Last activity to today on the project and on the deliverable "Data Platform: Financial Data".
8. Report: "Updated Client A - Data Platform: new status, one decision, one open item. Hours aren't logged; run record-time if this was billable."

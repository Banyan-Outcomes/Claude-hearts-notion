---
name: "record-time"
description: "Log billable time entries against a project in {{COMPANY}}'s Notion. Use when {{OWNER}} wants to record time, log hours, add billing entries, approve the time entries notion-eod suggested, or bill meetings or work sessions to a project, such as \"log time\", \"record my hours\" or \"add 2 hours to a project\"."
---

# Record Time

Logs work sessions as **Time Entries** linked to a **Project** in Notion, so hours roll up against the project's estimate and feed invoicing. Each entry is one work session: a date, hours and a note. notion-eod suggests entries each evening but never writes them; this skill writes them once {{OWNER}} approves.

The Projects database's title property and the relation on Time Entries are both named `Deal`.

## Where things are

- **Projects**: `collection://{{ID_PROJECTS_DATA_SOURCE}}` (title `Deal`; `Company`, `Stage`, `Billing Price`, `Billing Basis`, `Estimated Hours`)
- **Time Entries**: `collection://{{ID_TIME_ENTRIES_DATA_SOURCE}}`
- **Invoices**: `collection://{{ID_INVOICES_DATA_SOURCE}}` (another process writes these; this skill never does)

### Time Entries properties

| Property | Type | How to set |
| --- | --- | --- |
| `Notes` | title | Short description of the work and who it was with |
| `Date` | date | `date:Date:start` = `YYYY-MM-DD`, `date:Date:is_datetime` = 0 |
| `Hours` | number | Decimal hours in quarter-hour steps (for example `1.5`) |
| `Deal` | relation to Projects | Array with the project's page ID or URL |
| `Invoice` | relation to Invoices | Leave empty. An empty `Invoice` is what marks the entry as unbilled |

Projects calculate **Logged Hours** (a rollup of entry hours) and **Hours Remaining** (Estimated Hours less Logged Hours). Never set those.

## Steps

1. **Identify the project.** Use `notion-search` with the Projects data source URL as `data_source_url` to find it by name. Projects are titled "Client - Project", so search by either part. If more than one matches, ask. If none exists, offer to create it first (Deal title, Company, Estimated Hours, Billing Price, Stage) before logging.
2. **Gather the entries.** Each needs a date, hours and a note. When {{OWNER}} points at calendar meetings, read them from the calendar connectors to get each event's subject, date, length and attendees. Confirm the hours per entry, because prep time is sometimes folded into a meeting and sometimes billed separately.
3. **Create the entries** in one `notion-create-pages` call with the Time Entries data source as the parent. Set `Notes`, the date, `Hours` and `Deal`. Leave `Invoice` empty.
4. **Report back** in a small table: date, project, hours, notes. Total the hours, compare the project's Logged Hours with its Estimated Hours, and flag any overage with an offer to adjust the estimate. If the project's Stage isn't Won or Invoicing, say so, because only those stages get invoiced.

## Gotchas

- Use date-only values. Calendars often return UTC; convert to {{TIMEZONE}} and store the local date.
- `Hours` must be a number, and `Deal` is an array.
- Write Notes in the style of existing entries ("Kickoff call with Sam Carter", "Data Engine: loader fixes"), and never use em dashes.

## Example

{{OWNER}}: "Bill yesterday's two calls to Client A - Data Platform at 1 hour each, plus 2 hours of build work."

1. Find **Client A - Data Platform** with `notion-search` limited to Projects.
2. Read yesterday's two calls from the calendar for their titles and attendees.
3. One `notion-create-pages` call creates 3 Time Entries (1, 1 and 2 hours), each with `Deal` set to the project.
4. Report: 4 hours logged, the project's Logged Hours against its estimate, and whether it's over.

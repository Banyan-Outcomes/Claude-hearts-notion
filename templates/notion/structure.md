# Notion structure spec

This is the exact structure `/cos-install` builds. The skills depend on these page titles, database names, property names and option values, so keep them as written unless you also change the skills. Names in `[brackets]` come from `config.toml`.

Each line in "Pages" is created as a page under its parent. Each database is created as a full-page database under its parent, with the properties listed, then the views. After creating something, record its ID under the key shown, in `ids.json`.

- Page IDs are the 32-character hex string from the page URL.
- Data source IDs are the UUID inside `collection://...` that `notion-fetch` returns for a database.
- View IDs are the UUID inside `view://...`.

## Pages

| Page | Parent | ids.json key | Body |
| --- | --- | --- | --- |
| Organizer | top level (private) | `ORGANIZER_PAGE_ID` | `dashboard.md`, then the page links (see below) |
| Inbox | Organizer | `INBOX_PAGE_ID` | `inbox.md` |
| Notion Map | Organizer | `NOTION_MAP_PAGE_ID` | `notion-map.md` (written last, once every ID exists) |
| Goals | Organizer | `GOALS_PAGE_ID` | `goals.md` |
| Vision | Goals | `VISION_PAGE_ID` | `vision.md` |
| Archive | Organizer | `ARCHIVE_PAGE_ID` | one line: "Retired pages and databases. Nothing here is deleted." |
| Chief of Staff Harness | Organizer | `HARNESS_PAGE_ID` | `harness.md` |
| Skill Run Log | Chief of Staff Harness | `SKILL_RUN_LOG_PAGE_ID` | `skill-run-log.md` |
| Journal | Organizer | `JOURNAL_PAGE_ID` | one line: "My own writing. Claude never writes here." |
| [company.name] | Organizer | `WORK_AREA_PAGE_ID` | one line: "Clients, projects, people and billing for [company.name]." |
| Marketing | [company.name] | `MARKETING_PAGE_ID` | one line: "Sites, content and talks." |
| Meetups | [company.name] | `MEETUPS_PAGE_ID` | `meetups.md` (optional module) |
| AI News | [company.name] | `AI_NEWS_PAGE_ID` | one line: "One section per day, newest first. Fed by any news routine you run." (optional) |
| To Do List | Organizer | `TODO_LIST_PAGE_ID` | holds the To Do List database |
| Side Projects | Organizer | (none) | one line: "One page per side project." |
| Personal Life | Organizer | `PERSONAL_LIFE_PAGE_ID` | one line: "Health, routines, travel and family." |
| Health | Personal Life | `HEALTH_PAGE_ID` | one line, then the Daily Log database |
| Energy Plan | Health | `ENERGY_PLAN_PAGE_ID` | `energy-plan.md` |
| Investments and Finance | Organizer | `FINANCE_PAGE_ID` | one line: "Accounts, taxes and financial plans." |
| Home | Organizer | `HOME_PAGE_ID` | one line, `## Open items`, then the Maintenance Log database |
| Code | Organizer | (none) | holds the Repositories database (optional module) |

Organizer's page links, below the dashboard, in two columns:

- Left column, heading `## Pages`: Inbox, Notion Map, Goals, Chief of Staff Harness, [company.name], To Do List, Archive, Code, and the Daily Journal database.
- Right column: heading `## Side Projects` with Side Projects, then heading `## Personal` with Personal Life, Journal, Investments and Finance, Home.

## Databases

Types use Notion's names. "Relation → X" means a two-way relation to database X, with the reverse property name in parentheses.

### Clients (under [company.name]) → `CLIENTS_DATA_SOURCE`

| Property | Type | Notes |
| --- | --- | --- |
| Name | title | |
| Website | url | used to match email domains |
| People | relation → People (Companies) | |
| Deals | relation → Projects (Company) | the name is historical; it means projects |
| Invoices | relation → Invoices (Client) | |
| Default Rate | number (dollar) | |
| Next Action Date | date | |
| To Dos | relation → To Do List (Client) | |
| Relationship | select: Client, Prospect, Past client, Lost | |

### Projects (under [company.name]) → `PROJECTS_DATA_SOURCE`

| Property | Type | Notes |
| --- | --- | --- |
| Deal | title | titled "Client - Project" |
| Type | select: Client, Personal, Side project | empty means Client |
| Company | relation → Clients (Deals) | |
| Primary Contact | relation → People | |
| Stage | select: Lead, Qualified, Proposal, Negotiation, Won, Invoicing, Closed, Lost, Planned, Active, Done | the last three are for personal and side projects |
| Amount | number (dollar) | |
| Probability | number (percent) | |
| Close Date | date | |
| Billing Basis | select: Hourly, Per session, Fixed fee | |
| Billing Price | number (dollar) | hourly rate, or the price per session |
| Effective Rate | number (dollar) | what an hour actually earns; ranks billable work |
| Estimated Hours | number | |
| Due | date | |
| Next Milestone | text | |
| Last activity | date | stamped by the skills |
| Deliverables | relation → Deliverables (Deal) | |
| Time Entries | relation → Time Entries (Deal) | |
| Invoices | relation → Invoices (Deal) | |
| To Dos | relation → To Do List (Project) | |
| Logged Hours | rollup: Time Entries → Hours → sum | |
| Hours Remaining | formula: `prop("Estimated Hours") - prop("Logged Hours")` | |

Views: **Spreadsheet** (table, all rows, no filter) → `PROJECTS_SPREADSHEET_VIEW`. Add a board by Stage for yourself if you like.

### Deliverables (under [company.name]) → `DELIVERABLES_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Deliverable | title |
| Deal | relation → Projects (Deliverables) |
| Due | date |
| Done | checkbox |
| Last activity | date |
| To Dos | relation → To Do List (Deliverable) |

### People (under [company.name]) → `PEOPLE_DATA_SOURCE`

| Property | Type | Notes |
| --- | --- | --- |
| Name | title | |
| Email | email | |
| Other Emails | text | comma-separated |
| Phone | phone | |
| LinkedIn | url | |
| Role / Title | text | |
| Companies | relation → Clients (People) | |
| Deals | relation → Projects | |
| Level | select: 1, 2, 3, 4 | 1 family, 2 friend seen regularly, 3 would return a call, 4 follows your content. You set it. |
| Next Action | text | |
| Next Action Date | date | |
| To Dos | relation → To Do List (Person) | |

### To Do List (under To Do List) → `TODO_DATA_SOURCE`

| Property | Type | Notes |
| --- | --- | --- |
| Task | title | |
| Status | select: Today, This Week, This Month, Waiting On, Someday | the horizon |
| Status 1 | status: Not started, In progress, Done | progress |
| Checkbox | checkbox | checked means done; open rows are unchecked |
| Due | date | for Waiting On, the day to follow up |
| Category | select: the values in `[todo].categories` | |
| Person | relation → People (To Dos) | |
| Project | relation → Projects (To Dos) | |
| Client | relation → Clients (To Dos) | |
| Deliverable | relation → Deliverables (To Dos) | |
| Project Stage | rollup: Project → Stage → show original | |
| Billing | formula: `if(contains(format(prop("Project Stage")), "Won") or contains(format(prop("Project Stage")), "Invoicing"), "Billable", if(empty(prop("Project")), "", "Business development"))` | optional tag |

Views: **List** (table, filter Checkbox is unchecked, sort Due ascending) → `TODO_OPEN_LIST_VIEW`. Also useful for you: **Today** (Status is Today), **Waiting On** (Status is Waiting On, grouped by Person), **Follow Up Now** (Status is Waiting On and Due on or before today).

### Time Entries (under [company.name]) → `TIME_ENTRIES_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Notes | title |
| Date | date |
| Hours | number |
| Deal | relation → Projects (Time Entries) |
| Invoice | relation → Invoices (Time Entries) |

Views: **Default** (table, all rows, sort Date descending) → `TIME_ENTRIES_DEFAULT_VIEW`.

### Invoices (under [company.name]) → `INVOICES_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Invoice | title (for example INV-2026-001) |
| Client | relation → Clients (Invoices) |
| Deal | relation → Projects (Invoices) |
| Time Entries | relation → Time Entries (Invoice) |
| Amount | number (dollar) |
| Status | select: Draft, Sent, Paid |
| Sent | date |
| Paid | date |

### Daily Journal (under Organizer) → `DAILY_JOURNAL_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Day | title (YYYY-MM-DD) |
| Date | date |

Views: **Recent** (table, sort Date descending) → `DAILY_JOURNAL_RECENT_VIEW`.

### Daily Log (under Health) → `DAILY_LOG_DATA_SOURCE`

| Property | Type | Notes |
| --- | --- | --- |
| Day | title | "Day N", Day 1 being `[planning].daily_log_start` |
| Date | date | |
| Energy AM | number | 1 to 5, from day-plan |
| Energy PM | number | 1 to 5, from notion-eod |
| Deep work hours | number | estimated by notion-eod |
| Energy notes | text | |
| Weight (lb) | number | optional; add any habits you track |
| Notes | text | |

### Maintenance Log (under Home) → `MAINTENANCE_LOG_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Job | title |
| Date | date |
| Vendor | text |
| Cost | number (dollar) |
| Notes | text |

### Meetup Events (under Meetups, optional) → `MEETUP_EVENTS_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Event | title |
| Date | date (with time) |
| Organization | select: one option per `[meetups].sources` name |
| Location | text |
| Link | url |
| Status | select: New, Interested, Going, Skip |
| First seen | date |
| Notes | text |

Views: **Upcoming** (table, Date on or after today, Status is not Skip, sort Date ascending) → `MEETUPS_UPCOMING_VIEW`.

### Repositories (under Code, optional) → `REPOSITORIES_DATA_SOURCE`

| Property | Type |
| --- | --- |
| Repo | title (owner/name) |
| Owner | text |
| Purpose | text |
| Status | select: Active, Dormant, Archived, Placeholder |
| Client | relation → Clients |
| Project | relation → Projects |
| Production | url |
| Last push | date |
| GitHub | url |

## Skipping a module

If you skip Meetups, AI News, Code, Home or the Daily Log, don't create it, and put `"none"` for its keys in `ids.json`. The skills check what exists and say so in their reports rather than failing.

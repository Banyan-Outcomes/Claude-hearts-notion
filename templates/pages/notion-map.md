This page describes how Organizer is laid out and where each kind of information belongs. The notion-update, notion-inbox, notion-email, notion-github and notion-librarian skills read it before they write, so when the structure changes, this page changes with it.

## The tree

```txt
Organizer
├── Inbox              phone notes and work notion-update could not place; notion-inbox files them
├── Notion Map         this page
├── Goals              mantra, lifelong to weekly goals ({{OWNER}}'s own writing)
│   └── Vision         area plans for the year
├── Daily Journal      database: one row per day: the plan, what {{OWNER}} did, what changed in Notion
├── Chief of Staff Harness
│   │                  goal page for the system itself
│   └── Skill Run Log  when each skill last ran, the librarian's queue, Not to-dos
├── {{COMPANY}}
│   ├── Clients        database: one row per company, clients and prospects
│   ├── Projects       database: one row per project, from first conversation to closed,
│   │                  plus personal and side projects (Type)
│   ├── Deliverables   database: one row per deliverable or milestone
│   ├── People         database: contacts
│   ├── Time Entries, Invoices
│   ├── Marketing
│   ├── Meetups        local events (Meetup Events database), kept current by notion-librarian
│   └── AI News        one section per day
├── To Do List         database: every open to-do and Waiting On item
├── Code               Repositories database: one row per repo
├── Side Projects      one page per side project
├── Personal Life      Health (Energy Plan, Daily Log), routines, travel, family
├── Journal            {{OWNER}}'s own writing
├── Investments and Finance
├── Home               the house; Maintenance Log database; open house issues
└── Archive            retired pages and databases
```

## Client, project, deliverable

Client work lives in three related databases. Every row is a full page, so the details of a client, a project or a deliverable live on that row's own page.

### Client

A company {{COMPANY}} works with or is pursuing. One row in **Clients**.

- **Properties:** Name, Website, People, Deals (its projects), Invoices, Default Rate, Next Action Date, To Dos, Relationship.
- **Page sections:** `## About` (who they are, how the relationship started), `## Stakeholders` (people and roles), `## Activity` (dated lines for relationship events that belong to no single project).

### Project

One piece of work, from the first conversation to closed. One row in **Projects**; its title property is named Deal.

- **Properties:** Deal (title), Type (Client, Personal or Side project; empty means Client), Company, Primary Contact, Stage, Amount, Probability, Close Date, Billing Basis, Billing Price, Effective Rate, Estimated Hours, Due, Next Milestone, Last activity, Deliverables, Time Entries, Invoices, To Dos. Calculated: Logged Hours, Hours Remaining.
- **Stages:** Lead, Qualified, Proposal and Negotiation are the pipeline. Won and Invoicing are current, billable work. Closed and Lost are done. Personal and side projects use Planned, Active and Done.
- **Page sections, top to bottom:**
  - `## Status`: two or three sentences on where the project stands, rewritten on each update
  - `## Open items`: to-dos, checked off when done
  - `## Planned work`: steps for while the project isn't active yet, as plain bullets; they are not To Do rows
  - `## Decisions`: dated bullets, added to and never rewritten
  - {{OWNER}}'s notes, scopes and meeting notes, each under a dated heading such as `## 2026-01-12: Scope`
  - `## Activity`: one dated line per working session, oldest first, never rewritten
- **Naming:** "Client - Project", for example "Client A - Website Rebuild".

### Deliverable

A concrete output or milestone inside a project. One row in **Deliverables**.

- **Properties:** Deliverable (title), Deal, Due, Done, Last activity, To Dos.
- **Page:** what it is and what done looks like, links to files and repos, a `## Planned work` section while it isn't active, and `## Activity`. A deliverable that hasn't started says "Future deliverable" in its first line.

### Person

A contact. One row in **People**.

- **Properties:** Name, Email, Other Emails (comma-separated), Phone, LinkedIn, Role / Title, Companies, Deals, Level (1 family, 2 friend seen regularly, 3 would return a call, 4 follows {{OWNER}}'s content), Next Action, Next Action Date, To Dos.
- **Page:** relationship notes and an `## Activity` section for email and meetings with family, friends and people without a project.

## Other areas

These are plain pages without properties. Updates go into `## Open items` and `## Activity` sections on the page itself.

| Area | Where | Notes |
| --- | --- | --- |
| Side projects | Side Projects | One page each. A side project with a defined outcome is also a row in Projects (Type Side project). |
| Personal | Personal Life, Health, Home, Investments and Finance | Health notes go on Health; energy ratings are rows in the Daily Log; the Energy Plan describes the shape of {{OWNER}}'s day. House maintenance is a row in the Maintenance Log on Home. |
| Harness | Chief of Staff Harness | Work on the system itself. Uses the project layout. |
| Goals | Goals | {{OWNER}}'s own thinking. Only month-plan and week-plan write their sections, after a yes. |
| Journal | Journal | {{OWNER}}'s writing. Claude never writes here. |
| Anything else | Inbox | notion-inbox files and removes entries. |

## Databases

| Database | Data source |
| --- | --- |
| Clients | `collection://{{ID_CLIENTS_DATA_SOURCE}}` |
| Projects | `collection://{{ID_PROJECTS_DATA_SOURCE}}` |
| Deliverables | `collection://{{ID_DELIVERABLES_DATA_SOURCE}}` |
| People | `collection://{{ID_PEOPLE_DATA_SOURCE}}` |
| To Do List | `collection://{{ID_TODO_DATA_SOURCE}}` |
| Time Entries | `collection://{{ID_TIME_ENTRIES_DATA_SOURCE}}` |
| Invoices | `collection://{{ID_INVOICES_DATA_SOURCE}}` |
| Daily Journal | `collection://{{ID_DAILY_JOURNAL_DATA_SOURCE}}` |
| Daily Log | `collection://{{ID_DAILY_LOG_DATA_SOURCE}}` |
| Maintenance Log | `collection://{{ID_MAINTENANCE_LOG_DATA_SOURCE}}` |
| Meetup Events | `collection://{{ID_MEETUP_EVENTS_DATA_SOURCE}}` |
| Repositories | `collection://{{ID_REPOSITORIES_DATA_SOURCE}}` |

## Key pages

| Page | Page ID |
| --- | --- |
| Organizer | `{{ID_ORGANIZER_PAGE_ID}}` |
| Inbox | `{{ID_INBOX_PAGE_ID}}` |
| Goals | `{{ID_GOALS_PAGE_ID}}` |
| Chief of Staff Harness | `{{ID_HARNESS_PAGE_ID}}` |
| Skill Run Log | `{{ID_SKILL_RUN_LOG_PAGE_ID}}` |
| {{COMPANY}} | `{{ID_WORK_AREA_PAGE_ID}}` |
| To Do List | `{{ID_TODO_LIST_PAGE_ID}}` |
| Energy Plan | `{{ID_ENERGY_PLAN_PAGE_ID}}` |
| Archive | `{{ID_ARCHIVE_PAGE_ID}}` |

## Who writes what

| Writer | Owns |
| --- | --- |
| notion-update | Status, Open items, Decisions and Activity on project, deliverable and area pages; Last activity; Next Milestone and Due on projects; Done on deliverables; Inbox entries |
| notion-inbox | Filing Inbox entries and loose top-level pages, then removing them from the Inbox |
| notion-email | Notes from email, calendars and client Slack channels, the To Do rows that come from them, and basic People rows and addresses |
| notion-github | Status, Open items and Code lines from pull requests, Last activity, and the Commit log on the Skill Run Log |
| notion-librarian | Merging duplicates, linking names and relations, page layout, this map, and the Meetup Events list |
| notion-eod | Runs the four filing skills, adds To Do rows for missed to-dos, writes the Daily Journal row, checks off the day's work on the dashboard, and records Energy PM, Deep work hours and Energy notes. Suggests time entries but never writes them |
| record-time | Time Entries, after {{OWNER}} approves |
| day-plan | The Plan section of the day's Daily Journal row, To Do Status, the date, To-dos, Meetings and AI News panels, and Energy AM, after {{OWNER}} approves |
| week-plan | The week's section of Goals, Past plans, the weekly to-do check, and the Goals for this week panel, after {{OWNER}} approves |
| month-plan | The month's section of Goals, Past plans, the monthly to-do review, and the month figures on the dashboard, after {{OWNER}} approves |
| {{OWNER}} | Everything else, especially Goals, Journal and their own notes |

## Conventions

- Dates are written YYYY-MM-DD.
- The top of Organizer is {{OWNER}}'s dashboard: the date and mantra, Goals for this week, To-dos for today, Meetings and AI News today, above the page links. {{OWNER}} arranges the panels; the skills refresh only the content inside them, read check-offs and added lines first, and never touch the page links below.
- Anything {{OWNER}} is waiting on from someone is a To Do row with Status Waiting On, that person in Person, and a Due date: the day to follow up if nothing has arrived, by default about a week after the ask. On its Due date the row moves to Today with its Task starting "Follow up". After following up, it goes back to Waiting On with a new Due date.
- Every To Do row has Task, Status and Category, plus Due and Person when they apply. Checkbox marks a row done. Client to-dos also set Client and Project, and Deliverable when they move one forward.
- **To-dos and planned work.** A To Do row is an action {{OWNER}} has committed to and can start now: it stands alone, or the project and deliverable it serves are active. When something outside {{OWNER}}'s control stands in the way, the blocker is the to-do, as a Waiting On row. Every row has a horizon: Today, This Week, This Month or a due date. Someday holds standalone things to get to eventually and is reviewed each month.
- **Planned work** is the steps a project will take while it isn't active yet: plain bullets under `## Planned work`, never To Do rows. month-plan or week-plan promotes the next steps when the work becomes active.
- Items {{OWNER}} has said are not to-dos are listed under `## Not to-dos` on the Skill Run Log.
- Claude never uses em dashes in what it writes here.
- Move things to Archive rather than deleting them.
- Inbox entries are removed once filed; they are not archived.
- The Daily Journal is notion-eod's and day-plan's record of each day. It is separate from Journal, which stays {{OWNER}}'s own writing.
- Property names that look odd are kept for the skills: the Projects title is Deal, relations to Projects are called Deal or Deals, and the relation from People to Clients is Companies.

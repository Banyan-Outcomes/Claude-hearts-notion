# Customizing

Most changes fall into one of four places. After changing `config.toml` or a template, run `python3 scripts/render.py` and re-upload the skills that changed.

| You want to change | Where | Re-render? |
| --- | --- | --- |
| Your name, emails, time zone, company, default rate | `config.toml` | Yes |
| To Do categories and how they're chosen | `config.toml` `[todo]`, and the Category select options on the To Do List database | Yes |
| Lifelong goals and life areas the planners read | `config.toml` `[planning]`, and the Goals and Vision pages in Notion | Yes |
| GitHub accounts, Slack channels, meetup sources | `config.toml` | Yes |
| How your day is shaped, how Claude talks to you, personal rules | the Energy Plan page in Notion | No |
| Where things are filed, page layouts, conventions | the Notion Map page in Notion | No |
| Things that are never to-dos | the Not to-dos list on the Skill Run Log | No |
| A skill's steps or rules | `skills/<name>/SKILL.md` | Yes |

## Turning modules off

- **No billing.** Leave Time Entries and Invoices in place (the skills expect them) but ignore them. In Goals, don't write a "Bill N hours" line; day-plan and notion-eod then skip the billable pace. Don't upload `record-time`.
- **No GitHub.** Leave `[github]` empty and put `"none"` for `REPOSITORIES_DATA_SOURCE`. notion-github reports that nothing is configured and stops; notion-eod carries on.
- **No Slack.** Leave `[slack].channels` empty.
- **No meetups list.** Leave `[meetups].sources` empty and put `"none"` for the Meetups keys. The librarian skips Step 6.
- **No energy tracking.** Skip the Daily Log and put `"none"` for `DAILY_LOG_DATA_SOURCE`. The planners still read the Energy Plan for the shape of your day; leave the rating questions unanswered.
- **No AI News page.** Put `"none"` for `AI_NEWS_PAGE_ID`; the dashboard panel stays empty.

## Adding a new area

Create the page in Notion where you want it, then tell Claude:

```text
I added a page called "Nonprofit Board" under Personal Life for my board work. Add it to the Notion Map's tree and Other areas table, with Open items and Activity sections.
```

Every skill reads the map, so they start filing there right away.

## Adding a client Slack channel

Add an entry under `[slack].channels` with the channel's name, its ID (open the channel in Slack, then View channel details; the ID is at the bottom), the client name, the project title and the project page's ID. Re-render and re-upload `notion-email`.

## Changing a skill

Edit the template in `skills/<name>/SKILL.md`, not the rendered copy in `dist/`. Keep the placeholders. If you rename a Notion property, change it in `templates/notion/structure.md`, in every skill that mentions it, and in Notion itself.

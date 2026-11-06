# The planning kickoff

Run this once, after the install and after a few days of using /notion-update. It takes three short sittings, ideally on the same day. The answers become the first month plan. Paste each prompt into a Claude chat with Notion, email and calendar connected.

## Sitting 1: the survey (20 to 30 minutes)

```text
We're setting up my planning system. Interview me with the 20 questions below, in batches of four or five so I can answer by voice. Don't plan anything yet; just collect my answers and play back a one-paragraph summary at the end. Save the summary as a dated note on the Chief of Staff Harness page.

1. What do you want to be true by the end of this year? Name two or three things.
2. Rank your areas (for example: client work, a product, health, family, learning, friends) into three groups: top priority, middle, and maintain.
3. What is your monthly revenue or billable-hours target, and your usual hourly rate?
4. Which clients or projects are active now? For each: what's left, any budget or hour cap, and what "done" looks like.
5. Which client or project needs momentum most, and why?
6. Are there prospects you're talking to? Who, and what's the next step with each?
7. Which project do you care about most that nobody is paying you for yet?
8. What are you building for yourself (a product, a body of writing, a skill), and what milestone would make this month a success?
9. Who are the people you want to stay close to this month (family, friends, advisors)?
10. What's your health target for the month (weight, training, sleep, a test)? How do you track it?
11. When in the day are you sharpest? When do you fade? What resets you?
12. What motivates you, and what doesn't work for you (points, streaks, rewards, deadlines)?
13. What's on your plate that has no goal behind it but must get done (taxes, house, car, paperwork)?
14. What has slipped more than twice recently, and what does it cost you?
15. What fixed commitments do you have this month (travel, holidays, recurring meetings)?
16. How many hours a week can you really work? Any days off-limits?
17. What do you want to stop doing or hand off?
18. Is there a personal mantra or sentence you want to read every morning?
19. How do you want me to talk to you when you're behind: blunt numbers, gentle nudges, or something else?
20. Anything else I should know about how you work?
```

## Sitting 2: current state (15 minutes)

```text
Read my Notion (Projects, Deliverables, To Do List, Time Entries), my email and calendars for the last two weeks, and my GitHub activity if connected. Play back the current state: for each active project, the hours logged this month and last, what's open, what's waiting on someone, and what looks stuck. List the to-dos that look stale or that are really planned work for a project that isn't active yet.

Then ask me to correct anything you got wrong: actual hours, contract caps, what's really blocked and why. Save the corrected picture as a dated note on the Chief of Staff Harness page.
```

## Sitting 3: the first plans (20 minutes)

Run `/month-plan`, then `/week-plan`. Each reads the two notes above, proposes a plan, asks a few questions, and saves only after you say yes. Before you start, put your mantra in the green callout at the top of Goals and your lifelong goals under `## Lifelong Goals`.

From the next morning on: `/day-plan` each morning and `/notion-eod` each evening.

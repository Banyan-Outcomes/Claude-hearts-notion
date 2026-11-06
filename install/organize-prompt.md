# Prompt: organize an existing Notion workspace

Use this before installing if you already have a Notion workspace full of notes. Paste it into a Claude chat with the Notion connector on. It only proposes; nothing moves until you approve.

```text
Read my whole Notion workspace and propose a reorganization for a Claude-run "chief of staff" system.

The target shape: one top-level page called Organizer that everything lives under, with a nested tree that matches how I actually work:
- one area for my business (clients, projects, deliverables, people, billing),
- one for side projects (one page each),
- one for personal life (health, home, family, finances),
- plus an Inbox, a Goals page, a Journal for my own writing, and an Archive.

Repeated things (clients, projects, contacts, tasks, time entries) should be databases, not loose pages.

Give me, in this order:
1. The proposed tree, two or three levels deep.
2. A table of every existing top-level page and important subpage: where it would move, and why.
3. Pages that look like duplicates of each other, with which one to keep.
4. Pages that look stale enough to archive.
5. Loose pages that hold lists of clients, projects, contacts or tasks that should become database rows.

Rules: don't move, merge, rename or delete anything until I approve the list. Archive instead of deleting. Never change the text I wrote; only its location. Work in batches of about 20 moves so I can check them.
```

After you approve, ask Claude to carry out the moves in batches, then run `/cos-install`, which builds the remaining structure around what you kept. If you already have Clients, Projects or People databases, tell the installer; it will add the missing properties to them instead of creating new ones.

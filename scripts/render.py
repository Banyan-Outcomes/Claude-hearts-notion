#!/usr/bin/env python3
"""Render the skill and page templates with your config and Notion IDs.

Usage:
  python3 scripts/render.py                 # render into dist/
  python3 scripts/render.py --check         # only report missing values
  python3 scripts/render.py --install-claude-code   # also copy skills to ~/.claude/skills

Inputs:  config.toml (copy of config.example.toml) and ids.json (written by /cos-install).
Outputs: dist/skills/<name>/SKILL.md, dist/skills/<name>.zip (upload these to Claude),
         dist/pages/*.md (page bodies the installer pastes into Notion).
Requires Python 3.11 or newer (for tomllib). No other packages.
"""
import argparse, json, re, shutil, sys, zipfile
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    sys.exit("Python 3.11 or newer is required (tomllib). Check with: python3 --version")

ROOT = Path(__file__).resolve().parent.parent
TOKEN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def load(path, kind):
    if not path.exists():
        sys.exit(f"Missing {path.name}. " + ("Copy config.example.toml to config.toml and fill it in." if kind == "config"
              else "Run /cos-install first, or copy ids.example.json to ids.json and fill it in."))
    return tomllib.loads(path.read_text()) if kind == "config" else json.loads(path.read_text())


def values(cfg, ids):
    o, c, p, t = cfg["owner"], cfg["company"], cfg["planning"], cfg["todo"]
    gh, sl, mu = cfg.get("github", {}), cfg.get("slack", {}), cfg.get("meetups", {})
    v = {
        "OWNER": o["name"],
        "OWNER_EMAILS": ", ".join(o.get("emails", [])) or "(none listed)",
        "TIMEZONE": o["timezone"],
        "COMPANY": c["name"],
        "DEFAULT_RATE": f"${c['default_rate']}",
        "PER_SESSION_RULE": c.get("per_session_rule", "a per-session engagement counts each session at its price"),
        "LIFELONG_GOALS": ", ".join(p["lifelong_goals"]),
        "LIFE_AREAS": ", ".join(p["life_areas"]),
        "DAILY_LOG_START": p["daily_log_start"],
        "NEWS_INTERESTS": p.get("news_interests", "your work"),
        "CATEGORY_LIST": ", ".join(t["categories"]),
        "CATEGORY_RULES": t["category_rules"],
        "GITHUB_LOGIN": f"`{gh['login']}`" if gh.get("login") else "the owner's GitHub login",
    }
    accts = gh.get("accounts", [])
    v["GITHUB_ACCOUNTS"] = ("Read these accounts: " + ", ".join(f"`{a}`" for a in accts) + "."
                           if accts else "No GitHub accounts are configured. Say so in one line and stop.")
    chans = sl.get("channels", [])
    v["SLACK_CHANNEL_ROWS"] = "\n".join(
        f"| {ch['name']} | `{ch['id']}` | {ch['client']} | {ch['project']} `{ch['project_page_id']}` |" for ch in chans
    ) or "| (none configured; skip Slack) | | | |"
    srcs = mu.get("sources", [])
    v["MEETUP_SOURCES"] = "\n".join(f"   - {s['name']}: `{s['url']}`" for s in srcs) or "   - (none configured; skip Step 6)"
    for k, val in ids.items():
        if not k.startswith("_"):
            v["ID_" + k] = val
    return v


def render_text(text, v, missing, where):
    def sub(m):
        key = m.group(1)
        val = v.get(key)
        if val in (None, ""):
            missing.setdefault(key, set()).add(where)
            return m.group(0)
        return str(val)
    return TOKEN.sub(sub, text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--install-claude-code", action="store_true")
    a = ap.parse_args()
    cfg = load(ROOT / "config.toml", "config")
    ids = load(ROOT / "ids.json", "ids")
    v = values(cfg, ids)
    missing, out = {}, {}
    for f in sorted((ROOT / "skills").glob("*/SKILL.md")):
        out[("skills", f.parent.name)] = render_text(f.read_text(), v, missing, f.parent.name)
    for f in sorted((ROOT / "templates" / "pages").glob("*.md")):
        out[("pages", f.name)] = render_text(f.read_text(), v, missing, f.name)
    if missing:
        print("Missing values:")
        for k, w in sorted(missing.items()):
            print(f"  {k:32} used in {', '.join(sorted(w))}")
        print("\nFill these in config.toml or ids.json (use \"none\" for pages you chose not to create).")
        sys.exit(1)
    if a.check:
        print("All placeholders have values.")
        return
    dist = ROOT / "dist"
    shutil.rmtree(dist, ignore_errors=True)
    for (kind, name), text in out.items():
        if kind == "skills":
            d = dist / "skills" / name
            d.mkdir(parents=True, exist_ok=True)
            (d / "SKILL.md").write_text(text)
            with zipfile.ZipFile(dist / "skills" / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
                z.writestr(f"{name}/SKILL.md", text)
        else:
            (dist / "pages").mkdir(parents=True, exist_ok=True)
            (dist / "pages" / name).write_text(text)
    n = sum(1 for k in out if k[0] == "skills")
    print(f"Rendered {n} skills to dist/skills (folders and .zip files) and {len(out) - n} pages to dist/pages.")
    if a.install_claude_code:
        target = Path.home() / ".claude" / "skills"
        for (kind, name), text in out.items():
            if kind == "skills":
                (target / name).mkdir(parents=True, exist_ok=True)
                (target / name / "SKILL.md").write_text(text)
        print(f"Copied {n} skills to {target}")


if __name__ == "__main__":
    main()

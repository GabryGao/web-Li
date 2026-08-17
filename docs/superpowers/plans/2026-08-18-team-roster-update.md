# Team Roster Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish the five owner-supplied Ph.D. student names and only the three verified co-advising relationships on the Team page.

**Architecture:** Keep the existing Jekyll Team template unchanged. Replace the roster records in `_data/team_members.yml`; Liquid continues to omit the advising paragraph when the field is absent.

**Tech Stack:** Jekyll, Liquid, YAML, GitHub Pages

## Global Constraints

- Display only: Chao Teng, Shunfa, Jiahe Chen, Di Xu, Can Shen.
- Do not invent English spellings, surnames, links, dates, photos, research descriptions, or advisors.
- Show `Co-advised with` only for Shunfa, Jiahe Chen, and Di Xu using the exact approved advisor strings.

---

### Task 1: Replace the Ph.D. student roster

**Files:**
- Modify: `_data/team_members.yml`
- Verify: `_site/team/index.html`

**Interfaces:**
- Consumes: Jekyll data collection `site.data.team_members`.
- Produces: Five YAML records with optional `advising` strings for `_pages/team.html`.

- [x] **Step 1: Verify the current rendered roster does not contain all five approved names**

Run:

```bash
rg -n 'Chao Teng|Shunfa|Jiahe Chen|Di Xu|Can Shen' _site/team/index.html
```

Expected: fewer than five distinct approved names are present.

- [x] **Step 2: Replace the data records**

Set `_data/team_members.yml` to the five approved English names in given-name-first order. Add the approved `advising` field to Shunfa, Jiahe Chen, and Di Xu only.

- [x] **Step 3: Build and verify the generated page**

Run:

```bash
BUNDLE_GEMFILE=/private/tmp/web-li-local-Gemfile /Users/fara./.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected: exit code 0.

Then run:

```bash
python3 -c 'from pathlib import Path; import re; html=Path("_site/team/index.html").read_text(); rows=re.findall(r"<li class=\"student-row\">.*?</li>", html, re.S); expected=["Chao Teng","Shunfa","Jiahe Chen","Di Xu","Can Shen"]; assert all(any(name in row for row in rows) for name in expected); assert any("Shunfa" in row and "Zhiwen Pan" in row for row in rows); assert all(any(name in row and "Lansheng Han" in row for row in rows) for name in ["Jiahe Chen","Di Xu"]); assert all(any(name in row and "Co-advised" not in row for row in rows) for name in ["Chao Teng","Can Shen"]); print("team roster verified")'
```

Expected: `team roster verified`.

- [x] **Step 4: Visually inspect the local Team page**

Open the locally built `/team/` page and confirm the five rows use the existing academic roster layout without blank adviser lines.

- [ ] **Step 5: Commit and publish**

```bash
git add _data/team_members.yml docs/superpowers/plans/2026-08-18-team-roster-update.md
git commit -m "content: update PhD student roster"
git push origin main
```

Expected: GitHub Pages deployment succeeds and the public Team page contains all five names.

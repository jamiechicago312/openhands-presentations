---
marp: true
theme: default
paginate: true
header: 'Cursor vs OpenHands'
footer: 'Findings from building the same dashboard with both'
---

<!-- _class: title -->
<!-- _paginate: false -->

# Cursor vs OpenHands
## Building the Same GitHub Stats Dashboard

A hands-on comparison · 2025

---

## How This Comparison Was Done

- **Same goal**: GitHub repo → Next.js dashboard showing public repo stats (e.g. openhands repo)
- **Cursor**: Free plan, chat + IDE, Plan mode then Agent
- **OpenHands**: CLI, same task description + “provide API key when needed”
- **Environment**: Windows (both); GitHub account + phone/VoIP for sign-up

---

## Sign-Up & Setup

- **Sign-up**: Straightforward with GitHub; phone (or VoIP) used to verify human instead of captcha
- **Cursor**: Told it via chat/IDE to set up folder as a GitHub repo for the project
- **OpenHands**: Asked to create git repo in folder + new repo on GitHub and push; succeeded with risk prompts (auto-yes for medium/low; allowed high risk for creating repo)

---

## Cursor: Workflow & Feedback

- Clarifying questions in chat (e.g. CSV vs API vs other data)
- **Plan mode**: Long run (6+ min) searching for “best practices,” minimal updates; needed approval in **tiny font** (then opted into auto search)
- **Feeling**: “Not a lot of feedback… very much feels like I’m just waiting”
- Questions get **queued** during workflow; can override and “send now”
- Unclear if stuck in a loop—not enough visual feedback in chat
- Manually switched from Plan to Agent to start implementing

---

## Cursor: UX Details

- **Enter** = send message · **Shift+Enter** = new line
- Had to **manually accept** each step; no working auto-accept
- Could not auto-generate token; had to **create the repo on GitHub first**, then Cursor could push (no token needed after that)
- Changing project to GitHub Pages (from Vercel): **many approval steps**—“very annoying”
- One error was blamed on “secret not set” before the real fix was applied

---

## Cursor: Build & Cost

- **npm install**: Many deprecation warnings; 4 high severity vulnerabilities
- **localhost**: Worked on first run
- GitHub Pages + cache/“don’t update dashboard” required **three iterations** to clear errors
- **Free limit**: Hit at **$1**—then had uncommitted changes that couldn’t be committed (“probably by design”)

---

## OpenHands: Git & First Run

- Created repo and pushed to GitHub successfully with risk prompts (misclicks on yes/no possible but clickable)
- **Connection**: Lost connection once; paused CLI and restarted
- **npm install**: No critical errors but **not error-free**—EACCES permission errors on Windows (e.g. `.bin` cleanup)
- **First run**: **Could not run locally**; Cursor had run locally on first try

---

## OpenHands: Pivot & Cost

- At **$1.80** decided not to keep debugging—Next.js wouldn’t load locally
- Switched ask: make it **JS + HTML + CSS** hosted on GitHub Pages (same outcome as Cursor)
- **Total cost**: **$3.60** to produce the same dashboard
- **Takeaway**: “Wish OpenHands had done better. Sucks it failed the first try.”

---

## Side-by-Side

| Aspect | Cursor | OpenHands |
|--------|--------|-----------|
| **Cost to same result** | ~$1 (then hit limit) | $3.60 |
| **Run locally first time** | ✅ Yes | ❌ No |
| **Approval burden** | High (many steps) | Risk prompts, can misclick |
| **Feedback while working** | Low (“just waiting”) | — |
| **GitHub integration** | Repo created manually first | Created repo + pushed via CLI |

---

## Cursor: Final Thoughts

- **Verdict**: “Cursor is OK. It requires a lot of tending to.”
- Might have better GitHub integration with primary account
- **Frustration**: Reaching free limit with uncommitted changes (copy/paste only way out)
- **Speed vs cost**: Felt slow; might explain lower cost ($1) vs OpenHands ($3.60)

---

## OpenHands: Final Thoughts

- **Verdict**: “I wish OpenHands had done better.”
- **Pain point**: Failing on first approach (Next.js) then needing a pivot to static HTML/JS/CSS
- **Cost**: $3.60 for same deliverable suggests more iterations and tool use

---

## Summary

- **Cursor**: Cheaper to same outcome, runs locally first time, but heavy on approvals and low on progress feedback; free tier limit leaves uncommitted work stuck.
- **OpenHands**: Smooth git/repo creation and push; first attempt (Next.js) failed locally; pivot to static site worked but cost more.
- **Both**: Sign-up easy; npm/deps had warnings or permission issues on Windows.

---

<!-- _class: center -->

## Questions?

Thanks for following along.

---

<!-- _paginate: false -->
<!-- _class: title -->

# Thank You

Cursor vs OpenHands · Same task, two tools

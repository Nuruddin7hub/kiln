# Ship

## Pre-Ship Checks (Before Deploy, Final Build, or Publish)

- **User Approval Gate**: The user has explicitly approved the latest stills in chat. Never run a production deploy, publish, or costly final export before approval.
- **Production Build Verification**: Run the project's production build and typecheck/lint (`npm run build`, `tsc --noEmit`, etc.) and confirm zero build errors and zero runtime console errors on the built bundle.
- **Interactive & Safety Audit**:
  - Every click, form submit, navigation link, modal, dropdown, and keyboard shortcut works cleanly.
  - No horizontal overflow on desktop (`1440x900`) or mobile (`390x844`).
  - `prefers-reduced-motion: reduce` renders crisp final states immediately; pointer/tilt effects stay disabled on touch/coarse pointers.
- **Measured Metrics Logged**: Record final measured build metrics (bundle build pass, console error count, 4×4 HSV color delta via `scripts/color_check.py`, optional Lighthouse/frame time) cleanly separated from eyeballed critic scores in `kiln/ROUNDS.md`.

## Public Repo Checklist

Only push if `kiln/BRIEF.md` allows pushing. Otherwise prepare everything locally and report that it is ready.

- **`README.md`**: What the site or feature is, a hero screenshot or GIF of the finished build, how to install and run locally, and how to build/deploy.
- **`docs/PROMPT.md`**: The user's real prompt, merged from all their messages in the session and cleaned up—not rewritten. Name the model, its settings, and the number of references used.
- **Credits**: Fonts, icons, React Bits components, libraries, and any external assets.
- **Honest Numbers**: Measured or derived from logs, with estimates explicitly marked as estimates: total rounds, total hours, subagents used (and max in parallel), lines of code changed, and hardware/environment.
- **References — Never Publish Third-Party Screens**: Publish only references the user created or owns. **Never** commit, publish, or name third-party reference screens, sites, or clips (including `inspo` MCP screenshots) in a public repo.
- **Working State (`kiln/`)**: `kiln/` is working state (`kiln/refs/`, `kiln/stills/`, `kiln/compare/`). Add `kiln/refs/` and `kiln/compare/` to `.gitignore`, and never publish third-party references.

## Privacy Scan Before Anything Goes Public

Run this exact scan across the repo (including `README.md` and `docs/PROMPT.md`) for API keys, tokens, `.env` files, private keys, personal paths, emails, and private names:

```bash
git grep -nIE "(sk-[A-Za-z0-9]|api[_-]?key|secret|token|BEGIN [A-Z ]*PRIVATE KEY)"
```

- **Prompts are the riskiest file**: Real user prompts sometimes contain an API key or token pasted in plain text. Remove it immediately and tell the user to rotate it.
- Verify `.gitignore` covers `.env`, `.env.*`, `kiln/refs/`, `kiln/compare/`, build caches, and `node_modules/`.

## Release Note / Post

Publishing or posting is the user's action. If asked, draft a concise announcement summarizing what was built or upgraded, the visual craft & motion stack, and a link to the repository.

# Kiln Ledger: [project name]

Copy this file to `kiln/ROUNDS.md` at the start of every run. Keep the header current. Append one round entry per round, newest at the bottom. Always keep **Measured** numbers separate from **Eyeballed** critic scores.

- **Mode**: `[Option 1: Full Website | Option 2: Feature-Only]`
- **Reference Source**: `[User-Provided | inspo MCP]`
- **Started**: `[YYYY-MM-DD HH:MM, timezone]`
- **Time**: floor `[none / 2h / 8h]` | cap `[none / 1.5h]`
- **Bar**: Layout `[95%]` | Light `[95%]` | Color `[95%]` | Type/Comp `[95%]` | Detail `[95%]` | Motion `[9/10]` | Integration `[95% (Opt 2)]`
- **Calibration offset**: `[none yet]` (from `[user estimate, date]`)
- **Usage**: `[5h window, ~20%/h, never 100%]`
- **Gate**: stills approved `[no]` | final export/ship `[not started]`
- **Best so far**: round `[N]`, `kiln/stills/r[NN]/`, `[commit or snapshot]`

## Decisions

Autonomous decisions made after intake (never ask after intake), one line each:
- `[time]` `[decision]`, because `[reason]`

## User Feedback Inbox

Exact user words. Close an item only when a still or measured check proves it:
- `[time]` `"[exact quote]"` | round `[N]` | `[open / done, proof: path]`

---

## Round [NN]

- **Time**: `[start]` to `[end]` | total elapsed `[h]`
- **Usage**: `[% of window at round end, or "not readable"]`
- **Focus**: `[Option 1: shot & dimension | Option 2: F01 -> F02 -> ... -> FNN sequential pass]`

### Changes Made
*(Option 2: list changes per feature in build order `F01`, `F02`, ...)*
- `F01` / `S01`: [what changed, React Bits added/tuned, files edited]
- `F02` / `S02`: [what changed, React Bits added/tuned, files edited]

### Artifacts
- **Stills**: `kiln/stills/r[NN]/`
- **Side-by-side**: `kiln/compare/r[NN]/`

### Scores — Eyeballed (Calibrated Critic Median)
`[n]` fresh zero-context critics (`[models or "same model"]`):

| Shot / Feature | Layout | Light | Color | Type/Comp | Detail | Motion (/10) | vs Last Round |
|---|---|---|---|---|---|---|---|
| `S01` / `F01` | | | | | | | |
| `S02` / `F02` | | | | | | | |
| `Integration` *(Opt 2)* | | | | | | | |

- **Raw critic medians before calibration**: `[ ]`
- **Own score (logged only, never decides)**: `[ ]`

### Measured (Commands & Objective Checks)
- Interactive smoke test (clicks, forms, nav, scroll): `[pass / fail — details]`
- Console / runtime errors: `[0 / N]`
- React Bits safety (touch/coarse pointer off, `prefers-reduced-motion` verified, zero CLS): `[pass / fail]`
- Color / layout / timing check: `[result or "not measured"]`

### Not Checked This Round
- `[what, and why]`

### Top Gaps From Critics
1. `[shot/feature, exact region, what is wrong, exact fix for next round]`
2. `[ ]`
3. `[ ]`

### Gate & Stop Check
- **Progress note + stills sent**: `[time]`
- **Stop check**: bar `[no]` | safety checks `[no]` | floor `[no]` | stills approved `[no]` | final checked `[no]` -> `[next round / ship / stop at cap]`
- **Next focus**: `[ ]`

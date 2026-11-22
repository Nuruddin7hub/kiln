---
name: kiln
description: Runs the Kiln iterative visual build loop for websites and targeted web features by combining the Cook visual refinement loop, award-winning reference sourcing via the inspo MCP server, and React Bits animated components. Use when building a full website from scratch to match high-craft references or when adding, improving, or redesigning specific features on an existing website with dedicated per-feature references. Trigger when the user types /kiln or $kiln, asks to "fire up kiln", "kiln this site", "cook a website with inspo and react bits", or wants an iterative reference-matched web build or feature-by-feature polish loop.
---

# Kiln

Fire the website—or individual features—until every pixel holds up next to award-winning references.

Kiln unites four disciplines into one autonomous visual loop:
1. **Strict 3-step Intake** — locks Mode (Full Website vs. Feature-Only), Reference Source (User-Provided vs. `inspo` MCP), and Feature Manifest before any code is written.
2. **Award-Winning Reference Sourcing (`inspo` MCP)** — pulls curated real-world references on demand, either for a full site or isolated per feature.
3. **Purposeful Motion & Craft (React Bits)** — layers animated React Bits components from the bundled 217-component catalog across scroll depths under strict safety rules and a disciplined slop ban.
4. **The Iterative Cook Loop** — builds, renders stills, generates side-by-side comparisons (`ref` left, `render` right), scores with zero-context critics, and loops until the numeric bar is met.

## State files

All run state lives in `kiln/` at the project root. These files are your memory across context compactions and agent handoffs.

| Path | Holds |
|---|---|
| `kiln/BRIEF.md` | Mode, reference source, target, numeric bar, rules, time budget, deliverable, permissions. Written once after intake. |
| `kiln/SHOTS.md` | **Option 1**: One fixed viewport/camera shot per full-site reference (`R01`, `R02`, ...). |
| `kiln/FEATURES.md` | **Option 2**: Confirmed feature manifest (`F01`, `F02`, ...), action type (`create` / `improve` / `change`), dedicated reference folder per feature, target files, and viewport shots. |
| `kiln/ROUNDS.md` | The round ledger. Copy `templates/ROUNDS.md` and append one entry per round. |
| `kiln/refs/` | **Option 1**: `R01`, `R02`, ... **Option 2**: Isolated folders `F01/`, `F02/`, `F03/`, ... (one dedicated folder per feature). |
| `kiln/stills/rNN/` | Captured renders for round `NN` (per shot in Option 1; per feature + `integration` in Option 2). |
| `kiln/compare/rNN/` | Side-by-side comparison sheets (reference left, render right) built with `scripts/side-by-side.mjs`. |

## Start or resume

- `kiln/BRIEF.md` exists and the run is not shipped: **resume**. Read `kiln/BRIEF.md`, `kiln/SHOTS.md` (or `kiln/FEATURES.md`), and the last two entries of `kiln/ROUNDS.md`, then continue the next round. Do not re-ask intake questions or rebuild what already works.
- After every context compaction: do the same before your next action.
- `kiln/` holds a shipped run: move it to `kiln-archive/<date>/` and start at Step 1.
- No `kiln/` folder: start at Step 1.

## Step 1: Mandatory Strict Intake (Ask in Order, Before Any Build)

You MUST complete these three intake steps in strict order before writing any application code or fetching references. Full script and defaults: `references/intake-and-modes.md`.

1. **Step A — Mode (Ask FIRST)**: Ask the user to choose:
   - **Option 1**: Build a full website from scratch.
   - **Option 2**: Add a new feature to an existing website, or improve/change an existing feature on the website.
2. **Step B — Reference Source**: Ask the user whether:
   - **User-provided references**: The user supplies their own reference images, screens, or links, OR
   - **Auto-fetched via `inspo` MCP**: The agent fetches the best matching award-winning references itself using the `inspo` MCP tools.
3. **Step C — Option 2 Feature Manifest (Required if Option 2)**:
   - List and confirm with the user **every** feature to be created, improved, or changed on the website (`F01`, `F02`, `F03`, ...), including whether each is `create`, `improve`, or `change`.
   - Do not start the build loop until the user confirms the complete feature list.

Also lock the remaining Cook brief settings (numeric bar, time floor/cap, hard rules, deliverable, permissions) with sensible defaults so the user can reply concisely. Write `kiln/BRIEF.md`, `kiln/FEATURES.md` (Option 2) or `kiln/SHOTS.md` (Option 1), and `kiln/ROUNDS.md`. **Never ask another question after intake is locked**—log autonomous decisions in `kiln/ROUNDS.md` and keep moving.

## Step 2: Reference Acquisition & Target Setup

References are the minimum bar, not loose inspiration. Study every reference at full size before writing code.

- **If Reference Source = Auto-fetched via `inspo` MCP**: Follow `references/inspo-playbook.md` using the exact `inspo` MCP tools and call budget.
- **If Option 1 (Full Website from Scratch)**:
  - Save full-site references into `kiln/refs/R01.*`, `R02.*`, ...
  - Write `kiln/SHOTS.md` with fixed desktop/mobile viewports, scroll positions, and what to take from each reference (layout, typography, palette, spacing, motion).
- **If Option 2 (Feature-by-Feature Isolated References)**:
  - **CRITICAL RULE — Reference Isolation**: For **every** feature in `kiln/FEATURES.md` (`F01`, `F02`, `F03`, ...), you MUST fetch or assign **its own dedicated references** into `kiln/refs/F01/`, `kiln/refs/F02/`, `kiln/refs/F03/`, ...
  - **NEVER** use a single catch-all reference website that tries to cover all features at once. Each feature gets the best-in-class references specifically for *that* feature (e.g., pricing table references for `F01`, interactive calendar/command bar references for `F02`, testimonial wall references for `F03`).
  - Existing site design tokens (colors, fonts, spacing, component conventions) remain authoritative for integration cohesion—adapt each feature's reference craft into the existing site's visual system rather than clashing with it.

## Step 3: Craft, Motion & Rules

- **React Bits Integration**: Pick suitable animated components from the bundled 217-component catalog (`references/react-bits-catalog.md`) and layer them across the build following the placement map, non-negotiable safety rules (function first, touch/reduced-motion off, accessibility, performance, content stays king), and Kiln's slop-ban reconciliation (`references/react-bits-integration.md`).
- **Slop Ban**: No generic eyebrow labels, monospace uppercase filler, random serif pairings, unmotivated purple gradients, beige filler, `01/02/03` decorative counters, generic glowing orbs, shockwave rings, decorative floating particles, long thin decorative divider lines, or em dashes in UI copy.
- **Color & Contrast**: Match reference luminance and saturation—never washed out, muddy, or oversaturated. Keep measured metrics (DOM/CSS checks, 4×4 HSV color delta via `scripts/color_check.py`, Lighthouse/frame time) separate from eyeballed critic scores.

## Step 4: The Kiln Loop

Before Round 1, build the capture harness (fixed viewport presets, automated screenshot capture, side-by-side comparison via `scripts/side-by-side.mjs`, and optional 4×4 HSV color delta via `scripts/color_check.py`). Full loop mechanics, critic prompts, blind pair test, and pacing: `references/loop-and-critics.md`.

### Option 1 Round Flow (Full Website from Scratch)

Inside every round (`r01`, `r02`, ...):
1. **Focus**: Open user feedback first, else lowest-scoring dimension in the weakest shot.
2. **Build / Refine**: Fix in depth, layering suitable React Bits effects and matching reference craft. Split independent sections across parallel subagents when helpful.
3. **Capture Stills**: Render every shot in `kiln/SHOTS.md` at exact reference aspect/viewport into `kiln/stills/rNN/`.
4. **Side-by-Side**: Run `node <skill>/scripts/side-by-side.mjs --out kiln/compare/rNN/all.jpg kiln/refs/R01.png kiln/stills/rNN/R01.png ...`.
5. **Measure & Critique**: Run measurable checks, then spawn **at least 2 fresh zero-context critics** (receiving only the side-by-side images + rubric). Take the median after calibration.
6. **Log & Gate**: Append round entry to `kiln/ROUNDS.md`, send stills + short progress note to the user without pausing, and run the **Stop check**.

### Option 2 Round Flow (Feature-by-Feature Isolated Reference Loop)

Inside every round (`r01`, `r02`, ...), execute in this exact order:
1. **Build / Refine `F01`** against `kiln/refs/F01/` (applying matching React Bits effects + Cook craft rules + existing site design tokens).
2. **Build / Refine `F02`** against `kiln/refs/F02/`.
3. **Continue feature-by-feature** (`F03`, ..., `FNN`) until **ALL** features in `kiln/FEATURES.md` have been built/refined against their own respective dedicated references in this round.
4. **Capture Stills**: Render every feature (`kiln/stills/rNN/F01.png`, `F02.png`, ...) plus an `integration.png` view showing all features living together on the existing site.
5. **Side-by-Side**: Generate per-feature side-by-side comparisons (`F01` ref vs `F01` render, `F02` ref vs `F02` render, ...) using `scripts/side-by-side.mjs`.
6. **Measure & Critique**: Run measurable checks (interactive verification, console errors, color/layout checks) + **at least 2 fresh zero-context critics** scoring each feature against its own reference AND scoring overall site integration cohesion.
7. **Log & Gate**: Log scores, gaps, and decisions in `kiln/ROUNDS.md`, send stills + short note to the user without pausing, run the **Stop check**, and loop to the next round (`r02`, ...) until **every** feature and integration cohesion meet the bar.

## Step 5: Gate, Stop Check & Ship

- **Gate**: Send stills after every round with what changed, scores, and next focus. Do not pause waiting for a reply. **Never** run a final costly export, deployment, or publish step before the user explicitly approves the stills.
- **Stop Check**: Stop only when ALL are true:
  1. Every dimension in every shot (Option 1) or every feature + integration view (Option 2) meets the numeric bar by calibrated critic median.
  2. All interactive safety checks pass (clicks, forms, keyboard nav, reduced motion, zero console errors).
  3. Time floor is met (if a floor was set; capped jobs have no floor).
  4. The user approved the stills and final pre-ship checks + privacy scan (`references/ship.md`) are clean.

## Never

- Skip or reorder the 3-step Strict Intake (Mode -> Reference Source -> Option 2 Feature Manifest).
- Use one catch-all reference website for multiple features in Option 2; every feature MUST have its own dedicated references.
- Build features out of order or skip features within an Option 2 round before critiquing.
- Ask questions after intake is locked.
- Let your own self-score decide a stop; zero-context critic median decides.
- Report a metric you did not measure or a check you did not run.
- Break interactivity, accessibility, or reduced-motion safety with an animation effect.
- Deploy, push, or run final costly exports before user approval.

## Files in this skill

| File | Read when |
|---|---|
| `references/intake-and-modes.md` | Step 1: exact 3-step intake script, Option 1 vs Option 2 rules, defaults, and brief locking. |
| `references/inspo-playbook.md` | Step 2: verified `inspo` MCP tool catalog, call budget, Option 1 full-site hunting, and Option 2 per-feature hunting. |
| `references/react-bits-integration.md` | Step 3: pairing React Bits with Kiln, placement map, non-negotiable safety rules, and slop-ban reconciliation. |
| `references/react-bits-catalog.md` | Step 3: complete 217-component React Bits free index, exact install commands, and website-type presets. |
| `references/loop-and-critics.md` | Steps 4–5: Option 1 & Option 2 round mechanics, zero-context critic prompts, blind pair test, calibration, measurable checks, and Stop check. |
| `references/ship.md` | Step 5: pre-ship checks, public repo checklist, third-party reference rules, and privacy scan. |
| `templates/BRIEF.md` | Copy to `kiln/BRIEF.md` after intake. |
| `templates/FEATURES.md` | Copy to `kiln/FEATURES.md` for Option 2 runs. |
| `templates/ROUNDS.md` | Copy to `kiln/ROUNDS.md` at the start of every run. |
| `scripts/side-by-side.mjs` | Every round: generates `ref` (left) vs `render` (right) comparison sheets. |
| `scripts/color_check.py` | Every round (optional): measures 4×4 HSV saturation and brightness deltas between reference and render. |

# Loop Mechanics, Zero-Context Critics & Stop Check

## Pre-Round 1 Harness

Before Round 1 begins, set up a repeatable capture & measurement harness so every round takes seconds to verify:
1. **Viewport presets**: Fixed desktop (e.g. `1440x900`) and mobile (`390x844`) viewports matching each reference's aspect ratio.
2. **Automated still capture**: Playwright/Puppeteer script (or browser capture) saving PNGs to `kiln/stills/rNN/`.
   - Option 1: `R01.png`, `R02.png`, ...
   - Option 2: `F01.png`, `F02.png`, ..., `FNN.png`, plus `integration.png`.
3. **Side-by-side generator**: Run `scripts/side-by-side.mjs` (requires Node 18+ and `ffmpeg` on `PATH`):
   ```bash
   # Option 1 (full site)
   node <kiln-skill-dir>/scripts/side-by-side.mjs --out kiln/compare/r01/all.jpg \
     kiln/refs/R01.png kiln/stills/r01/R01.png \
     kiln/refs/R02.png kiln/stills/r01/R02.png

   # Option 2 (per-feature isolated comparisons)
   node <kiln-skill-dir>/scripts/side-by-side.mjs --out kiln/compare/r01/features.jpg \
     kiln/refs/F01/F01_ref01.png kiln/stills/r01/F01.png \
     kiln/refs/F02/F02_ref01.png kiln/stills/r01/F02.png
   ```
   Reference is always on the **left**, render on the **right**.
4. **4×4 HSV Color Delta Check (optional, requires Python + Pillow + NumPy)**:
   ```bash
   python <kiln-skill-dir>/scripts/color_check.py kiln/refs/R01.png kiln/stills/r01/R01.png
   ```
   Compares mean saturation and brightness across a 4×4 grid (reference vs render). A negative saturation delta means the render is greyer/more washed out than the reference.

## Option 1 Round Execution (Full Website from Scratch)

1. **Focus**: Open user feedback inbox items first; otherwise target the lowest-scoring dimension in the weakest shot.
2. **Build / Refine**: Implement changes in depth, applying matching React Bits effects (`references/react-bits-catalog.md`, `references/react-bits-integration.md`) and Cook craft rules. Parallelize independent sections across subagents when useful.
3. **Capture Stills**: Render every shot in `kiln/SHOTS.md` into `kiln/stills/rNN/`.
4. **Side-by-Side**: Generate `kiln/compare/rNN/all.jpg`.
5. **Measure**: Run automated checks (console errors = 0, interactive click/form smoke test, `python <kiln-skill-dir>/scripts/color_check.py <ref> <render>` for 4×4 HSV color delta, render/frame timing).
6. **Zero-Context Critics**: Spawn **at least 2 fresh subagents** with zero prior conversation context (see prompt below). Take the **median** per dimension. If critic spread exceeds `10` percentage points (or `1.0` on a 10-point scale), add a 3rd critic and take the median.
7. **Calibrate**: Apply any logged calibration offset from user feedback. Log your own self-score for transparency, but **never** let your own score decide a stop.
8. **Log & Gate**: Append round entry to `kiln/ROUNDS.md`, commit/snapshot the round, update `Best so far`, send stills + short note to the user without pausing, and run the **Stop check**.

## Option 2 Round Execution (Feature-by-Feature Isolated Reference Loop)

Inside **every** round (`r01`, `r02`, ...), strictly follow this sequence:

1. **Feature `F01`**:
   - Open `kiln/refs/F01/` and study `F01`'s dedicated references.
   - Build (r01) or refine (r02+) `F01` against `kiln/refs/F01/`, prioritizing open user feedback for `F01` and its lowest-scoring critic dimensions.
   - Layer suitable React Bits components (`references/react-bits-catalog.md`, `references/react-bits-integration.md`) for `F01` following safety rules and existing site design tokens.
   - Verify `F01` interactions work cleanly.
2. **Feature `F02`**:
   - Open `kiln/refs/F02/` and build/refine `F02` against `F02`'s dedicated references.
3. **Continue through `FNN`**:
   - Repeat feature-by-feature until **ALL** features in `kiln/FEATURES.md` have been built/refined against their own respective dedicated references in this round.
4. **Capture Stills**:
   - Capture dedicated cropped/focused stills for each feature (`kiln/stills/rNN/F01.png`, `F02.png`, ..., `FNN.png`) PLUS `kiln/stills/rNN/integration.png` (showing the full page/app context with all features integrated).
5. **Side-by-Side**:
   - Build `kiln/compare/rNN/features.jpg` pairing each feature's dedicated reference (left) against that feature's render (right).
6. **Measure**:
   - Run automated checks across every feature (zero console errors, all buttons/inputs/toggles/menus functional, touch/reduced-motion CSS verified, zero horizontal overflow).
7. **Zero-Context Critics (Per Feature + Integration)**:
   - Spawn **at least 2 fresh zero-context critics** given ONLY the per-feature side-by-side images, `integration.png`, and the rubric.
   - Each critic scores **every feature (`F01`..`FNN`)** against its own reference AND scores **Integration Cohesion** (do all features look like they belong to the same cohesive website?).
   - Take the median (add a 3rd critic if spread > 10pt / 1.0).
8. **Log & Gate**:
   - Append the round entry to `kiln/ROUNDS.md` (recording every feature's scores + integration score + top gaps).
   - Send stills + short progress note to the user without pausing.
   - Run the **Stop check**. If ANY feature or integration cohesion is below the bar, start the next round (`r02`, `r03`, ...) repeating steps 1–8!

## Scoring Rubric (UI & Web Craft)

Rate every shot (Option 1) or every feature (Option 2) on these 6 dimensions:

| Dimension | What Critics Judge |
|---|---|
| **Layout & Spacing** | Grid alignment, visual hierarchy, whitespace rhythm, proportions vs reference. |
| **Light & Contrast** | Surface elevation, shadows, borders, foreground/background contrast, dark/light balance. |
| **Color** | Palette fidelity, saturation/luminance accuracy (never muddy or oversaturated). |
| **Typography & Components** | Font pairing, scale, weight contrast, component polish, crisp edges, zero slop-ban violations. |
| **Detail Density** | Micro-details, states, icons, empty/hover states, near and far visual richness. |
| **Motion & Interaction** | Purposeful React Bits effects, smooth transitions, zero layout shift, tactile clarity (out of 10). |

*(Option 2 adds **Integration Cohesion**: visual harmony of all features inside the host website.)*

## Zero-Context Critic Prompt Template

Pass ONLY the side-by-side image(s), `integration.png` (Option 2), and this prompt to a fresh subagent:

```text
You are a strict, zero-context visual design critic. You did not build this site.
Each row in the attached image shows the target reference on the LEFT and the current build on the RIGHT.

Score each row harshly and honestly from 0–100% on:
1. Layout & Spacing
2. Light & Contrast
3. Color
4. Typography & Components
5. Detail Density
And 0–10 on:
6. Motion & Interaction cues (visual affordances, polish, perceived craft)
[Option 2 only: Also score Integration Cohesion (0–100%) on the attached integration.png.]

Flag any AI slop (generic purple gradients, glowing orbs, eyebrow filler, 01/02/03 counters, em dashes, cramped or washed-out regions).
List the Top 3 concrete visual gaps per row: [row/feature, exact region, what is wrong, exact fix].
Do not praise; be clinical and specific.
```

## Calibration, Blind Pair Test & Measured vs. Eyeballed Split

- **Models rate themselves too high.** Whenever the user gives a score estimate (e.g. "looks 75% to me" when critics said 88%), log the gap (`-13%`) as the **Calibration offset** in `kiln/ROUNDS.md` and apply it to every subsequent critic median.
- **Blind pair test**: Show a fresh critic the reference and the render **without labels** (randomized left/right order) and ask which one was built in code and why. A confident, correct answer names your exact next focus.
- Keep **Measured** numbers (produced by a command/script: console error count, 4×4 HSV color delta from `scripts/color_check.py`, Lighthouse/timing, DOM test pass/fail) strictly separate from **Eyeballed** numbers (critic scores). If a check was not run, write `"not measured"`.

## Pacing, Gate & Stop Check

- **Gate**: After every round, send the stills + a short note (what changed, calibrated scores, top gaps, next focus). Do not pause waiting for a reply. **Never** run final costly exports, production deploys, or public pushes until the user explicitly approves the stills.
- **Usage Pacing**: For long runs, target ~20% of a 5h quota window per hour (~99% max, never 100%).
- **Stop Check**: Stop only when ALL are true:
  1. Every dimension in every shot (Option 1) or **every feature + integration** (Option 2) meets the numeric bar by calibrated critic median.
  2. All functional & React Bits safety checks pass (measured).
  3. Time floor is met (if a floor was set; capped runs have no floor).
  4. User has approved the stills and final checks + privacy scan (`references/ship.md`) pass.
- If a hard time cap or usage limit is reached first, finish the current round, log it cleanly in `kiln/ROUNDS.md`, and report plainly what is still below the bar.

# Intake & Modes

Kiln runs one strict intake before writing a single line of application code or fetching any references. After intake is confirmed and `kiln/BRIEF.md` is written, **never ask another question**—make decisions autonomously, log them under `Decisions` in `kiln/ROUNDS.md`, and keep iterating.

## Mandatory 3-Step Intake Order

You MUST obtain answers to **Step A**, **Step B**, and (if Option 2) **Step C** in order. If the user's opening prompt already unambiguously answered one of them, echo it back for confirmation and ask the remaining required steps.

### Step A — Mode (Ask FIRST)

Always ask the user to choose the build mode first:

> **1. Mode** — Which mode are we running?
> - **Option 1**: Build a **full website from scratch**.
> - **Option 2**: **Add a new feature** to an existing website, or **improve / change an existing feature** on the website.

### Step B — Reference Source (Ask SECOND)

Always ask where the visual references come from:

> **2. Reference Source** — How should we source references?
> - **User-provided**: You supply your own reference images, screenshots, or links.
> - **Auto-fetched via `inspo` MCP**: I fetch the best matching award-winning references myself using the `inspo` MCP tools.

### Step C — Feature Manifest (Required if Option 2)

If the user chose **Option 2**, you MUST list and confirm **all** features to be created, improved, or changed before starting the loop:

> **3. Feature Manifest (Option 2)** — Please list or confirm every feature we are creating, improving, or changing:
> - `F01`: [Feature name] — `[create / improve / change]` — [brief goal]
> - `F02`: [Feature name] — `[create / improve / change]` — [brief goal]
> - `F03`: ...
>
> Confirm this list is complete (or add/remove items) before I fetch dedicated references for each feature and start Round 1.

If the user gave a vague Option 2 request (e.g. "upgrade the dashboard and add a pricing modal"), inspect the existing codebase first, propose a numbered manifest (`F01`, `F02`, ...) with exact action types (`create` / `improve` / `change`) and target files, and wait for the user to confirm it.

## Optional Run Settings (Ask in the Same Intake Message with Defaults)

Include compact defaults for the remaining Cook brief settings so the user can accept them in one word ("defaults") or override specific numbers:

| # | Setting | Default |
|---|---|---|
| 4 | **Target & Vibe** | Inferred from prompt / existing site (Option 2 preserves existing brand tokens). |
| 5 | **Numeric Bar** | UI stills: **95%+** visual match to refs (stretch **99%** for hero/flagship); Motion/interaction: **9/10** minimum. |
| 6 | **Time Budget** | Option 1 full site: floor **2h** (or user-specified, e.g. 8h overnight). Option 2 feature batch: cap **1.5h** or until all features hit bar. |
| 7 | **React Bits Effects** | Enabled — layer all suitable animated components following safety rules & slop ban. |
| 8 | **Deliverable & Permissions** | Local working app in this repo; no git push, deploy, or external publish without explicit approval. |

## Mode Comparison

| Aspect | Option 1: Full Website from Scratch | Option 2: Feature-Only (Add / Improve / Change) |
|---|---|---|
| **Scope** | Entire site architecture, pages, sections, design system. | Only the confirmed features in `kiln/FEATURES.md` + seamless integration into the existing site. |
| **Manifest File** | `kiln/SHOTS.md` (`R01`, `R02`, ...) | `kiln/FEATURES.md` (`F01`, `F02`, ...) |
| **Reference Structure** | `kiln/refs/R01.png`, `R02.png`, ... | **Strictly isolated per feature**: `kiln/refs/F01/`, `kiln/refs/F02/`, `kiln/refs/F03/`, ... |
| **Catch-All Reference Rule** | Allowed to combine cohesive full-site exemplars. | **FORBIDDEN** — never pick one catch-all reference website for all features. Every feature gets its own best-in-class references. |
| **Existing Design System** | Established fresh from references (`get_design_system` or user refs). | **Existing codebase tokens win** for brand colors/fonts/spacing; feature refs supply layout craft, hierarchy, micro-interactions, and polish. |
| **Per-Round Build Order** | Weakest shot/dimension across the site. | **Sequential feature-by-feature**: `F01` (vs `refs/F01/`) -> `F02` (vs `refs/F02/`) -> ... -> `FNN` (vs `refs/FNN/`) -> capture all + `integration` -> critique all -> next round. |

## Locking the Brief

Once the user confirms Steps A, B, (and C for Option 2):
1. Copy `templates/BRIEF.md` -> `kiln/BRIEF.md` and fill every field.
2. Copy `templates/ROUNDS.md` -> `kiln/ROUNDS.md` and record the exact start timestamp.
3. For Option 2, copy `templates/FEATURES.md` -> `kiln/FEATURES.md` with every confirmed feature (`F01`..`FNN`).
4. Proceed immediately to Step 2 (Reference Acquisition) without asking further questions.

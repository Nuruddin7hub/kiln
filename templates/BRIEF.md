# Kiln Brief: [project name]

Copy this file to `kiln/BRIEF.md` once Intake Steps A, B, (and C for Option 2) are confirmed. Do not ask intake questions again after this file is locked.

## 1. Mode & Reference Source (Locked)

- **Mode**: `[Option 1: Full Website from Scratch | Option 2: Feature-Only (Add / Improve / Change)]`
- **Reference Source**: `[User-Provided | Auto-Fetched via inspo MCP]`
- **Feature Manifest (Option 2 only)**: See `kiln/FEATURES.md` (`[N]` confirmed features: `F01`–`FNN`).

## 2. Target & Aesthetic

- **What we are building**: [One concise sentence describing the site or feature set]
- **Tech stack**: [e.g. React + Vite + Tailwind / Next.js + shadcn]
- **Aesthetic / Vibe**: [e.g. crisp dark editorial / warm minimal SaaS / preserve existing site tokens]
- **Existing Design System (Option 2)**: [Paths to existing theme/CSS variables/component tokens that must remain authoritative]

## 3. Numeric Bar

References are the minimum bar, not loose inspiration.

- **Layout & Spacing**: `[95%+ / 99%]`
- **Light & Contrast**: `[95%+ / 99%]`
- **Color**: `[95%+ / 99%]` (not muddy, not washed out, not oversaturated)
- **Typography & Components**: `[95%+ / 99%]`
- **Detail Density**: `[95%+ / 99%]`
- **Motion & Interaction**: `[9/10 minimum]`
- **Integration Cohesion (Option 2 only)**: `[95%+]`

## 4. Rules & React Bits

- **React Bits Effects**: `[Enabled — layer all suitable components per references/react-bits-integration.md | Disabled]`
- **Safety Rules**: Function first (verify all clicks/forms/scroll), touch/coarse pointer tilt/glow OFF, `prefers-reduced-motion` static fallback, zero CLS, pause hidden canvases.
- **Slop Ban**: No eyebrow labels, monospace uppercase filler, random serif pairings, unmotivated purple gradients, beige filler, `01/02/03` counters, generic glowing orbs, shockwave rings, decorative floating particles, long thin decorative divider lines, or em dashes in UI copy.
- **Option 2 Reference Isolation**: Every feature (`F01`, `F02`, ...) MUST have its own dedicated references in `kiln/refs/FNN/`—never one catch-all reference website.
- **Scope Boundary**: Work only inside this project folder.

## 5. Time & Usage Budget

- **Started**: `[YYYY-MM-DD HH:MM, timezone]`
- **Time floor**: `[e.g. 2h / 8h / none]`
- **Time cap**: `[e.g. 1.5h / none]`
- **Usage pacing**: `[e.g. 5h window, ~20%/h, max ~99%, never 100%]`

## 6. Deliverable & Permissions

- **Deliverable**: `[Working local web app / updated feature components + verified stills]`
- **Gate**: Send stills + short progress note after every round without pausing. Never deploy, push, or run final costly exports before user approves stills.
- **Permissions**: `[Local only | May push/publish after approval]`

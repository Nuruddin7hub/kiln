# Kiln Feature Manifest (Option 2): [project name]

Copy this file to `kiln/FEATURES.md` for **Option 2** runs (adding new features or improving/changing existing features on an existing website).

**CRITICAL RULES**:
1. Every feature listed below MUST have **its own dedicated reference folder** (`kiln/refs/F01/`, `kiln/refs/F02/`, ...). NEVER assign one catch-all reference website to cover multiple features.
2. Inside every round (`r01`, `r02`, ...), build/refine features sequentially (`F01` -> `F02` -> ... -> `FNN`) against their own dedicated references before capturing stills and critiquing.

Confirmed with user: `[YYYY-MM-DD HH:MM]`

## Feature Index

| ID | Feature Name | Action | Target Files / Routes | Dedicated Ref Folder | Inspo Slugs / User Refs | Viewport Shot | Status |
|---|---|---|---|---|---|---|---|
| `F01` | [e.g. Interactive Pricing Matrix] | `[create / improve / change]` | `[src/components/Pricing.tsx]` | `kiln/refs/F01/` | `[slug-a, slug-b / user-ref]` | `[1440x900, #pricing]` | `[pending]` |
| `F02` | [e.g. Quick-Add Event Modal] | `[create / improve / change]` | `[src/components/EventModal.tsx]` | `kiln/refs/F02/` | `[slug-c / user-ref]` | `[1440x900, modal open]` | `[pending]` |
| `F03` | [e.g. Navigation Dock] | `[create / improve / change]` | `[src/components/Nav.tsx]` | `kiln/refs/F03/` | `[slug-d / user-ref]` | `[1440x900, top bar]` | `[pending]` |

## Per-Feature Specifications & Craft Notes

### `F01`: [Feature Name]
- **Action**: `[create / improve / change]`
- **Goal**: [Exact user-visible outcome]
- **Dedicated References (`kiln/refs/F01/`)**:
  - `F01_ref01.png` — [What to take: layout, hierarchy, spacing, component anatomy]
  - `F01_ref02.png` — [What to take: micro-interactions, contrast, detail density]
- **Planned React Bits Effects**: [e.g. `TiltedCard` + `BorderGlow`, `Count Up`, `ScrollReveal`]
- **Integration Constraints**: [Must inherit existing CSS vars / font stack / dark mode tokens]
- **Interactive Checks**: [List exact clicks/inputs/states that must work]

### `F02`: [Feature Name]
- **Action**: `[create / improve / change]`
- **Goal**: [Exact user-visible outcome]
- **Dedicated References (`kiln/refs/F02/`)**:
  - `F02_ref01.png` — [What to take]
- **Planned React Bits Effects**: [e.g. `SplitText`, micro button states]
- **Integration Constraints**: [Must inherit existing theme tokens]
- **Interactive Checks**: [List exact clicks/inputs/states that must work]

## Integration Shot

- **Still path**: `kiln/stills/rNN/integration.png`
- **What it proves**: All features (`F01`..`FNN`) coexist harmoniously inside the host website with consistent palette, spacing, and zero visual clashes.

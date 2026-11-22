# React Bits Integration & Slop-Ban Reconciliation

Kiln pairs reference-matched layout craft with purposeful, high-craft motion from React Bits. All 217 free components, exact install commands, and website-type presets are bundled directly in `references/react-bits-catalog.md`. Read `references/react-bits-catalog.md` whenever you need to pick exact component names, presets, and install commands.

## Core Philosophy

- **No arbitrary 3–5 cap**: Use every React Bits effect that genuinely elevates a section across all scroll depths (hero, headings, cards, galleries, counters, navigation, buttons, forms, scroll reveals).
- **Cohesion beats restraint-for-restraint's-sake**: Visual discipline comes from a unified color palette, consistent motion easing/speed, and a coherent component family—not from leaving the page static.
- **In Option 2 (Feature-Only)**: Apply React Bits effects **inside the target features** (`F01`, `F02`, ...) matching the existing site's mood (Serious / Playful / Premium) without injecting unrequested global page effects outside your scope.

## Placement Map

| Surface / Role | Recommended React Bits Family | Notes |
|---|---|---|
| **Page / Section Background** | 1 quiet ambient base (`pointer-events: none`) | Must never fight foreground contrast or text legibility. |
| **Headings & Display Copy** | `SplitText`, `DepthText`, `Blur Text`, `Gradient Text` | Layerable; preserve accessible text and zero layout shift. |
| **Hero / Primary Showcase Card** | `TiltedCard` + `BorderGlow` inside | Keep tilt subtle (~5–6° default). |
| **Framed Items / Media Cards** | `TiltedCard` | Must never intercept or block click/link handlers. |
| **Card Decks / Stacks** | `CardSwap`, `Shredder` | Ideal for feature tours, testimonials, or showcase decks. |
| **Navigation** | 1 primary: `BranchedMenu`, `Pill Nav`, `Gooey Nav`, `Dock`, `Flowing Menu` | Pick one primary nav pattern; never stack competing animated navs. |
| **Logo / Badge** | `StickerPeel` (top-left or accent badge) | Use where playful/tactile brand tone fits. |
| **Status / Tagline** | `TextType` | Types once and stops—never infinite looping distraction. |
| **Metrics / Stats / Dates** | `Count Up`, `Counter` | Trigger on viewport entry, settle cleanly. |
| **Buttons & Controls** | Micro interaction components everywhere useful | Tactile feedback without delaying click response. |
| **Below-the-Fold Sections** | `ScrollReveal` | Fire **ONCE** and disconnect observer. |

## Installation Rule

- Prefer the official shadcn registry command from `references/react-bits-catalog.md`:
  ```bash
  npx shadcn@latest add @react-bits/<Name>-JS-CSS
  ```
- Install peer dependencies (`motion`, `gsap`, `ogl`, etc.) when required by the chosen component.
- If the project does not use shadcn CLI (e.g., plain Vite/React or custom setup), implement the clean JS/CSS variant directly in the project's component folder with equivalent accessibility and reduced-motion guards.

## Non-Negotiable Safety Rules (Verify Every Round)

1. **Function First**: After adding any React Bits layer, verify every tap, click, checkbox, dropdown, form submit, link, and scroll container. Remove or fix any effect that blocks pointer events or breaks interaction.
2. **Touch & Reduced Motion**:
   - Disable pointer-tracking, tilt, cursor glow, and magnetic hover effects on touch / coarse pointers (`@media (hover: hover) and (pointer: fine)`).
   - Respect `prefers-reduced-motion: reduce` by rendering the crisp final static state immediately.
3. **Accessibility & Zero CLS**: Animated text MUST keep clean screen-reader copy (`aria-label` or reserved-space invisible text) and cause zero cumulative layout shift.
4. **Performance**: Pause WebGL/Canvas background animations when `document.hidden` is true, cap canvas DPR/resolution, and disconnect `IntersectionObserver` after one-shot scroll reveals fire.
5. **Content Stays King**: Never obscure, delay, or dim core content behind decorative effects.

## Reconciling the Cook Slop Ban with React Bits

Cook bans generic AI-template slop, while React Bits adds intentional kinetic craft. Follow this boundary strictly:

| Still BANNED (Cook Slop Ban) | ALLOWED (Disciplined React Bits Craft) |
|---|---|
| Generic purple/indigo gradients slapped onto dark cards by default | Palette-matched subtle gradients or `BorderGlow` pulled directly from the reference or existing brand tokens |
| Random glowing orbs, pulsing blobs, shockwave rings popping out of elements | Quiet, reference-aligned ambient canvas backgrounds (`pointer-events: none`) that support depth without stealing focus |
| Decorative floating particles everywhere | Purposeful micro-interactions (`TiltedCard`, `ScrollReveal`, `Count Up`, `SplitText`) tied to real user actions or content hierarchy |
| Eyebrow labels (`01 // FEATURE`), monospace uppercase filler, `01/02/03` counters, random serif fonts, beige filler, long thin decorative lines, em dashes in UI copy | Clean typographic hierarchy matched to the reference's real type scale and spacing |

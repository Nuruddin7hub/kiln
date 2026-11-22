# Inspo MCP Playbook

Use this playbook whenever the user selects **Auto-fetched via `inspo` MCP** in Intake Step B. All tool names and parameters below are verified against the installed `inspo` MCP server. Never invent tool names or out-of-vocabulary filter values.

## When to Call vs. Respect Existing Conventions

- **Call `inspo` MCP** for new pages, new screens, redesigns, visual reference hunting, and per-feature craft inspiration.
- **Project conventions win over Inspo**: In Option 2 (existing website), do **not** overwrite the project's established brand tokens, color palette, or component library unless the user explicitly asked for a rebrand. Extract layout geometry, hierarchy, spacing rhythm, card anatomy, and interaction polish from Inspo, then render them using the existing site's tokens.
- **Do not call `inspo` MCP** for pure backend logic, copywriting, tests, or infrastructure tasks.

## Verified `inspo` MCP Tool Catalog (15 Tools)

Required parameters are marked with `*`.

| Tool | Parameters | Purpose |
|---|---|---|
| `recommend` | `brief*`, `mode?`, `vibe?`, `color?`, `pageType?`, `macrostructure?`, `device?`, `detail?`, `maxTokens?` | **Start here.** Returns macrostructure pick, 5 exemplars, reference component index, palette, and evidence packet. |
| `search_screens` | `query?`, `style?`, `industry?`, `macrostructure?`, `mode?`, `vibe?`, `color?`, `pageType?`, `paperBand?`, `displayClass?`, `accentHue?`, `device?`, `limit?`, `detail?`, `maxTokens?` | Filtered search across curated award-winning screens. |
| `get_screen` | `slug*` | Full screen record (viewports, palette, fonts, tech stack, credit). |
| `get_design_system` | `slug*`, `live?` | Full `DESIGN.md` (fonts, palette, CSS variables, type ramp). |
| `compare` | `slugs*` | Side-by-side comparison of 2–4 slugs across palette, typography, macrostructure, and scales. |
| `find_by_color` | `hex*`, `tolerance?`, `limit?`, `detail?`, `maxTokens?` | OKLAB color-matched screens (ideal in Option 2 to match an existing brand hex). |
| `find_components` | `type*`, `style?`, `industry?`, `macrostructure?`, `mode?`, `vibe?`, `color?`, `pageType?`, `device?`, `limit?`, `detail?`, `maxTokens?` | Targeted component hunting. Valid `type`: `hero`, `pricing`, `features`, `cta`, `nav`, `footer`, `testimonial`, `logo-cloud`, `faq`, `stat`. |
| `find_examples_for_macrostructure` | `name*`, `device?`, `limit?`, `detail?`, `maxTokens?` | Exemplars for a specific layout macrostructure. |
| `find_reference_components` | `type?`, `macro?` | Index of canonical component archetypes. |
| `get_reference_jsx` | `type*`, `id*` | Copy-pasteable canonical JSX source for an archetype. |
| `find_similar` | `slug*`, `sameSite?`, `limit?`, `detail?`, `maxTokens?` | Visually similar screens (set `sameSite` to inspect sibling pages). |
| `get_site_pages` | `siteSlug?`, `limit?`, `maxTokens?` | Ordered multi-page flow of a single site. |
| `list_collections` | *(none)* | List curated inspiration collections. |
| `get_collection` | `slug*`, `detail?`, `maxTokens?` | Inspect screens inside a named collection. |
| `get_filters` | *(none)* | Zero-input vocabulary lookup. Call first if unsure of valid enum strings—out-of-vocab filter values error. |

## Call Budget Discipline

Keep reference hunting crisp and token-efficient:
- Use `detail: "standard"` by default (`"full"` only when you genuinely need complete autopsies).
- Call `get_filters()` once if you need exact enum values for `style`, `vibe`, `industry`, or `macrostructure`.
- **Per-study budget**: `1 recommend` + `1–2 search_screens` (or `find_components`) + `get_screen` on the **3–5 kept references** = complete study. Avoid firing a 4th exploratory search.

## Workflow A: Option 1 (Full Website from Scratch)

1. Call `recommend(brief="<site purpose + aesthetic>", mode=..., vibe=..., pageType=...)`.
2. Optionally run 1–2 targeted calls (`search_screens` or `find_components`) for hero, navigation, or signature sections.
3. Call `get_screen(slug)` on your top 3–5 finalists and `compare(slugs=[...])` if deciding between 2–4 directions.
4. Call `get_design_system(slug)` on the primary anchor reference to extract type ramp, spacing, and palette tokens.
5. Save reference screenshots/records to `kiln/refs/R01.*`, `R02.*`, ... and document every shot in `kiln/SHOTS.md`.

## Workflow B: Option 2 (Per-Feature Isolated Reference Hunting)

**HARD RULE**: Never fetch one catch-all website reference and reuse it across `F01`, `F02`, `F03`. Each feature gets its own dedicated hunt and its own folder (`kiln/refs/F01/`, `kiln/refs/F02/`, ...).

For **each** feature `FNN` in `kiln/FEATURES.md`:
1. **Pick the tightest tool for `FNN`**:
   - If `FNN` maps to a standard component type (`hero`, `pricing`, `features`, `cta`, `nav`, `footer`, `testimonial`, `logo-cloud`, `faq`, `stat`), start with `find_components(type="<type>", mode=<site-mode>, vibe=<site-vibe>, limit=5)`.
   - If `FNN` is a specialized UI pattern (e.g., calendar view, command palette, sidebar, settings drawer, analytics widget), run `recommend(brief="<specific feature only>", mode=<site-mode>)` or `search_screens(query="<feature keywords>", mode=<site-mode>, limit=5)`.
   - To harmonize with the existing site's brand color, use `find_by_color(hex="<existing-accent-or-bg-hex>")` when helpful.
   - For structural JSX patterns, pair with `find_reference_components(type=...)` -> `get_reference_jsx(type, id)`.
2. **Select 1–3 best-in-class references exclusively for `FNN`** and call `get_screen(slug)` on each kept reference.
3. **Save into `kiln/refs/FNN/`** (`FNN_ref01.png`, `FNN_ref02.png`, plus a short `notes.md` recording slugs, URLs, and the exact traits to adopt).
4. **Update `kiln/FEATURES.md`** with the exact reference paths and slugs for `FNN`.
5. Repeat cleanly for the next feature until **every** feature in `kiln/FEATURES.md` has its own dedicated references.

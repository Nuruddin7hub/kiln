# Kiln

> Fire your website—or individual features—until every pixel holds up next to award-winning references.

**Kiln** is a 100% standalone, agent-agnostic **Agent Skill (`SKILL.md`)** that works with **any AI coding agent** supporting `SKILL.md` / Agent Skills—including **Claude Code, Codex, Cursor, Antigravity, Gemini CLI, Windsurf**, or any custom agent harness. It combines a Cook-style iterative visual refinement loop, award-winning reference sourcing via the `inspo` MCP server, and all **217 free [React Bits](https://reactbits.dev) animated components** into one autonomous build workflow.

## What Kiln Does

1. **Dual-Mode 3-Step Intake**: Locks **Mode** (**Option 1**: Full Website from Scratch vs. **Option 2**: Per-Feature Isolated Reference Loop on an existing site), **Reference Source** (User-Provided vs. Auto-fetched via `inspo` MCP), and **Feature Manifest** (`F01`, `F02`, ...) before any code is written.
2. **Award-Winning Reference Sourcing (`inspo` MCP or User Refs)**: Pulls curated real-world references automatically via `inspo` MCP—or uses your own reference images/URLs. In Option 2, enforces strict **Reference Isolation**: each feature gets its own dedicated reference folder (`kiln/refs/F01/`, `F02/`, ...), never a single catch-all site.
3. **Bundled 217-Component React Bits Catalog**: Includes the complete free React Bits index, exact `shadcn` install commands, website-type presets, placement map, non-negotiable accessibility/reduced-motion safety rules, and slop-ban reconciliation.
4. **Cook Visual Loop & Zero-Context Critics**: Captures fixed-viewport stills, builds side-by-side comparisons (`ref` left, `render` right) with `scripts/side-by-side.mjs`, measures 4×4 HSV color deltas with `scripts/color_check.py`, scores with fresh zero-context critics + blind pair tests, and loops until every dimension meets the numeric bar.

## Installation

### Project-Local (Universal)

Clone into your project's skills folder so the skill travels with the repo:

```bash
# Universal (Codex, Antigravity, Cursor, and other Agent Skills-compatible tools)
git clone https://github.com/Nuruddin7hub/kiln.git .agents/skills/kiln

# Claude Code (project-local)
git clone https://github.com/Nuruddin7hub/kiln.git .claude/skills/kiln

# Cursor (project-local)
git clone https://github.com/Nuruddin7hub/kiln.git .cursor/skills/kiln
```

### Global (Available in Every Project)

Clone into your agent's global skills directory:

| Agent | Global Install Command (macOS / Linux) |
|---|---|
| **Claude Code** | `git clone https://github.com/Nuruddin7hub/kiln.git ~/.claude/skills/kiln` |
| **Codex / Universal** | `git clone https://github.com/Nuruddin7hub/kiln.git ~/.agents/skills/kiln` |
| **Cursor** | `git clone https://github.com/Nuruddin7hub/kiln.git ~/.cursor/skills/kiln` |
| **Antigravity** | `git clone https://github.com/Nuruddin7hub/kiln.git ~/.gemini/antigravity/skills/kiln` |
| **Gemini CLI** | `git clone https://github.com/Nuruddin7hub/kiln.git ~/.gemini/skills/kiln` |

On Windows (PowerShell), replace `~` with `$env:USERPROFILE`, for example:

```powershell
git clone https://github.com/Nuruddin7hub/kiln.git "$env:USERPROFILE\.agents\skills\kiln"
```

### Any Other Agent or Custom Harness

Clone the repo anywhere and point your agent directly at `SKILL.md` (e.g., pass `kiln/SKILL.md` in your system prompt, rules file, or context).

### Triggering Kiln

Invoke the skill with `/kiln`, `$kiln`, or by asking your agent to *"fire up kiln"* or *"kiln this site"*.

## Prerequisites

| Requirement | Needed For |
|---|---|
| **`inspo` MCP server** *(optional)* | Auto-fetching award-winning design references (not required if you supply your own reference images). |
| **Node.js 18+** | Running `scripts/side-by-side.mjs` and installing React Bits via `npx shadcn@latest add`. |
| **`ffmpeg`** (on `PATH`) | Compositing side-by-side reference vs. render comparison sheets (`scripts/side-by-side.mjs`). |
| **Playwright** (or headless browser capture) | Capturing repeatable fixed-viewport desktop & mobile stills each round. |
| **Python 3 + Pillow + NumPy** *(optional)* | Running 4×4 HSV saturation & brightness delta checks (`scripts/color_check.py`). |

## Repository Layout

```text
.
├── SKILL.md                              # Core Kiln workflow & rules
├── references/
│   ├── intake-and-modes.md               # 3-step intake script, Option 1 vs Option 2 rules & defaults
│   ├── inspo-playbook.md                 # inspo MCP tool catalog, call budget & per-feature hunting
│   ├── react-bits-integration.md         # Placement map, safety rules & slop-ban reconciliation
│   ├── react-bits-catalog.md             # Complete 217-component free React Bits index & presets
│   ├── loop-and-critics.md               # Round mechanics, zero-context critics, blind pair test & stop check
│   └── ship.md                           # Pre-ship checks, public repo checklist & privacy scan
├── templates/
│   ├── BRIEF.md                          # Run brief template
│   ├── FEATURES.md                       # Option 2 feature manifest template
│   └── ROUNDS.md                         # Round ledger template
├── scripts/
│   ├── side-by-side.mjs                  # Reference (left) vs. Render (right) sheet generator
│   └── color_check.py                    # 4x4 HSV saturation & brightness delta script
├── LICENSE                               # MIT License
└── README.md
```

## License

[MIT](LICENSE)

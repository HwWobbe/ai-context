---
⌖  RnHw:𝒢:SrEdMicroContentPortability
𝒢  AiContext/ContextLatticeStamp/Docs/SrEd_MicroContentPortability.md
📅 2026-03-17
⟳  draft
→  RnHw:𝒢:MicroContentPortability, RnHw:𝒞:WaysH260317
---

# SrEd: MicroContent Portability
**Date:** 2026-03-17  
**Status:** Resolution achieved — scope defined, build deferred

---

## Uncertainty / Limitation

Full transclusion (TiddlyWiki `{{tiddler}}` style) does not transfer outside TW.  
Attempting to replicate it in `.md`, HTML artifacts, or Claude/OpenFang environments  
requires a transclusion engine that does not exist in those contexts.

**Risk:** DevTime spent building portable transclusion exceeds UseTime benefit.  
**Question:** Is portable transclusion actually necessary, or is the goal achievable differently?

---

## Work Done

- Explored transclusion options across `.md`, HTML, TW, DataDict
- Built RightSidebarTemplate (v1–v7) — generalized H2–H6 drill-down navigation
- Identified that context-sensitivity of content is a *feature*, not a deficiency
- Connected leaf/branch model to existing DataDict lane:category:topic grammar
- Assessed Git branching as the version-divergence mechanism

---

## Assess / Scope / Test

**Assessment:** Full transclusion outside TW is unnecessary.  
The requirement was: same content usable in multiple contexts.  
The simpler model satisfies this: **same leaf on many branches**.

**Scope:**
- Leaf = a registered DataDict note (`RnHw:{Lane}:{Topic}`)
- Branch = the lane + category context in which the leaf appears
- Same content, branch-dependent meaning — natural and correct
- Git handles version divergence when a leaf genuinely differs across branches

**Test:** DataDict already implements this model.  
`RnHw:𝒯:𝕽𝕯Design` and `RnHw:𝒞:𝕮𝕷𝕾Main` are leaves on different branches.  
No transclusion engine needed — the key grammar encodes context.

---

## Resolution — Achieved

**Model adopted:** Same leaf, many branches. Context provided by DataDict key structure.

**Portability stack (pragmatic rule):**

| Need | Tool |
|------|------|
| Wiki power + transclusion | TiddlyWiki |
| Portable structured docs | `.md` + RightSidebarTemplate |
| Machine-readable leaf index | DataDict JSON |
| Version divergence | Git branching |

**Deferred build:** Lightweight `{{key}}` syntax resolving via DataDict lookup.  
Worth revisiting when DataDict reaches century-scale population.

**Design principle added:**  
*Use TW when you want a wiki. Use `.md` when you want portability.  
MicroContent portability is achieved through DataDict key grammar, not transclusion.*

---

## Related artifacts

- `MicroContentPortability.md` — seed idea notes
- `RightSidebarTemplate.html` — branch navigator (h2 = branch, h3+ = leaves)
- `RnhwJsonManager.py` v0.2.3 — leaf registry
- `ContextLatticeStamp/Architecture.md` — lane:category:topic grammar

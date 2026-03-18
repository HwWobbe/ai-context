---
⌖  RnHw:𝒢:MicroContentPortability
𝒢  AiContext/ContextLatticeStamp/Docs/MicroContentPortability.md
📅 2026-03-17
⟳  seed
→  RnHw:𝒢:𝕰𝖘一, RnHw:𝒞:WaysH260317
---

# MicroContent Portability

**Date:** 2026-03-17  
**Status:** Seed idea — expand from usage

---

## Core insight

Full transclusion (TW-style) tries to maintain one canonical copy rendering everywhere.  
A simpler model: **same leaf on many branches**.

The branch (context) provides the meaning. Same content, many interpretations — natural and correct.  
Git handles version divergence when a leaf genuinely needs to differ across contexts.

---

## Why this works

- No transclusion engine needed outside TiddlyWiki
- Context-sensitivity is a feature, not a bug
- `RedisDesign` means something different in the DataDict branch vs the IVI branch
- Git branching + DataDict keys provide traceability without a wiki engine

---

## DataDict as branch index

A registered note (`RnHw:𝒯:𝕽𝕯Design`) is already a leaf.  
The lane + category + topic **is** the branch context.  
Same leaf key, different branch = different meaning — already in the architecture.

---

## Portability stack (pragmatic)

| Environment | Transclusion | Portability |
|-------------|-------------|-------------|
| TiddlyWiki | Full `{{tiddler}}` | TW-only |
| `.md` files | None | Universal |
| HTML artifacts | Manual wiring | Universal |
| DataDict JSON | Key lookup | Machine-readable |

**Rule of thumb:** Use TW when wiki power is needed. Use `.md` + sidebar widget when portability matters.

---

## Future build (deferred)

A lightweight `{{key}}` syntax resolving via DataDict lookup — bridges `.md` portability with TW-style transclusion.  
DevTime/UseTime trade-off: not yet worth the build.

---

## Related

- `ContextLatticeStamp/Architecture.md` — hex addressing, lane/category/topic grammar
- `RightSidebarTemplate.html` — branch navigator pattern (h2 = branch, h3/h4 = leaves)
- `RnhwJsonManager.py` v0.2.3 — DataDict as leaf registry

# Landing Zone Standard
**Date:** 2026-03-17 | **Status:** stable

---

## Format

Every `.md` file in AiContext begins with a landing zone block:

```
---
⌖  RnHw:{Lane}:{Category}{Topic}
𝒢  AiContext/{folder}/{filename}.md
📅 YYYY-MM-DD
⟳  seed | draft | stable | archived
→  RnHw:key1, RnHw:key2
---
```

## Rules

- Always first block in the file, before any prose
- 5 fields, no more
- `⌖` key must match a registered DataDict entry (or be registered on creation)
- `→` related keys are DataDict keys, not free-form text
- Status lifecycle: `seed` → `draft` → `stable` → `archived`

## Example

```
---
⌖  RnHw:𝒢:MicroContentPortability
𝒢  AiContext/ContextLatticeStamp/Docs/MicroContentPortability.md
📅 2026-03-17
⟳  seed
→  RnHw:𝒢:𝕰𝖘一, RnHw:𝒯:𝕽𝕯Design
---
```

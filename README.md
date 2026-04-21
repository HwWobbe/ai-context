# AiContext

> A personal toolkit for working smarter with AI — structured context, dense stamps, and portable session state.
>> currently just a preliminary assessment

---

## What Is This Repo?

AI conversations are stateless. Every new session starts blank.  
**AiContext** is a collection of tools and documents that solve that problem — capturing, compressing, and injecting context so AI picks up exactly where you left off.

The philosophy: **denser is better**. A well-structured JSON stamp beats a wall of prose every time.

---

## Projects

### [`ContextLatticeStamp/`](ContextLatticeStamp/README.md)
The core system. Build versioned JSON stamps of your working context, inject them into any AI chat via hotkey, and maintain continuity across sessions.

| What | Where |
|---|---|
| Docs & guides | `ContextLatticeStamp/Docs/` |
| Scripts (Python + AHK) | `ContextLatticeStamp/Scripts/` |
| Example stamps | `ContextLatticeStamp/Examples/` |
| Design essay | `ContextLatticeStamp/Essay/` |

---

## Repo Conventions

**Naming:** PascalCase for all directories and documents.  
**Private data:** Files prefixed `RnHw_` are personal/local only — never committed. Excluded via `.gitignore`.  
**Versioning:** Long-form drafts use `_vX.Y` suffix (e.g. `DenserIsBetter_v0.1.md`).

See [`ContextLatticeStamp/Docs/FolderStructureGuide.md`](ContextLatticeStamp/Docs/FolderStructureGuide.md) for the full layout and decision rules.

---

## What's Not Here

| Excluded | Reason |
|---|---|
| `RnHw_*.json` | Personal vocabulary & private data dictionaries — local only |
| Session logs | Transient; not versioned |

---

## Status

Active personal project. Structure is stable; tooling and documentation are expanding.

---

*By [HwWobbe](https://github.com/HwWobbe)*

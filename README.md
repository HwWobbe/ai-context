# AiContext

> A personal toolkit for working smarter with AI — structured context, dense stamps, and portable session state..
>> currently just a preliminary assessment that is 
>> ideally: 
>>> based on a wiki Foundation,
>>> AiH augmented,
>>> exploiting unicodeSymbols and nonWord stringPatterns. triggered via TwH( GitCalTwe ).

----

## What Is This Repo?

AI conversations are stateless. Every new session starts blank.  
**AiContext** is a collection of tools and documents that solve that problem — capturing, compressing, and injecting context so AI picks up exactly where you left off.

The philosophy: "**denser is better**". A well-structured JSON stamp beats a wall of prose every time.

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

- also:
  - 2026-05-26: considering EndianNess
  - 2026-05-11: updates & 2026-05-26 ( offline )

---

## What's Not Here

| Excluded | Reason |
|---|---|
| `RnHw_*.json` | Personal vocabulary & private data dictionaries — local only |
| Session logs | Transient; not versioned |

- 2026-06-13: pulseTweaks
- 2026-04-25: Jdate macro V0.0.1
---

## Status

Active personal project. Structure is stable; tooling and documentation are expanding.
- confirm Sync(s) are active and effective
- Minimizing edits on this page reduces disruptions - leading to a "QualityCascade" (but AiContext fixed)

### Plans:
... merge ...

-----

TwH (markdown list):

- 🧩 Context Space
  - Current 🧩
    - TbH
      - Workflow Dispatcher
        - Menus
        - Launch Points
        - Context Switches
        - Resume Points
    - Target 🧩
      - Active Work  ReView
- boxChars FAILed

----

## Background:
About Your AiContext Repo 🙂
Here's what I can see from the webpage, Hans:

Tech Stack Overview
Languages
	* Python — 77.4% (dominant)
	* HTML — 17.1%
	* AutoHotkey (AHK) — 5.5%

Key Files & Their Roles
| File | Purpose |
|---|---|
| `jump_server.py` | A local "JumpH" server |
| `reg_url.py` | URL registration utility |
| `rnhw_json_manager.py` | JSON data management |
| `sync_datadict_to_twh.py` | Data dictionary sync |
| `Register.ahk` | AutoHotkey hotkey triggers |

Infrastructure
	* GitHub Actions — there's a .github/workflows directory with a Python application workflow, so CI is wired up
	* JSON — RnHw_DataDict.json appears to be a core data structure (personal vocabulary/private data)

The Core Concept
The system is built around ContextLatticeStamp — essentially versioned JSON "stamps" that capture AI session state, injected via hotkey (AHK) to restore context across stateless AI conversations.

The philosophy is "denser is better" — compact structured data over verbose prose.

<hr>

*By [HwWobbe](https://github.com/HwWobbe)*

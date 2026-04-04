# -*- coding: utf-8 -*-
"""
RnHw: JSON DataDict Manager v0.2.3
contextLatticeStamp central DataDict (Redis-free, lane-based, exec templates)
HwWvWT260222 | register_from_url added HwWvWT260302
"""
import json
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, unquote

# ── Storage ─────────────────────────────────────────────────────────────────
DATADICT_FILE = Path('RnHw_DataDict.json')

# ── Namespace ───────────────────────────────────────────────────────────────
NS = 'RnHw'

# Lane symbols (site identifiers) - Script font
LANE_CONVO = '𝒞'  # Claude conversations (Script)
LANE_TW    = '𝒯'  # TiddlyWiki
LANE_KEEP  = '𝒦'  # Google Keep
LANE_SQL   = '𝒮'  # SQL Server/database
LANE_FILE  = 'ℱ'  # File system
LANE_GIT   = '𝒢'  # GitHub/repos
LANE_DOCS  = '𝒟'  # Google Docs

LANES = {
    'convo': LANE_CONVO,
    'tw':    LANE_TW,
    'keep':  LANE_KEEP,
    'sql':   LANE_SQL,
    'file':  LANE_FILE,
    'git':   LANE_GIT,
    'docs':  LANE_DOCS,
}

# Category symbols - Fraktur font (reserved for organizational groupings)
# 𝕬 𝕭 𝕮 𝕯 𝕰 𝕱 𝕲 ℌ 𝕴 𝕵 𝕶 𝕷 𝕸 𝕹 𝕺 𝕻 𝕼 𝕽 𝕾 𝕿 𝖀 𝖁 𝖂 𝖃 𝖄 𝖅

# Topic symbols - Blackboard bold (subject domains)
# Can be multi-char like 𝕽𝕯 for Redis, 𝕰𝖘 for Essay, 𝕷𝖆𝖙 for Lattice

def load() -> dict:
    """Load entire DataDict from JSON file."""
    if DATADICT_FILE.exists():
        return json.loads(DATADICT_FILE.read_text(encoding='utf-8'))
    return {}

def save(data: dict):
    """Save entire DataDict to JSON file."""
    DATADICT_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

def key(*parts) -> str:
    """Build namespaced key: RnHw:part1:part2:..."""
    return ':'.join([NS] + list(parts))

# ── Core CRUD ───────────────────────────────────────────────────────────────
def put(domain: str, name: str, data: dict):
    """Store a dict at RnHw:domain:name"""
    dd = load()
    k = key(domain, name)
    dd[k] = data
    save(dd)
    print(f"SET  {k}")

def get(domain: str, name: str) -> dict:
    """Retrieve dict from RnHw:domain:name"""
    dd = load()
    return dd.get(key(domain, name), {})

def drop(domain: str, name: str):
    """Delete RnHw:domain:name"""
    dd = load()
    k = key(domain, name)
    if k in dd:
        del dd[k]
        save(dd)
        print(f"DEL  {k}")

def browse(pattern: str = '*') -> list:
    """Find all keys matching pattern (^F equivalent)"""
    dd = load()
    prefix = key(pattern.rstrip('*'))
    return [k for k in dd.keys() if k.startswith(prefix)]

def rename(domain: str, old: str, new: str):
    """Rename a key (useful for version bumps)"""
    dd = load()
    old_k = key(domain, old)
    new_k = key(domain, new)
    if old_k in dd:
        dd[new_k] = dd.pop(old_k)
        save(dd)
        print(f"REN  {old_k} → {new_k}")

# ── Seed DataDict ───────────────────────────────────────────────────────────
def seed():
    """Populate initial RnHw: DataDict entries."""

    # cls:symbols:temporal
    put('cls:symbols', 'temporal', {
        'year'    : '巳=Snake=2025 indexOrigin0:2020=Rat',
        'month'   : '㋀-㋋ circledKatakana 1-12',
        'week'    : '①-㊿ encircled 1-50',
        'day'     : '㏠-㏾ parenthesized 1-31',
        'weekday' : '☿♀♁♂♃♄♅ planetary Mon-Sun',
        'hour'    : '㍘-㍰ 24hr range 0-24',
        'ampm'    : '㏂㏜ hybrid marker',
    })

    # cls:symbols:rank
    put('cls:symbols', 'rank', {
        'numeric' : '⑴-⒇ parenthesized 1-20',
        'alpha'   : '⒜-⒵ parenthesized a-z',
        'category': '𝕬-𝖅 blackboard bold uppercase',
        'subtype' : '𝖆-𝖟 blackboard bold lowercase',
    })

    # cls:dimensions (QrSt)
    put('cls', 'dimensions', {
        'Q' : 'queue: ordinal position before/after',
        'r' : 'rank: ⑴-⒇ numeric | ⒜-⒵ categorical',
        'S' : 'space: 3x3m resolution PlusCodes',
        't' : 'time: compound temporal lattice',
    })

    # identity
    put('cls', 'identity', {
        'full'    : 'Hans-Werner Wobbe',
        'HwW'     : 'progressiveTyping short form',
        'HwWvW'   : 'Twitter unique tag',
        'H'       : 'terminating personal significance marker',
        'T260222' : 'timestamp YYMMDD = Feb 22 2026',
    })

    # tools
    put('tools', 'textblaze', {
        'status'     : 'testing',
        'desktop'    : 'active',
        'iOS'        : 'outstanding - monitor for support',
        'workaround' : 'iOS dictation for prose, manual for stamps',
        'purpose'    : 'progressive entry for non-touch-typists',
    })

    put('tools', 'remarkable', {
        'status'  : 'active',
        'PDF'     : 'preferred - adequate support',
        'sketch'  : 'active - collapse/expand pinch effective',
        'role'    : 'review/annotation/freeform/lattice sketching',
        'sync'    : 'PDF pipeline to TW/GitHub',
    })

    put('tools', 'tiddlywiki', {
        'status'  : 'active - primary laboratory',
        'role'    : 'canonical knowledge base',
        'context' : '🐟 file marker in stamps',
        'level'   : 'advanced power-user',
    })

    put('tools', 'json', {
        'status'  : 'active',
        'role'    : 'DataDict backend (Redis-free)',
        'file'    : 'RnHw_DataDict.json',
        'version' : 'v0.2.3T260302',
    })

    # channels
    put('cls', 'channels', {
        'TW' : 'TiddlyWiki canonical source',
        'GH' : 'GitHub version control',
        'SS' : 'Substack public facing SubStackT0217',
        'DG' : 'DebateGraph argumentation',
        'JS' : 'JSON DataDict (local)',
        'TB' : 'TextBlaze snippet entry',
        'RM' : 'reMarkable PDF/sketch',
    })

    # versions
    put('cls', 'versions', {
        'v0.1'   : 'SubStackT0217 first expansive draft',
        'v0.2'   : 'lane-based refactor',
        'v0.2.1' : 'Redis-as-DataDict section',
        'v0.2.2' : 'exec templates for jumpTo and batch ops',
        'v0.2.3' : 'register_from_url — URL-first registration',
        'v0.3'   : 'community contributions',
    })

    # exec templates
    put('exec', 'jump_tw', {
        'cmd'    : 'webbrowser.open("http://localhost:8080/#{tiddler}")',
        'params' : ['tiddler'],
        'desc'   : 'Jump to TiddlyWiki tiddler by name',
    })

    put('exec', 'jump_note', {
        'cmd'    : 'webbrowser.open(jump_note("{lane}", "{key}"))',
        'params' : ['lane', 'key'],
        'desc'   : 'Jump to any note via DataDict lookup',
    })

    put('exec', 'register_tw_batch', {
        'code'   : '''for t in tiddlers:
    topic = t.get("topic", "noTopic")
    register_note("tw", topic, t["url"], t["title"])''',
        'params' : ['tiddlers'],
        'desc'   : 'Batch register TiddlyWiki tiddlers',
    })

# ── Note key generator ──────────────────────────────────────────────────────
CJK_BASE = 0x4E00  # Unicode CJK Unified Ideographs start

def next_note_key(lane: str, category: str) -> str:
    """
    Generate next available note key for given lane + category.
    Scans existing RnHw:lane:category* keys, finds first free slot
    in Unicode range 4E00+ (CJK ideographs).
    """
    lane_sym = LANES.get(lane, lane)
    dd = load()
    pattern = key(lane_sym, category)

    used = set()
    prefix_len = len(pattern)
    for k in dd.keys():
        if k.startswith(pattern) and len(k) > prefix_len + 1:
            parts = k.split(':')
            if len(parts) >= 4:
                displacement = parts[-1]
                if len(displacement) == 1:
                    used.add(ord(displacement))

    slot = CJK_BASE
    while slot in used:
        slot += 1

    return category + chr(slot)

def register_note(lane: str, category: str, url: str, title: str = '',
                  related: str = '', manual_key: str = None) -> str:
    """
    Register a note in any lane (convo, tw, keep, sql, etc.).
    """
    lane_sym = LANES.get(lane, lane)

    if manual_key:
        # Guard: strip RnHw:lane_sym: prefix if caller already included it
        full_prefix = f"{NS}:{lane_sym}:"
        if manual_key.startswith(full_prefix):
            manual_key = manual_key[len(full_prefix):]
        note_key = manual_key
    else:
        note_key = next_note_key(lane, category)

    data = {'url': url}
    if title:
        data['title'] = title
    if related:
        data['related'] = related

    put(lane_sym, note_key, data)
    return note_key

def jump_note(lane: str, note_key: str) -> str:
    """Retrieve note URL for jumping."""
    lane_sym = LANES.get(lane, lane)
    data = get(lane_sym, note_key)
    return data.get('url')

def find_notes(lane: str = None, prefix: str = '') -> list:
    """
    Find all notes matching lane + prefix.
    Excludes system keys (cls, tools, exec).
    """
    dd = load()
    matches = []
    SYSTEM_DOMAINS = {'cls', 'tools', 'exec', 'cls:symbols'}

    if lane:
        lane_sym = LANES.get(lane, lane)
        pattern = key(lane_sym, prefix) if prefix else key(lane_sym, '')
    else:
        pattern = key(prefix) if prefix else None

    for k, v in dd.items():
        parts = k.split(':')
        if len(parts) < 3:
            continue
        domain = parts[1]
        # Skip system domains
        if domain in SYSTEM_DOMAINS:
            continue
        # Skip non-lane keys when no lane filter
        if not any(domain == sym for sym in LANES.values()):
            continue
        if pattern and not k.startswith(pattern):
            continue

        note_lane = domain
        note_key  = ':'.join(parts[2:])
        lane_name = {v: k for k, v in LANES.items()}.get(note_lane, note_lane)

        matches.append({
            'lane'    : lane_name,
            'lane_sym': note_lane,
            'key'     : note_key,
            'title'   : v.get('title', ''),
            'url'     : v.get('url', '')
        })

    return sorted(matches, key=lambda x: (x['lane'], x['key']))

def list_notes(lane: str = None):
    """List all registered notes with details."""
    notes = find_notes(lane=lane)
    if not notes:
        print("No notes registered yet.")
        return

    lane_str = f" in {lane}" if lane else ""
    print(f"\n── Registered Notes{lane_str} ({len(notes)} found)")

    current_lane = None
    for n in notes:
        if n['lane'] != current_lane:
            current_lane = n['lane']
            print(f"\n[{n['lane_sym']} {n['lane']}]")
        title_str = f" - {n['title']}" if n['title'] else ""
        print(f"  {n['key']}{title_str}")
        print(f"    {n['url']}")
    return notes

# ── URL-first registration ───────────────────────────────────────────────────
URL_LANE_PATTERNS = [
    ('localhost:8080',   'tw'),
    ('claude.ai',        'convo'),
    ('github.com',       'git'),
    ('docs.google.com',  'docs'),
    ('keep.google.com',  'keep'),
]

def _detect_lane(url: str) -> str:
    """Infer lane from URL pattern. Returns lane string or 'file' as fallback."""
    for pattern, lane in URL_LANE_PATTERNS:
        if pattern in url:
            return lane
    if url.startswith('file:///') or url.startswith('C:\\') or url.startswith('/'):
        return 'file'
    return 'file'

def _extract_title(url: str, lane: str) -> str:
    """Best-effort title extraction from URL."""
    parsed = urlparse(url)

    if lane == 'tw':
        fragment = unquote(parsed.fragment)
        return fragment if fragment else parsed.path.rstrip('/').split('/')[-1]

    if lane == 'convo':
        parts = [p for p in parsed.path.split('/') if p]
        return parts[-1] if parts else 'conversation'

    if lane == 'git':
        parts = [p for p in parsed.path.split('/') if p]
        if len(parts) >= 2:
            return '/'.join(parts[:2])
        return parts[0] if parts else 'repo'

    if lane == 'docs':
        parts = [p for p in parsed.path.split('/') if p]
        if 'd' in parts:
            idx = parts.index('d')
            if idx + 1 < len(parts):
                return parts[idx + 1]
        return parts[-1] if parts else 'doc'

    parts = [p for p in parsed.path.split('/') if p]
    return unquote(parts[-1]) if parts else parsed.netloc

def register_from_url(url: str, category: str = '', title: str = '',
                      lane: str = '', manual_key: str = '') -> str:
    """
    Register a note from a URL with minimal arguments.
    Lane and title are auto-detected if not provided.

    Args:
      url:        Full URL or file path — required
      category:   Fraktur symbol e.g. '𝕯' — optional
      title:      Human label — optional, auto-extracted if omitted
      lane:       Override auto-detect ('tw','convo','git','keep','docs','file')
      manual_key: Override auto-generated key

    Returns: registered key string

    Examples:
      register_from_url('http://localhost:8080/#TagVocabulary')
      register_from_url('https://claude.ai/chat/abc123', title='Redis session')
      register_from_url('https://github.com/HwWobbe/AiContext', category='𝕰𝖘')
    """
    detected_lane  = lane  or _detect_lane(url)
    detected_title = title or _extract_title(url, detected_lane)

    key_used = register_note(
        lane       = detected_lane,
        category   = category,
        url        = url,
        title      = detected_title,
        manual_key = manual_key or None,
    )

    print(f"REG  {key_used}  [{detected_lane}]  {detected_title}")
    return key_used

# ── Executable templates ────────────────────────────────────────────────────
def exec_template(template_key: str, **kwargs) -> any:
    """Execute a stored template with parameter substitution."""
    import webbrowser

    template = get('exec', template_key)
    if not template:
        raise ValueError(f"Template not found: exec:{template_key}")

    if 'cmd' in template:
        cmd = template['cmd']
        for k, v in kwargs.items():
            cmd = cmd.replace(f'{{{k}}}', str(v))
        return eval(cmd)

    elif 'code' in template:
        code = template['code']
        local_vars = kwargs.copy()
        local_vars['register_note'] = register_note
        local_vars['jump_note'] = jump_note
        exec(code, globals(), local_vars)
        return local_vars.get('result')

    else:
        raise ValueError(f"Template missing 'cmd' or 'code': {template_key}")

# ── Display helpers ─────────────────────────────────────────────────────────
def show(domain: str, name: str):
    """Pretty-print a single DataDict entry."""
    k = key(domain, name)
    data = get(domain, name)
    if not data:
        print(f"  (empty) {k}")
        return
    print(f"\n── {k}")
    for f, v in data.items():
        print(f"  {f:<12} {v}")

def ls(pattern: str = '*'):
    """List all matching keys."""
    keys = sorted(browse(pattern))
    print(f"\n── KEYS RnHw:{pattern} ({len(keys)} found)")
    for k in keys:
        print(f"  {k}")
    return keys

# ── Stamp generator ─────────────────────────────────────────────────────────
ZODIAC = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
MONTHS   = list('㋀㋁㋂㋃㋄㋅㋆㋇㋈㋉㋊㋋')
WEEKDAYS = list('☿♀♁♂♃♄♅')
HOURS    = list('㍘㍙㍚㍛㍜㍝㍞㍟㍠㍡㍢㍣㍤㍥㍦㍧㍨㍩㍪㍫㍬㍭㍮㍯㍰')
ENCIRCLED = (
    list('①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳') +
    list('㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿')
)
DAYS = list('㏠㏡㏢㏣㏤㏥㏦㏧㏨㏩㏪㏫㏬㏭㏮㏯㏰㏱㏲㏳㏴㏵㏶㏷㏸㏹㏺㏻㏼㏽㏾')

def stamp(dt: datetime = None, context: str = '🐟') -> str:
    """Generate a contextLatticeStamp for a given datetime."""
    dt = dt or datetime.now()
    yr  = ZODIAC[(dt.year - 2020) % 12]
    mo  = MONTHS[dt.month - 1]
    wk  = ENCIRCLED[dt.isocalendar()[1] - 1]
    dy  = DAYS[dt.day - 1]
    wd  = WEEKDAYS[dt.weekday()]
    apm = '㏂' if dt.hour < 12 else '㏜'
    hr  = HOURS[dt.hour]
    return f'ℌ{context}{yr}{mo}{wk}{dy}{wd}{apm}{hr}'

# ── Main ────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("RnHw: JSON DataDict Manager v0.2.3")
    print(f"File: {DATADICT_FILE.absolute()}")
    print(f"stamp(now) = {stamp()}\n")

    seed()
    ls()

    show('cls:symbols', 'temporal')
    show('cls', 'dimensions')
    show('tools', 'textblaze')
    show('cls', 'versions')
    show('exec', 'jump_tw')

    print("\n── Lane-based Note Registration Demo")

    key1 = register_note('convo', '𝕽𝕯',
        'https://claude.ai/chat/d0792d66-0af2-4c21-bc8a-58e3a6420130',
        title='contextLatticeStamp main design session',
        manual_key='𝕮𝕷𝕾Main')
    print(f"  [𝒞 convo] {key1}")

    key2 = register_note('convo', '𝕽𝕯',
        'claude.ai/chat/redis-comparison',
        title='Redis vs alternatives')
    print(f"  [𝒞 convo] {key2} (auto-generated)")

    key3 = register_note('tw', '𝕽𝕯',
        'http://localhost:8080/#RedisDesign',
        title='Redis design patterns',
        manual_key='𝕽𝕯Design')
    print(f"  [𝒯 tw]    {key3}")

    print(f"\n  jump_note('convo', '{key1}') → {jump_note('convo', key1)}")
    print(f"\n✓ DataDict saved to: {DATADICT_FILE.absolute()}")

    print("\n── register_from_url Demo")
    register_from_url('http://localhost:8080/#TagVocabulary')
    register_from_url('https://claude.ai/chat/d0792d66-0af2-4c21-bc8a-58e3a6420130',
                      title='CLS main design session')
    register_from_url('https://github.com/HwWobbe/AiContext', category='𝕰𝖘')

    print("\n── Exec Template Demo")
    print("\nTest: exec_template('jump_tw', tiddler='Design%3ATagVocabulary')")
    print("  (Would open TiddlyWiki tiddler in browser)")
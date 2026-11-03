#!/usr/bin/env python3
"""
build_db.py — bygger jeeves.db (SQLite) fran de fyra Jeeves-markdownfilerna.

Kor fran mappen som innehaller kalfilerna (Tables_SE.md m.fl.):
    python build_db.py            # letar kalfiler i ../  och skriver jeeves.db har
    python build_db.py --src DIR  # ange var kalfilerna ligger

Skapar tabellerna:
    tables(code, name_sv, description)
    columns(table_code, prompt_sv, data_name, jeeves_type, chars, decimals, sql_type)
    terms(code, name_en, description)
    term_tables(term_code, table_code)      -- var en term/kolumn anvands
    programs(code, name_sv, description)
    program_tables(program_code, table_code)-- huvudtabell for program
    program_nodes(program_code, node_code, node_name)
    docareas(code, title, body)
    + FTS5-index for fritextsokning
"""
import argparse
import os
import re
import sqlite3
import sys

# ---- Regexmonster ------------------------------------------------------------

RE_BLOCK_SPLIT = re.compile(r'^# (?=tbd_|ted_|pgm_)', re.M)  # ej anvant direkt
RE_LINK = re.compile(r'\[([^\]]*)\]\(ms-its:[^)]*?/(tbd_|ted_|pgm_|doc_)([^.)]+)\.[Hh][Tt][Mm]\)')
# titelrad: **Namn** (Kod)
RE_TITLE = re.compile(r'^\*\*(.+?)\*\*\s*\(([^)]+)\)\s*$', re.M)
# fältrad i tabellista:  | [prompt](...ted_X.htm) | **DataName** | jtyp | tecken | dec | sqltyp |
RE_FIELD_ROW = re.compile(
    r'^\|\s*(.*?)\s*\|\s*\*\*([^*]+?)\*\*\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$',
    re.M
)
# program-huvudtabellrad i Tables: ### Program: [code](...pgm_X.HTM) **name**
RE_PGM_IN_TABLE = re.compile(r'\[[^\]]*\]\(ms-its:[^)]*?/pgm_([^.)]+)\.[Hh][Tt][Mm]\)\s*\*\*(.+?)\*\*')
# nodrad i Programs: * AA **NE-order** * AAA **Arbetsoperationer** ...
RE_NODE = re.compile(r'([A-Z][A-Za-z0-9]*)\s*\*\*(.+?)\*\*')


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def split_blocks(text, prefix):
    """Dela upp filen i (namn_fran_rubrik, kropp) per '# <prefix>...htm'."""
    parts = re.split(r'^# (' + prefix + r'[^\n]*?)\.[Hh][Tt][Mm]\s*$', text, flags=re.M)
    # parts = [pre, name1, body1, name2, body2, ...]
    out = []
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ''
        out.append((name, body))
    return out


def first_title(body):
    m = RE_TITLE.search(body)
    if m:
        # koden anvands som PRIMARY KEY och join-nyckel mot lank-harledda
        # koder (som redan ar rena) - maste rensas fran markdown-escapes
        # (t.ex. "Account\_xb" -> "Account_xb") annars matchar den aldrig.
        return clean(m.group(1)), clean(m.group(2))
    return None, None


def clean(s):
    s = (s or '').replace('\\_', '_').replace('\\*', '*')
    return re.sub(r'\s+', ' ', s).strip()


def description_before(body, *markers):
    """Text mellan titelraden och forsta forekomsten av nagon markor."""
    # ta bort titelunderstrykning (====) och plocka text fram till markor
    idx = len(body)
    for mk in markers:
        p = body.find(mk)
        if p != -1:
            idx = min(idx, p)
    seg = body[:idx]
    # ta bort titelrad och understrykningsrader
    lines = []
    for ln in seg.splitlines():
        s = ln.strip()
        if not s:
            continue
        if RE_TITLE.match(s):
            continue
        if set(s) <= set('=-'):
            continue
        if s.startswith('!['):  # bild
            continue
        lines.append(s)
    return clean(' '.join(lines))


# ---- Parsers -----------------------------------------------------------------

def parse_tables(text):
    tables, columns, table_programs = [], [], []
    for name, body in split_blocks(text, 'tbd_'):
        name_sv, code = first_title(body)
        code = code or clean(name.replace('tbd_', ''))
        desc = description_before(body, 'Tabellen innehller', 'Tabellen r huvudtabell',
                                  'Fljande standardposter')
        tables.append((code, name_sv or code, desc))
        # falt
        for m in RE_FIELD_ROW.finditer(body):
            prompt_cell, data_name, jtyp, tecken, dec, sqltyp = m.groups()
            # hoppa over rubrik-/skiljerader
            if data_name.lower() in ('datanamn',) or set(prompt_cell) <= set('-'):
                continue
            prompt_txt = re.sub(r'\[([^\]]*)\].*', r'\1', prompt_cell).strip() or prompt_cell.strip()
            columns.append((code, clean(prompt_txt), clean(data_name),
                            clean(jtyp), clean(tecken), clean(dec), clean(sqltyp)))
        # program dar tabellen ar huvudtabell
        seg = body[body.find('huvudtabell'):] if 'huvudtabell' in body else ''
        for pm in RE_PGM_IN_TABLE.finditer(seg):
            table_programs.append((code, pm.group(1).strip()))
    return tables, columns, table_programs


def parse_terms(text):
    terms, term_tables = [], []
    for name, body in split_blocks(text, 'ted_'):
        name_en, code = first_title(body)
        code = code or clean(name.replace('ted_', ''))
        desc = description_before(body, 'Fltet ingr', 'Faltet ingar')
        terms.append((code, name_en or code, desc))
        seg = body[body.find('ingr i'):] if 'ingr i' in body else body[body.find('ingar i'):] if 'ingar i' in body else ''
        for m in RE_LINK.finditer(seg or body):
            if m.group(2) == 'tbd_':
                term_tables.append((code, m.group(3).strip()))
    return terms, term_tables


def parse_programs(text):
    programs, program_tables, program_nodes = [], [], []
    for name, body in split_blocks(text, 'pgm_'):
        # titel i Programs: "Namn : **(Kod)**"
        m = re.search(r'^(.*?):\s*\*\*\(([^)]+)\)\*\*', body, re.M)
        if m:
            name_sv, code = clean(m.group(1)), clean(m.group(2))
        else:
            name_sv, code = None, clean(name.replace('pgm_', ''))
        # beskrivningstext borjar efter rubriken "Beskrivning" (om den finns)
        desc_start = body.find('Beskrivning')
        desc_body = body[desc_start + len('Beskrivning'):] if desc_start != -1 else body
        desc = description_before(desc_body, 'Huvudtabell', 'Fljande standardposter',
                                  'Tillmpningen beskrivs')
        programs.append((code, name_sv or code, desc))
        # huvudtabell
        seg_start = body.find('Huvudtabell')
        seg = body[seg_start:] if seg_start != -1 else ''
        for lm in RE_LINK.finditer(seg[:2000]):
            if lm.group(2) == 'tbd_':
                program_tables.append((code, lm.group(3).strip()))
                break
        # noder
        nstart = body.find('noder')
        if nstart != -1:
            nseg = body[nstart:nstart + 4000]
            for nm in RE_NODE.finditer(nseg):
                nc, nn = nm.group(1).strip(), clean(nm.group(2))
                if nc and nc.lower() != 'noder':
                    program_nodes.append((code, nc, nn))
    return programs, program_tables, program_nodes


def parse_docareas(text):
    docs = []
    parts = re.split(r'^# ([^\n]+?)\.[Hh][Tt][Mm]\s*$', text, flags=re.M)
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ''
        title = name
        for ln in body.splitlines():
            s = ln.strip().strip('*').strip()
            if s and not set(s) <= set('=-|') and not s.startswith('|'):
                title = s
                break
        docs.append((name, clean(title)[:300], clean(body)[:2500]))
    return docs


# ---- DB ----------------------------------------------------------------------

def build(src, out):
    files = {k: os.path.join(src, v) for k, v in {
        'tables': 'Tables_SE.md', 'terms': 'Terms_SE.md',
        'programs': 'Programs_SE.md', 'docareas': 'DocAreas_SE.md'}.items()}
    for p in files.values():
        if not os.path.exists(p):
            sys.exit(f'Hittar inte kalfil: {p}')

    tables, columns, table_programs = parse_tables(read(files['tables']))
    terms, term_tables = parse_terms(read(files['terms']))
    programs, program_tables_p, program_nodes = parse_programs(read(files['programs']))
    docareas = parse_docareas(read(files['docareas']))

    # Slaa ihop bada hallen av program<->huvudtabell-relationen (fran Tables_SE
    # resp. Programs_SE) till en deduplicerad lista - ger mest komplett tackning
    # for konsekvensanalys (vilka program paverkas av en tabell).
    program_tables = sorted(set(
        [(p, t) for (t, p) in table_programs] + [(p, t) for (p, t) in program_tables_p]
    ))

    if os.path.exists(out):
        os.remove(out)
    db = sqlite3.connect(out)
    c = db.cursor()
    # Jeeves-koder skrivs olika (versaler/gemener) beroende pa kalfil
    # (t.ex. "ak" i Tables_SE.md vs "Ak"/"AK" i Programs_SE.md-lankar).
    # COLLATE NOCASE pa alla kod-/nyckelkolumner gor joins och uppslag
    # skiftlagesokansliga automatiskt, utan att varje fraga maste minnas det.
    c.executescript('''
        CREATE TABLE tables(code TEXT PRIMARY KEY COLLATE NOCASE, name_sv TEXT, description TEXT);
        CREATE TABLE columns(table_code TEXT COLLATE NOCASE, prompt_sv TEXT, data_name TEXT COLLATE NOCASE,
                             jeeves_type TEXT, chars TEXT, decimals TEXT, sql_type TEXT);
        CREATE TABLE terms(code TEXT PRIMARY KEY COLLATE NOCASE, name_en TEXT, description TEXT);
        CREATE TABLE term_tables(term_code TEXT COLLATE NOCASE, table_code TEXT COLLATE NOCASE);
        CREATE TABLE programs(code TEXT PRIMARY KEY COLLATE NOCASE, name_sv TEXT, description TEXT);
        CREATE TABLE program_tables(program_code TEXT COLLATE NOCASE, table_code TEXT COLLATE NOCASE);
        CREATE TABLE program_nodes(program_code TEXT COLLATE NOCASE, node_code TEXT, node_name TEXT);
        CREATE TABLE docareas(code TEXT, title TEXT, body TEXT);
        CREATE INDEX ix_columns_table ON columns(table_code);
        CREATE INDEX ix_columns_data  ON columns(data_name);
        CREATE INDEX ix_termtab_term  ON term_tables(term_code);
        CREATE INDEX ix_termtab_table ON term_tables(table_code);
        CREATE INDEX ix_progtab_prog  ON program_tables(program_code);
        CREATE INDEX ix_progtab_table ON program_tables(table_code);
    ''')
    c.executemany('INSERT OR IGNORE INTO tables VALUES(?,?,?)', tables)
    c.executemany('INSERT INTO columns VALUES(?,?,?,?,?,?,?)', columns)
    c.executemany('INSERT OR IGNORE INTO terms VALUES(?,?,?)', terms)
    c.executemany('INSERT INTO term_tables VALUES(?,?)', term_tables)
    c.executemany('INSERT OR IGNORE INTO programs VALUES(?,?,?)', programs)
    c.executemany('INSERT INTO program_tables VALUES(?,?)', program_tables)
    c.executemany('INSERT INTO program_nodes VALUES(?,?,?)', program_nodes)
    c.executemany('INSERT INTO docareas VALUES(?,?,?)', docareas)

    # Ingen FTS5: en full uppsattning FTS-index over tables/terms/programs/
    # docareas gjorde filen ~32 MB - for nara Claude.ai:s 30 MB-grans
    # (uppackad storlek) for att vara sakert. Fritextsokning gors istallet
    # med vanlig LIKE mot description/name_sv/name_en/title - fullt
    # tillrackligt snabbt pa dessa radantal (max ~12k rader) i en
    # engangsfraga, och havallar filen pa ~19 MB med gott om marginal.
    c.executescript('''
        CREATE INDEX ix_tables_name ON tables(name_sv);
        CREATE INDEX ix_terms_name  ON terms(name_en);
        CREATE INDEX ix_programs_name ON programs(name_sv);
    ''')
    db.commit()
    c.execute('VACUUM')

    stats = {
        'tables': len(tables), 'columns': len(columns),
        'terms': len(terms), 'term_tables': len(term_tables),
        'programs': len(programs), 'program_tables': len(program_tables),
        'program_nodes': len(program_nodes), 'docareas': len(docareas),
    }
    db.close()
    return stats


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument('--src', default=os.path.dirname(here),
                    help='mapp med kalfilerna (default: parent)')
    ap.add_argument('--out', default=os.path.join(here, 'jeeves.db'))
    a = ap.parse_args()
    s = build(a.src, a.out)
    print('Klar ->', a.out)
    for k, v in s.items():
        print(f'  {k:16} {v:>7}')

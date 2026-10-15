# -*- coding: utf-8 -*-
"""
Master Builder for Oral Pathology & Microbiology University Exam Preparation Suite
Generates:
1. Oral_Pathology_Master_Notes.md (Cleaned Markdown with tables and 15-mark monographs)
2. Oral_Pathology_Master_Notes.html (Print-ready document with embedded schematics)
3. Oral_Pathology_Master_Notes.pdf (Headless Edge compiled PDF)
4. index.html (Responsive, Interactive Study Dashboard & Microscopic Spotter Explorer)
"""

import os
import sys
import json
import subprocess

from content.odontogenic_cysts_and_tumors import CHAPTERS as c1
from content.salivary_and_neoplasms import CHAPTERS as c2
from content.caries_and_developmental import CHAPTERS as c3
from content.infections_blood_bone_forensic import CHAPTERS as c4
from content.formatter import ICONS, FAVICON_SVG, clean_latex, parse_markdown_to_html
from content.interactive_data import COMPARISON_MATRICES, SPOTTER_CARDS, VIVA_QUIZ
from content.diagrams_data import generate_svg_schematic, LAYMAN_ANALOGIES, FLASHCARDS

ALL_CHAPTERS = c1 + c2 + c3 + c4

def generate_markdown(chapters):
    md_lines = []
    md_lines.append("# Master Compendium of Oral Pathology & Microbiology: 15-Mark University Examination Monograph")
    md_lines.append("\n*Comprehensive Clinical & Histopathological Study Guide for BDS (3rd Year) & Postgraduate Dental Examinations based on Shafer, Neville, Cawson, Regezi & OPN Lecture Blueprints*\n")
    md_lines.append("## Curriculum Table of Contents")
    for i, ch in enumerate(chapters, 1):
        md_lines.append(f"{i}. [{ch['title']}](#{ch['id']}) - *{ch['category']}*")
    md_lines.append("\n---\n")

    for ch in chapters:
        md_lines.append(f"<a id='{ch['id']}'></a>")
        md_lines.append(f"## {ch['title']}")
        md_lines.append(f"**Category:** {ch['category']} | **Standard:** {ch['badge']} | **Reading Time:** {ch['reading_time']}\n")
        
        md_lines.append("### High-Yield Key Points")
        for kp in ch["key_points"]:
            md_lines.append(f"- {clean_latex(kp)}")
        md_lines.append("")

        md_lines.append(f"> [!TIP]\n> **Clinical & Histopathological Pearl:** {clean_latex(ch['clinical_pearl'])}\n")

        layman = LAYMAN_ANALOGIES.get(ch["id"])
        if layman:
            md_lines.append(f"> [!NOTE]\n> **Layman's Intuition — {layman['title']}:**\n> {layman['analogy']}\n")

        md_lines.append("### Comprehensive 15-Mark Structural Monograph")
        for sec in ch["sections"]:
            md_lines.append(f"\n#### {sec['title']}\n")
            md_lines.append(clean_latex(sec["content"].strip()))
            md_lines.append("")

        md_lines.append("\n---\n")

    return "\n".join(md_lines)

def generate_print_html(chapters):
    html_parts = []
    html_parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="{FAVICON_SVG}">
<title>Oral Pathology & Microbiology Master Compendium - 15-Mark University Examination Monograph</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap');

@page {{
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {{
        content: counter(page);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #6b21a8;
    }}
    @bottom-left {{
        content: "Oral Pathology & Microbiology Master Monograph | University Exam Preparation";
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #6b21a8;
    }}
}}

body {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.6;
    font-size: 9.5pt;
}}

.cover-page {{
    page-break-after: always;
    height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;
    border-left: 8px solid #9333ea;
    background: #fafaf9;
}}

.cover-title {{
    font-family: 'Newsreader', serif;
    font-size: 32pt;
    font-weight: 700;
    color: #581c87;
    line-height: 1.15;
    margin-bottom: 8px;
}}

.cover-subtitle {{
    font-size: 13pt;
    color: #7e22ce;
    font-weight: 600;
    margin-bottom: 24px;
}}

.cover-meta {{
    font-size: 9.5pt;
    color: #475569;
    line-height: 1.8;
}}

.chapter-container {{
    page-break-before: always;
    margin-bottom: 25px;
}}

.chapter-badge {{
    display: inline-block;
    background: #fdf4ff;
    color: #86198f;
    border: 1px solid #f0abfc;
    font-size: 7.5pt;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}}

.chapter-title {{
    font-family: 'Newsreader', serif;
    font-size: 20pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 12px;
    border-bottom: 2px solid #9333ea;
    padding-bottom: 6px;
}}

.pearl-box {{
    background: #faf5ff;
    border-left: 4px solid #a855f7;
    padding: 10px 14px;
    margin: 14px 0;
    font-size: 9pt;
    color: #581c87;
    border-radius: 0 6px 6px 0;
}}

.layman-box {{
    background: #f8fafc;
    border-left: 4px solid #0284c7;
    padding: 10px 14px;
    margin: 14px 0;
    font-size: 8.8pt;
    color: #0f172a;
    border-radius: 0 6px 6px 0;
}}

.section-title {{
    font-size: 11.5pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 18px;
    margin-bottom: 8px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.8pt;
    page-break-inside: avoid;
}}

th, td {{
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: #f8fafc;
    color: #0f172a;
    font-weight: 700;
}}

tr:nth-child(even) {{
    background-color: #f1f5f9;
}}

code, pre {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 2px 6px;
}}

pre {{
    padding: 12px;
    overflow-x: auto;
    white-space: pre-wrap;
    line-height: 1.4;
}}

ul, ol {{
    padding-left: 20px;
    margin-top: 6px;
    margin-bottom: 10px;
}}

li {{
    margin-bottom: 4px;
}}
</style>
</head>
<body>
<div class="cover-page">
    <div style="width: 50px; height: 50px; background: #9333ea; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 24pt; font-weight: 800;">OP</div>
    <div class="cover-title">Oral Pathology &amp; Microbiology</div>
    <div class="cover-subtitle">15-Mark University Examination Master Monograph</div>
    <div class="cover-meta">
        <strong>Curriculum:</strong> BDS 3rd Year &amp; MDS Oral Pathology Standards<br>
        <strong>Primary References:</strong> Shafer's Textbook of Oral Pathology, Neville Oral &amp; Maxillofacial Pathology, Cawson Essentials<br>
        <strong>Core Inclusions:</strong> Vickers-Gorlin Criteria, Odontogenic Cysts &amp; Tumors, Salivary Gland Neoplasms, OPMD &amp; OSCC, Forensic Odontology
    </div>
</div>
""")

    for ch in chapters:
        html_parts.append(f"""<div class="chapter-container" id="{ch['id']}">
        <span class="chapter-badge">{ch['category']} • {ch['badge']}</span>
        <h1 class="chapter-title">{ch['title']}</h1>
        
        <div class="pearl-box">
            <strong>Clinical &amp; Histopathological Pearl:</strong> {clean_latex(ch['clinical_pearl'])}
        </div>
        """)

        layman = LAYMAN_ANALOGIES.get(ch["id"])
        if layman:
            html_parts.append(f"""<div class="layman-box">
                <strong style="color: #0369a1;">Layman's Intuition — {layman['title']}:</strong><br>
                {layman['analogy']}
            </div>""")

        for sec in ch["sections"]:
            html_parts.append(f"""<h3 class="section-title">{sec['title']}</h3>""")
            html_parts.append(parse_markdown_to_html(sec["content"]))

        html_parts.append("</div>")

    html_parts.append("</body></html>")
    return "\n".join(html_parts)

def generate_interactive_dashboard(chapters):
    enriched_chapters = []
    for ch in chapters:
        ch_id = ch["id"]
        svg_diagram = generate_svg_schematic(ch_id, ch["title"])
        analogy = LAYMAN_ANALOGIES.get(ch_id, {
            "title": "Pathological Intuition",
            "analogy": ch["clinical_pearl"]
        })
        cards = FLASHCARDS.get(ch_id, [
            {"q": f"What is the microscopic hallmark of {ch['title']}?", "a": ch['clinical_pearl']}
        ])
        
        # Classification types from sections
        type_list = []
        for sec in ch["sections"][:4]:
            type_list.append({
                "name": sec["title"],
                "badge": "Histopathologic Criterion",
                "hemodynamics": "Pathognomonic Microscopic Sign",
                "summary": clean_latex(sec["content"][:220].strip()) + "..."
            })
        custom_types = {
            "title": f"Histopathological Classifications: {ch['title']}",
            "types": type_list
        }

        # Viva questions
        viva_list = []
        for c in cards:
            viva_list.append(c["q"])

        enriched_chapters.append({
            "id": ch["id"],
            "title": ch["title"],
            "category": ch["category"],
            "badge": ch["badge"],
            "reading_time": ch["reading_time"],
            "clinical_pearl": ch["clinical_pearl"],
            "key_points": ch.get("key_points", []),
            "sections": ch["sections"],
            "schematic_svg": svg_diagram,
            "analogy": analogy,
            "flashcards": cards,
            "classification": custom_types,
            "viva_questions": viva_list
        })

    chapters_json = json.dumps(enriched_chapters)
    matrices_json = json.dumps(COMPARISON_MATRICES)
    spotters_json = json.dumps(SPOTTER_CARDS)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="{FAVICON_SVG}">
    <title>Oral Pathology Master Portal — University Exam Companion</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #fdfcf9;
            --bg-surface: #ffffff;
            --bg-card: #ffffff;
            --bg-card-hover: #fdf4ff;
            --border-color: #cbd5e1;
            --border-active: #9333ea;
            --text-primary: #0f172a;
            --text-secondary: #334155;
            --text-muted: #475569;
            --accent-primary: #9333ea;
            --accent-light: #faf5ff;
            --accent-glow: rgba(147, 51, 234, 0.18);
            --header-bg: rgba(253, 252, 249, 0.94);
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 14px rgba(0,0,0,0.08);
            --shadow-lg: 0 10px 30px rgba(0,0,0,0.12);
        }}

        body.dark {{
            --bg-base: #0d0b18;
            --bg-surface: #151226;
            --bg-card: #1c1833;
            --bg-card-hover: #272247;
            --border-color: rgba(255, 255, 255, 0.14);
            --border-active: #c084fc;
            --text-primary: #f8fafc;
            --text-secondary: #e2e8f0;
            --text-muted: #cbd5e1;
            --accent-primary: #c084fc;
            --accent-light: rgba(192, 132, 252, 0.15);
            --accent-glow: rgba(192, 132, 252, 0.25);
            --header-bg: rgba(13, 11, 24, 0.94);
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 14px rgba(0,0,0,0.4);
            --shadow-lg: 0 10px 30px rgba(0,0,0,0.6);
        }}

        /* Ultra-thin surgical scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: transparent;
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(148, 163, 184, 0.35);
            border-radius: 999px;
            border: 1px solid transparent;
            background-clip: content-box;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(100, 116, 139, 0.6);
        }}
        body.dark ::-webkit-scrollbar-thumb {{
            background: rgba(148, 163, 184, 0.25);
        }}
        body.dark ::-webkit-scrollbar-thumb:hover {{
            background: rgba(148, 163, 184, 0.45);
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            scrollbar-width: thin;
            scrollbar-color: rgba(148, 163, 184, 0.35) transparent;
        }}

        /* Tactile button feedback */
        .btn:active, .nav-btn:active, .speed-pill:active, .mobile-bottom-tab:active, .filter-chip:active {{
            transform: scale(0.96) translateY(1px);
        }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-base);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            transition: background-color 0.25s ease, color 0.25s ease;
        }}

        /* Header Navbar */
        .navbar {{
            position: sticky;
            top: 0;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            background: var(--header-bg);
            border-bottom: 1px solid var(--border-color);
            padding: 0.75rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 100;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: inherit;
            cursor: pointer;
        }}

        .brand-badge {{
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, #9333ea, #7e22ce);
            border-radius: 9px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.05rem;
            color: #ffffff;
            box-shadow: 0 4px 10px rgba(147, 51, 234, 0.25);
        }}

        .brand-title h1 {{
            font-size: 1.05rem;
            font-weight: 700;
            letter-spacing: -0.3px;
        }}

        .brand-title span {{
            font-size: 0.72rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.5px;
        }}

        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .nav-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 7px 14px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: var(--shadow-sm);
        }}

        .nav-btn:hover {{
            background: var(--accent-light);
            border-color: var(--accent-primary);
            color: var(--accent-primary);
        }}

        .nav-btn-primary {{
            background: var(--accent-primary);
            color: #ffffff !important;
            border-color: transparent;
        }}
        .nav-btn-primary:hover {{
            background: #7e22ce;
        }}

        /* Main App Grid Layout */
        .app-layout {{
            display: flex;
            flex: 1;
            max-width: 1560px;
            width: 100%;
            margin: 0 auto;
            position: relative;
        }}

        /* Sidebar */
        .sidebar {{
            width: 330px;
            flex-shrink: 0;
            border-right: 1px solid var(--border-color);
            background: var(--bg-surface);
            display: flex;
            flex-direction: column;
            height: calc(100vh - 61px);
            position: sticky;
            top: 61px;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 40;
        }}

        .sidebar-header {{
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        .search-box {{
            position: relative;
            margin-bottom: 10px;
        }}

        .search-input {{
            width: 100%;
            padding: 9px 36px 9px 12px;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 0.85rem;
            font-family: inherit;
            outline: none;
            transition: border-color 0.2s ease;
        }}
        .search-input:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }}

        .search-kbd {{
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 4px;
            font-size: 0.7rem;
            padding: 1px 5px;
            color: var(--text-muted);
            pointer-events: none;
        }}

        .category-scroll {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}

        .filter-chip {{
            white-space: nowrap;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.72rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 999px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .filter-chip:hover, .filter-chip.active {{
            background: var(--accent-primary);
            color: #ffffff;
            border-color: var(--accent-primary);
        }}

        .topic-list {{
            flex: 1;
            overflow-y: auto;
            padding: 8px;
        }}

        .topic-item {{
            display: flex;
            align-items: flex-start;
            gap: 10px;
            padding: 10px 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
            margin-bottom: 4px;
            border: 1px solid transparent;
        }}
        .topic-item:hover {{
            background: var(--bg-card-hover);
        }}
        .topic-item.active {{
            background: var(--accent-light);
            border-color: var(--accent-primary);
        }}
        .topic-check {{
            margin-top: 2px;
            color: var(--text-muted);
            cursor: pointer;
            flex-shrink: 0;
        }}
        .topic-check.completed {{
            color: var(--accent-primary);
        }}
        .topic-info {{
            flex: 1;
            min-width: 0;
        }}
        .topic-title {{
            font-size: 0.86rem;
            font-weight: 600;
            color: var(--text-primary);
            line-height: 1.35;
        }}
        .topic-meta {{
            font-size: 0.72rem;
            color: var(--text-secondary);
            font-weight: 500;
            margin-top: 2px;
        }}

        /* Content Area */
        .content-area {{
            flex: 1;
            min-width: 0;
            padding: 24px 32px 120px 32px;
            overflow-y: auto;
        }}

        /* Dashboard Hero */
        .dash-hero {{
            background: linear-gradient(135deg, rgba(147, 51, 234, 0.08), rgba(126, 34, 206, 0.03));
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            flex-wrap: wrap;
        }}
        .dash-badge {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-primary);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        .dash-title {{
            font-family: 'Newsreader', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .dash-subtitle {{
            font-size: 0.88rem;
            color: var(--text-secondary);
            margin-top: 4px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 12px;
            margin-bottom: 28px;
        }}
        .stat-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 14px 18px;
            box-shadow: var(--shadow-sm);
        }}
        .stat-val {{
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--accent-primary);
            line-height: 1.1;
        }}
        .stat-lbl {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
            margin-top: 4px;
        }}

        /* Chapter View Header & Tabs */
        .chapter-header {{
            margin-bottom: 20px;
        }}
        .chapter-top-badge {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-primary);
            font-size: 0.75rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 6px;
            text-transform: uppercase;
            margin-bottom: 8px;
            border: 1px solid var(--accent-primary);
        }}
        body.dark .chapter-top-badge {{
            background: rgba(192, 132, 252, 0.2);
            color: #d8b4fe;
            border-color: #d8b4fe;
        }}
        .chapter-title-display {{
            font-family: 'Newsreader', serif;
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--text-primary);
            line-height: 1.2;
            letter-spacing: -0.5px;
        }}

        .tab-bar-container {{
            position: sticky;
            top: 61px;
            background: var(--bg-base);
            z-index: 30;
            padding: 10px 0;
            margin-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
        }}
        .tab-bar {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .tab-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.82rem;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            white-space: nowrap;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: var(--shadow-sm);
        }}
        .tab-btn:hover {{
            background: var(--bg-card-hover);
            color: var(--text-primary);
        }}
        .tab-btn.active {{
            background: var(--accent-primary);
            color: #ffffff;
            border-color: var(--accent-primary);
            box-shadow: 0 4px 12px var(--accent-glow);
        }}

        /* 15-Mark Master Essay Reading Ergonomics */
        .master-essay-content {{
            max-width: 76ch;
            margin: 0 auto;
        }}
        .pearl-card {{
            background: var(--accent-light);
            border-left: 4px solid var(--accent-primary);
            border-radius: 0 8px 8px 0;
            padding: 14px 18px;
            margin-bottom: 24px;
            font-size: 0.92rem;
            color: var(--text-primary);
        }}
        .essay-section-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px 28px;
            margin-bottom: 20px;
            box-shadow: var(--shadow-sm);
        }}
        .essay-section-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
        }}
        .essay-section-title {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .essay-body {{
            font-size: 0.96rem;
            line-height: 1.72;
            color: var(--text-secondary);
        }}
        .essay-body h4 {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-primary);
            margin: 18px 0 8px 0;
        }}
        .essay-body p {{
            margin-bottom: 14px;
        }}
        .essay-body ul, .essay-body ol {{
            padding-left: 22px;
            margin-bottom: 14px;
        }}
        .essay-body li {{
            margin-bottom: 6px;
        }}
        .essay-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 18px 0;
            font-size: 0.88rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            overflow: hidden;
        }}
        .essay-body th, .essay-body td {{
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        .essay-body th {{
            background: var(--bg-base);
            color: var(--text-primary);
            font-weight: 700;
        }}
        .essay-body tr:nth-child(even) {{
            background: var(--bg-card-hover);
        }}
        .essay-body pre {{
            background: #0f172a;
            color: #f0abfc;
            border-radius: 8px;
            padding: 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            overflow-x: auto;
            margin: 16px 0;
        }}

        /* Layman Intuition Card */
        .layman-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 28px;
            box-shadow: var(--shadow-sm);
        }}
        .layman-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }}
        .layman-badge {{
            background: #fdf4ff;
            color: #86198f;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 6px;
        }}
        .layman-title {{
            font-family: 'Newsreader', serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .layman-body {{
            font-size: 1.02rem;
            line-height: 1.8;
            color: var(--text-secondary);
        }}

        /* Classification / Types Explorer */
        .types-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 18px;
        }}
        .type-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease;
        }}
        .type-card:hover {{
            border-color: var(--accent-primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }}
        .type-card-badge {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-primary);
            font-size: 0.72rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
            margin-bottom: 8px;
        }}
        .type-card-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}
        .type-card-stat {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 6px 10px;
            font-size: 0.78rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--accent-primary);
            margin-bottom: 10px;
        }}
        .type-card-summary {{
            font-size: 0.88rem;
            color: var(--text-secondary);
            line-height: 1.5;
        }}

        /* Diagrams Gallery */
        .diagram-container {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
        }}
        .diagram-title {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 14px;
        }}
        .diagram-viewer-box {{
            cursor: zoom-in;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #0f172a;
        }}

        /* Examiner Viva Voce */
        .viva-item {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px 22px;
            margin-bottom: 14px;
            box-shadow: var(--shadow-sm);
        }}
        .viva-q {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}
        .viva-speaker-btn {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--accent-primary);
            width: 32px;
            height: 32px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }}
        .viva-speaker-btn:hover {{
            background: var(--accent-light);
            border-color: var(--accent-primary);
        }}
        .viva-reveal-btn {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.8rem;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 6px;
            cursor: pointer;
            margin-top: 6px;
        }}
        .viva-ans {{
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px dashed var(--border-color);
            font-size: 0.92rem;
            color: var(--text-secondary);
            display: none;
        }}
        .viva-ans.revealed {{
            display: block;
        }}

        /* Active Recall Flashcards */
        .flashcard-wrap {{
            max-width: 620px;
            margin: 20px auto;
            perspective: 1000px;
        }}
        .flashcard {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            min-height: 280px;
            padding: 36px 32px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            cursor: pointer;
            box-shadow: var(--shadow-md);
            position: relative;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .flashcard:hover {{
            border-color: var(--accent-primary);
        }}
        .flashcard-tag {{
            position: absolute;
            top: 18px;
            left: 20px;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--accent-primary);
        }}
        .flashcard-instruction {{
            position: absolute;
            bottom: 16px;
            font-size: 0.75rem;
            color: var(--text-secondary);
            font-weight: 600;
        }}
        .flashcard-text {{
            font-size: 1.18rem;
            font-weight: 600;
            color: var(--text-primary);
            line-height: 1.6;
        }}
        .flashcard-controls {{
            display: flex;
            justify-content: center;
            gap: 14px;
            margin-top: 20px;
        }}

        /* Exam Simulator & Rubric */
        .exam-sim-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            box-shadow: var(--shadow-sm);
        }}
        .rubric-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 12px 0;
            border-bottom: 1px solid var(--border-color);
        }}
        .rubric-info h4 {{
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .rubric-info p {{
            font-size: 0.82rem;
            color: var(--text-muted);
        }}
        .rubric-slider {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        /* Clinical Notes */
        .notes-textarea {{
            width: 100%;
            height: 380px;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            font-family: inherit;
            font-size: 0.95rem;
            color: var(--text-primary);
            line-height: 1.6;
            outline: none;
            resize: vertical;
        }}
        .notes-textarea:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }}

        /* Modern Floating Island Audio Player Dock */
        .audio-dock {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 48px);
            max-width: 1040px;
            z-index: 1050;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(28px) saturate(180%);
            -webkit-backdrop-filter: blur(28px) saturate(180%);
            border: 1px solid rgba(147, 51, 234, 0.25);
            border-radius: 22px;
            box-shadow: 0 16px 42px -6px rgba(15, 23, 42, 0.25), 0 4px 16px rgba(0, 0, 0, 0.05);
            padding: 12px 22px;
            display: block;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
        }}
        body.dark .audio-dock {{
            background: rgba(21, 18, 38, 0.94);
            border: 1px solid rgba(192, 132, 252, 0.25);
            box-shadow: 0 20px 50px -8px rgba(0, 0, 0, 0.75), 0 0 24px rgba(147, 51, 234, 0.18);
        }}
        .audio-dock.hidden {{
            transform: translate(-50%, 150%);
            opacity: 0;
            pointer-events: none;
        }}
        .audio-dock-inner {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            flex-wrap: wrap;
        }}
        .audio-dock-meta {{
            display: flex;
            align-items: center;
            gap: 12px;
            min-width: 200px;
            max-width: 300px;
            flex-shrink: 0;
        }}
        .audio-dock-track-icon {{
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, #9333ea 0%, #7e22ce 100%);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(147, 51, 234, 0.3);
        }}
        .audio-dock.is-playing .audio-dock-track-icon {{
            animation: pulseTrackIcon 2.4s ease-in-out infinite;
        }}
        @keyframes pulseTrackIcon {{
            0%, 100% {{ transform: scale(1); box-shadow: 0 4px 12px rgba(147, 51, 234, 0.3); }}
            50% {{ transform: scale(1.05); box-shadow: 0 6px 18px rgba(147, 51, 234, 0.45); }}
        }}
        .audio-dock-track-title {{
            font-size: 9pt;
            font-weight: 700;
            color: var(--text-primary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .audio-dock-chapter-title {{
            font-size: 7.5pt;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-top: 2px;
        }}
        .audio-dock-controls-wrap {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            flex: 1;
            min-width: 240px;
        }}
        .audio-dock-buttons {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .audio-control-btn {{
            background: transparent;
            border: none;
            color: var(--text-primary);
            cursor: pointer;
            padding: 6px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }}
        .audio-control-btn:hover {{
            background: var(--bg-card-hover);
            color: var(--accent-primary);
        }}
        .audio-btn-playpause {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--accent-primary);
            color: #ffffff !important;
            box-shadow: 0 4px 14px var(--accent-glow);
        }}
        .audio-btn-playpause:hover {{
            background: #7e22ce;
            transform: scale(1.04);
        }}
        .audio-dock-progress-wrap {{
            display: flex;
            align-items: center;
            gap: 10px;
            width: 100%;
            max-width: 440px;
        }}
        .audio-time-label {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 7.5pt;
            color: var(--text-secondary);
            min-width: 36px;
            font-weight: 600;
        }}
        .audio-scrubber {{
            flex: 1;
            -webkit-appearance: none;
            appearance: none;
            height: 4px;
            border-radius: 999px;
            background: #cbd5e1;
            outline: none;
            cursor: pointer;
        }}
        body.dark .audio-scrubber {{
            background: #334155;
        }}
        .audio-scrubber::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent-primary);
            cursor: pointer;
        }}
        .audio-dock-options {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }}
        .audio-voice-select {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            font-size: 7.5pt;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: 8px;
            outline: none;
            cursor: pointer;
            max-width: 160px;
        }}
        .audio-speed-selector {{
            display: flex;
            align-items: center;
            gap: 4px;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 3px 6px;
        }}
        .speed-label {{
            font-size: 7.5pt;
            color: var(--text-primary);
            font-weight: 700;
            margin-right: 2px;
        }}
        .speed-pill {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 7.5pt;
            font-weight: 700;
            padding: 3px 6px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .speed-pill:hover {{
            color: var(--accent-primary);
        }}
        .speed-pill.active {{
            background: var(--accent-primary);
            color: #ffffff;
        }}
        .audio-dock-close {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            padding: 6px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .audio-dock-close:hover {{
            background: var(--bg-card-hover);
            color: #ef4444;
        }}

        /* Mobile Bottom Floating Bar */
        .mobile-bottom-bar {{
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--header-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-top: 1px solid var(--border-color);
            padding: 6px 12px 10px 12px;
            z-index: 90;
            justify-content: space-around;
        }}
        .mobile-bottom-tab {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 0.74rem;
            font-weight: 700;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 8px;
        }}
        .mobile-bottom-tab.active {{
            color: var(--accent-primary);
        }}

        /* Modals */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.82);
            backdrop-filter: blur(8px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 2000;
            padding: 20px;
        }}
        .modal-box {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            max-width: 960px;
            width: 100%;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }}
        .modal-header {{
            padding: 14px 20px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .modal-body {{
            padding: 20px;
            overflow-y: auto;
            flex: 1;
        }}

        @media (max-width: 1024px) {{
            .audio-dock {{
                bottom: 74px !important;
                padding: 10px 16px;
            }}
            .sidebar {{
                position: fixed;
                left: 0;
                top: 61px;
                bottom: 0;
                transform: translateX(-100%);
            }}
            .sidebar.open {{
                transform: translateX(0);
            }}
            .mobile-bottom-bar {{
                display: flex;
            }}
            .content-area {{
                padding: 16px 16px 140px 16px;
            }}
        }}

        @media (max-width: 640px) {{
            .navbar {{
                padding: 0.6rem 1rem;
            }}
            .chapter-title-display {{
                font-size: 1.6rem;
            }}
            .audio-dock {{
                width: calc(100% - 24px);
                padding: 8px 12px;
            }}
            .audio-voice-wrap {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <!-- Top Header -->
    <header class="navbar">
        <div class="brand" onclick="showDashboard()">
            <div class="brand-badge">OP</div>
            <div class="brand-title">
                <h1>ORAL PATHOLOGY</h1>
                <span>Clinical &amp; Spotter Suite</span>
            </div>
        </div>
        <div class="nav-actions">
            <button class="nav-btn" onclick="togglePlayPauseAudio()" title="Continuous Audio Walk">
                {ICONS["headphones"]}
                <span>Audio Walk</span>
            </button>
            <button class="nav-btn" onclick="openPdfModal()" title="View Master PDF">
                {ICONS["pdf"]}
                <span>Master PDF</span>
            </button>
            <button class="nav-btn" onclick="toggleTheme()" id="themeToggleBtn" aria-label="Toggle dark/light mode">
                {ICONS["moon"]}
            </button>
        </div>
    </header>

    <div class="app-layout">
        <!-- Sidebar Navigation -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="search-box">
                    <input type="text" id="searchInput" class="search-input" placeholder="Search lesions, signs, stains..." oninput="onSearchInput()">
                    <span class="search-kbd">/</span>
                </div>
                <div class="category-scroll" id="categoryPillBar">
                    <button class="filter-chip active" onclick="setCategoryFilter('All')">All Topics</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Tumor')">Tumors</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Cyst')">Cysts</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Salivary')">Salivary</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Oncology')">Oncology</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Caries')">Caries</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Developmental')">Developmental</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Infectious')">Infections</button>
                    <button class="filter-chip" onclick="setCategoryFilter('Forensic')">Forensic</button>
                </div>
            </div>
            <div class="topic-list" id="sidebarTopicList" tabindex="0" aria-label="Curriculum topics list">
                <!-- Dynamically rendered -->
            </div>
        </aside>

        <!-- Main Content Viewer -->
        <main class="content-area" id="mainContent">
            <!-- Dynamically rendered (Dashboard or Chapter View) -->
        </main>
    </div>

    <!-- Mobile Floating Bottom Navigation Bar -->
    <nav class="mobile-bottom-bar" id="mobileFloatingBottomBar">
        <button class="mobile-bottom-tab" onclick="toggleMobileSidebar()">
            {ICONS["menu"]}
            <span>Topics</span>
        </button>
        <button class="mobile-bottom-tab active" onclick="switchTab('master')">
            {ICONS["master_answer"]}
            <span>15-Mark</span>
        </button>
        <button class="mobile-bottom-tab" onclick="switchTab('diagrams')">
            {ICONS["diagrams"]}
            <span>Spotters</span>
        </button>
        <button class="mobile-bottom-tab" onclick="switchTab('viva')">
            {ICONS["viva"]}
            <span>Viva</span>
        </button>
        <button class="mobile-bottom-tab" onclick="togglePlayPauseAudio()">
            {ICONS["headphones"]}
            <span>Audio</span>
        </button>
    </nav>

    <!-- Floating Island Audio Dock -->
    <div id="masterAudioDock" class="audio-dock hidden">
        <div class="audio-dock-inner">
            <div class="audio-dock-meta">
                <div class="audio-dock-track-icon">{ICONS["headphones"]}</div>
                <div class="audio-dock-text">
                    <div class="audio-dock-track-title" id="audioDockTrackTitle">Section Audio</div>
                    <div class="audio-dock-chapter-title" id="audioDockChapterTitle">Oral Pathology Monograph</div>
                </div>
            </div>

            <div class="audio-dock-controls-wrap">
                <div class="audio-dock-buttons">
                    <button class="audio-control-btn" onclick="prevAudioTrack()" title="Previous Section">{ICONS["prev_track"]}</button>
                    <button class="audio-control-btn audio-btn-playpause" onclick="togglePlayPauseAudio()" id="audioDockPlayPauseBtn" title="Play / Pause">{ICONS["play"]}</button>
                    <button class="audio-control-btn" onclick="nextAudioTrack()" title="Next Section">{ICONS["next_track"]}</button>
                </div>
                <div class="audio-dock-progress-wrap">
                    <span class="audio-time-label" id="audioCurrentTime">0:00</span>
                    <input type="range" class="audio-scrubber" id="audioProgressScrubber" min="0" max="100" value="0" oninput="onAudioScrub(this.value)" aria-label="Audio playback progress scrubber">
                    <span class="audio-time-label" id="audioDuration">0:00</span>
                </div>
            </div>

            <div class="audio-dock-options">
                <div class="audio-voice-wrap" title="Narration Voice Engine">
                    <span class="speed-label">Voice:</span>
                    <select id="audioVoiceSelect" class="audio-voice-select" onchange="onVoiceSelected(this.value)" aria-label="Select Narration Voice">
                        <option value="">Auto (Natural Studio)</option>
                    </select>
                </div>
                <div class="audio-speed-selector">
                    <span class="speed-label">Speed:</span>
                    <button class="speed-pill active" onclick="setAudioPlaybackRate(1.0)" data-speed="1.0">1x</button>
                    <button class="speed-pill" onclick="setAudioPlaybackRate(1.25)" data-speed="1.25">1.25x</button>
                    <button class="speed-pill" onclick="setAudioPlaybackRate(1.5)" data-speed="1.5">1.5x</button>
                    <button class="speed-pill" onclick="setAudioPlaybackRate(2.0)" data-speed="2.0">2x</button>
                </div>
                <button class="audio-dock-close" onclick="closeAudioDock()" title="Stop and Close Player">{ICONS["close"]}</button>
            </div>
        </div>
    </div>

    <!-- Master PDF Modal -->
    <div class="modal-overlay" id="pdfModal" onclick="closePdfModal(event)">
        <div class="modal-box" style="height: 85vh;" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-size: 1.1rem; font-weight: 700;">Oral Pathology Master Compendium (PDF)</h3>
                <div style="display: flex; gap: 8px;">
                    <a href="Oral_Pathology_Master_Notes.pdf" download class="nav-btn nav-btn-primary" style="padding: 4px 10px; font-size: 0.78rem;">Download</a>
                    <button class="audio-dock-close" onclick="closePdfModal()">{ICONS["close"]}</button>
                </div>
            </div>
            <div class="modal-body" style="padding: 0;">
                <iframe src="Oral_Pathology_Master_Notes.pdf" style="width: 100%; height: 100%; border: none;"></iframe>
            </div>
        </div>
    </div>

    <!-- Spotter / Diagram Zoom Modal -->
    <div class="modal-overlay" id="modal" onclick="closeDiagramModal(event)">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 id="modalDiagramTitle" style="font-size: 1.1rem; font-weight: 700;">Microscopic Spotter Schematic</h3>
                <button class="audio-dock-close" onclick="closeDiagramModal()">{ICONS["close"]}</button>
            </div>
            <div class="modal-body" id="modalDiagramBody" style="display:flex; justify-content:center; align-items:center; background:#0f172a;">
                <!-- Injected SVG / Image -->
            </div>
        </div>
    </div>

    <!-- Application Script Bundle -->
    <script>
        const CHAPTERS = {chapters_json};
        const MATRICES = {matrices_json};
        const SPOTTERS = {spotters_json};

        let currentChapterIdx = 0;
        let activeTab = 'master';
        let currentCategory = 'All';
        let completedTopics = JSON.parse(localStorage.getItem('oral_pathology_completed_topics') || '{{}}');
        let currentFlashcardIdx = 0;
        let isFlashcardFlipped = false;

        // --- Audio & Neural Speech Synthesis Engine ---
        let availableVoices = [];
        let selectedVoice = null;
        let isAudioPlaying = false;
        let audioPlaybackSpeed = 1.0;
        let currentSpeechUtterance = null;
        let speechKeepaliveTimer = null;
        let speechTickerTimer = null;

        function initVoiceList() {{
            if (!('speechSynthesis' in window)) return;
            const updateVoices = () => {{
                availableVoices = window.speechSynthesis.getVoices().filter(v => v.lang && v.lang.startsWith('en'));
                const select = document.getElementById('audioVoiceSelect');
                if (!select) return;

                const currentVal = select.value || localStorage.getItem('oral_pathology_selected_voice') || '';
                select.innerHTML = '<option value="">Auto (Natural Studio)</option>';

                const sorted = [...availableVoices].sort((a, b) => {{
                    const aNat = a.name.includes('Natural') || a.name.includes('Online') || a.name.includes('Enhanced');
                    const bNat = b.name.includes('Natural') || b.name.includes('Online') || b.name.includes('Enhanced');
                    if (aNat && !bNat) return -1;
                    if (!aNat && bNat) return 1;
                    return a.name.localeCompare(b.name);
                }});

                sorted.forEach(v => {{
                    const opt = document.createElement('option');
                    opt.value = v.name;
                    const isPremium = v.name.includes('Natural') || v.name.includes('Online') || v.name.includes('Enhanced');
                    opt.textContent = `${{isPremium ? '✨ ' : ''}}${{v.name.replace(/Microsoft |Google /g, '')}} (${{v.lang}})`;
                    if (v.name === currentVal) opt.selected = true;
                    select.appendChild(opt);
                }});

                if (currentVal) {{
                    selectedVoice = availableVoices.find(v => v.name === currentVal) || null;
                }}
            }};

            updateVoices();
            if (window.speechSynthesis.onvoiceschanged !== undefined) {{
                window.speechSynthesis.onvoiceschanged = updateVoices;
            }}
        }}

        function onVoiceSelected(voiceName) {{
            if (!voiceName) {{
                selectedVoice = null;
                localStorage.removeItem('oral_pathology_selected_voice');
            }} else {{
                selectedVoice = availableVoices.find(v => v.name === voiceName) || null;
                localStorage.setItem('oral_pathology_selected_voice', voiceName);
            }}
            if (isAudioPlaying) {{
                speakCurrentChapterSection();
            }}
        }}

        function cleanMedicalTextForSpeech(text) {{
            if (!text) return '';
            let s = text.replace(/<[^>]+>/g, ' ');
            s = s.replace(/\|/g, ' ');
            s = s.replace(/\*\*/g, '');
            s = s.replace(/```[\s\S]*?```/g, ' ');
            s = s.replace(/`([^`]+)`/g, '$1');

            // Expand standard oral pathology abbreviations
            const expansions = [
                [/\\bOKC\\b/g, 'Odontogenic Keratocyst'],
                [/\\bKCOT\\b/g, 'Keratocystic Odontogenic Tumor'],
                [/\\bCEOT\\b/g, 'Calcifying Epithelial Odontogenic Tumor'],
                [/\\bAOT\\b/g, 'Adenomatoid Odontogenic Tumor'],
                [/\\bOPMD\\b/g, 'Oral Potentially Malignant Disorders'],
                [/\\bOSMF\\b/g, 'Oral Submucous Fibrosis'],
                [/\\bOLP\\b/g, 'Oral Lichen Planus'],
                [/\\bOSCC\\b/g, 'Oral Squamous Cell Carcinoma'],
                [/\\bAI\\b/g, 'Amelogenesis Imperfecta'],
                [/\\bDI\\b/g, 'Dentinogenesis Imperfecta'],
                [/\\bDEJ\\b/g, 'Dentinoenamel Junction'],
                [/\\bCEJ\\b/g, 'Cementoenamel Junction'],
                [/\\bBMZ\\b/g, 'Basement Membrane Zone'],
                [/\\bDIF\\b/g, 'Direct Immunofluorescence'],
                [/\\bPAS\\b/g, 'Periodic Acid Schiff'],
                [/\\bGMS\\b/g, 'Grocott Gomori Methenamine Silver'],
                [/\\bREE\\b/g, 'Reduced Enamel Epithelium'],
                [/\\bAdCC\\b/g, 'Adenoid Cystic Carcinoma'],
                [/\\bMEC\\b/g, 'Mucoepidermoid Carcinoma']
            ];

            expansions.forEach(([rx, replacement]) => {{
                s = s.replace(rx, replacement);
            }});
            return s.trim();
        }}

        function togglePlayPauseAudio() {{
            const dock = document.getElementById('masterAudioDock');
            if (dock) dock.classList.remove('hidden');

            if (!('speechSynthesis' in window)) {{
                alert('Speech synthesis is not supported in this browser.');
                return;
            }}

            if (window.speechSynthesis.paused) {{
                window.speechSynthesis.resume();
                isAudioPlaying = true;
                updateAudioUI();
            }} else if (window.speechSynthesis.speaking) {{
                window.speechSynthesis.pause();
                isAudioPlaying = false;
                updateAudioUI();
            }} else {{
                speakCurrentChapterSection();
            }}
        }}

        function speakCurrentChapterSection() {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();
            clearInterval(speechTickerTimer);
            clearInterval(speechKeepaliveTimer);

            const ch = CHAPTERS[currentChapterIdx];
            if (!ch) return;

            const titleEl = document.getElementById('audioDockTrackTitle');
            const chTitleEl = document.getElementById('audioDockChapterTitle');
            if (titleEl) titleEl.innerText = ch.title;
            if (chTitleEl) chTitleEl.innerText = ch.category;

            const textToSpeak = `${{ch.title}}. Category: ${{ch.category}}. Histopathological Pearl: ${{ch.clinical_pearl}}. ${{ch.sections.map(s => s.title + '. ' + s.content).join(' ')}}`;
            const cleanText = cleanMedicalTextForSpeech(textToSpeak);

            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.rate = audioPlaybackSpeed || 1.0;

            if (selectedVoice) {{
                utterance.voice = selectedVoice;
            }} else if (availableVoices.length > 0) {{
                const best = availableVoices.find(v => v.name.includes('Natural') || v.name.includes('Online') || v.name.includes('Enhanced')) || availableVoices[0];
                if (best) utterance.voice = best;
            }}

            const words = cleanText.split(/\\s+/).length;
            const estDurationSec = Math.max(10, (words / (150 * (audioPlaybackSpeed || 1.0))) * 60);
            let elapsedSec = 0;

            const durEl = document.getElementById('audioDuration');
            const curTimeEl = document.getElementById('audioCurrentTime');
            const scrubber = document.getElementById('audioProgressScrubber');
            if (durEl) durEl.innerText = formatTime(estDurationSec);

            speechTickerTimer = setInterval(() => {{
                if (isAudioPlaying) {{
                    elapsedSec += 0.5;
                    if (curTimeEl) curTimeEl.innerText = formatTime(elapsedSec);
                    if (scrubber && estDurationSec > 0) {{
                        scrubber.value = Math.min(100, (elapsedSec / estDurationSec) * 100);
                    }}
                }}
            }}, 500);

            // Heartbeat to prevent Chromium 15s freeze
            speechKeepaliveTimer = setInterval(() => {{
                if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {{
                    window.speechSynthesis.pause();
                    window.speechSynthesis.resume();
                }}
            }}, 12000);

            utterance.onend = () => {{
                clearInterval(speechTickerTimer);
                clearInterval(speechKeepaliveTimer);
                if (currentChapterIdx + 1 < CHAPTERS.length) {{
                    currentChapterIdx++;
                    renderChapterView();
                    speakCurrentChapterSection();
                }} else {{
                    isAudioPlaying = false;
                    updateAudioUI();
                }}
            }};

            utterance.onerror = () => {{
                clearInterval(speechTickerTimer);
                clearInterval(speechKeepaliveTimer);
                isAudioPlaying = false;
                updateAudioUI();
            }};

            window.speechSynthesis.speak(utterance);
            currentSpeechUtterance = utterance;
            isAudioPlaying = true;
            updateAudioUI();
        }}

        function setAudioPlaybackRate(rate) {{
            audioPlaybackSpeed = rate;
            document.querySelectorAll('.speed-pill').forEach(pill => {{
                const pSpeed = parseFloat(pill.getAttribute('data-speed'));
                if (Math.abs(pSpeed - rate) < 0.01) {{
                    pill.classList.add('active');
                }} else {{
                    pill.classList.remove('active');
                }}
            }});
            if (isAudioPlaying) {{
                speakCurrentChapterSection();
            }}
        }}

        function onAudioScrub(val) {{
            // Visual scrubber
        }}

        function prevAudioTrack() {{
            if (currentChapterIdx > 0) {{
                currentChapterIdx--;
                renderChapterView();
                if (isAudioPlaying) speakCurrentChapterSection();
            }}
        }}

        function nextAudioTrack() {{
            if (currentChapterIdx + 1 < CHAPTERS.length) {{
                currentChapterIdx++;
                renderChapterView();
                if (isAudioPlaying) speakCurrentChapterSection();
            }}
        }}

        function closeAudioDock() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
            }}
            clearInterval(speechTickerTimer);
            clearInterval(speechKeepaliveTimer);
            isAudioPlaying = false;
            const dock = document.getElementById('masterAudioDock');
            if (dock) dock.classList.add('hidden');
            updateAudioUI();
        }}

        function updateAudioUI() {{
            const btn = document.getElementById('audioDockPlayPauseBtn');
            const dock = document.getElementById('masterAudioDock');
            if (btn) {{
                btn.innerHTML = isAudioPlaying ? '{ICONS["pause"]}' : '{ICONS["play"]}';
            }}
            if (dock) {{
                if (isAudioPlaying) dock.classList.add('is-playing');
                else dock.classList.remove('is-playing');
            }}
        }}

        function speakVivaPearl(btn, text) {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();
            const cleanText = cleanMedicalTextForSpeech(text);
            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.rate = audioPlaybackSpeed || 1.0;
            if (selectedVoice) utterance.voice = selectedVoice;

            btn.style.color = '#c084fc';
            utterance.onend = () => {{ btn.style.color = ''; }};
            utterance.onerror = () => {{ btn.style.color = ''; }};
            window.speechSynthesis.speak(utterance);
        }}

        function formatTime(sec) {{
            const m = Math.floor(sec / 60);
            const s = Math.floor(sec % 60);
            return `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
        }}

        // --- View & Navigation Logic ---
        function renderSidebar() {{
            const query = (document.getElementById('searchInput').value || '').toLowerCase();
            const listEl = document.getElementById('sidebarTopicList');
            listEl.innerHTML = '';

            const filtered = CHAPTERS.filter(ch => {{
                const matchesCat = (currentCategory === 'All') || ch.category.toLowerCase().includes(currentCategory.toLowerCase());
                const matchesQuery = !query || ch.title.toLowerCase().includes(query) || ch.sections.some(s => s.content.toLowerCase().includes(query));
                return matchesCat && matchesQuery;
            }});

            if (filtered.length === 0) {{
                listEl.innerHTML = '<div style="padding:20px; color:var(--text-muted); text-align:center;">No matching pathological lesions found.</div>';
                return;
            }}

            filtered.forEach((ch, idx) => {{
                const originalIdx = CHAPTERS.findIndex(c => c.id === ch.id);
                const isCompleted = !!completedTopics[ch.id];
                const item = document.createElement('div');
                item.className = 'topic-item' + (originalIdx === currentChapterIdx ? ' active' : '');
                item.onclick = () => selectChapter(originalIdx);
                item.innerHTML = `
                    <div class="topic-check ${{isCompleted ? 'completed' : ''}}" onclick="event.stopPropagation(); toggleTopicComplete('${{ch.id}}')">
                        ${{isCompleted ? '{ICONS["check_circle"]}' : '{ICONS["circle"]}'}}
                    </div>
                    <div class="topic-info">
                        <div class="topic-title">${{originalIdx + 1}}. ${{ch.title}}</div>
                        <div class="topic-meta">${{ch.category}} • ${{ch.reading_time}}</div>
                    </div>
                `;
                listEl.appendChild(item);
            }});
        }}

        function selectChapter(idx) {{
            currentChapterIdx = idx;
            renderSidebar();
            renderChapterView();
            toggleMobileSidebar(false);
        }}

        function showDashboard() {{
            currentChapterIdx = -1;
            renderSidebar();
            renderDashboard();
        }}

        function renderDashboard() {{
            const main = document.getElementById('mainContent');
            const total = CHAPTERS.length;
            const completed = Object.keys(completedTopics).length;
            const remaining = total - completed;
            const pct = Math.round((completed / total) * 100);

            main.innerHTML = `
                <div class="dash-hero">
                    <div>
                        <span class="dash-badge">BDS 3RD YEAR &amp; MDS PATHOLOGY MONOGRAPH</span>
                        <h2 class="dash-title">Oral Pathology Master Exam Hub</h2>
                        <p class="dash-subtitle">15-Mark Essay Blueprints • Histopathological Criteria • Microscopic Spotter Flashcards</p>
                    </div>
                    <button class="nav-btn nav-btn-primary" onclick="selectChapter(0)">Explore Lesions →</button>
                </div>

                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-val">${{total}}</div>
                        <div class="stat-lbl">Total Topics</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-val" style="color: #a855f7;">${{completed}}</div>
                        <div class="stat-lbl">Completed</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-val" style="color: #f59e0b;">${{remaining}}</div>
                        <div class="stat-lbl">Remaining</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-val" style="color: #38bdf8;">${{pct}}%</div>
                        <div class="stat-lbl">Syllabus Ready</div>
                    </div>
                </div>

                <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 14px;">Curriculum Pathological Entities</h3>
                <div class="types-grid">
                    ${{CHAPTERS.map((ch, idx) => `
                        <div class="type-card" onclick="selectChapter(${{idx}})" style="cursor: pointer;">
                            <span class="type-card-badge">${{ch.category}}</span>
                            <div class="type-card-title">${{idx + 1}}. ${{ch.title}}</div>
                            <div class="type-card-stat">${{ch.badge}} • ${{ch.reading_time}}</div>
                            <div class="type-card-summary">${{ch.clinical_pearl}}</div>
                        </div>
                    `).join('')}}
                </div>
            `;
        }}

        function renderChapterView() {{
            if (currentChapterIdx < 0 || currentChapterIdx >= CHAPTERS.length) {{
                renderDashboard();
                return;
            }}

            const ch = CHAPTERS[currentChapterIdx];
            const main = document.getElementById('mainContent');

            main.innerHTML = `
                <div class="chapter-header">
                    <span class="chapter-top-badge">${{ch.category}} • ${{ch.badge}}</span>
                    <h2 class="chapter-title-display">${{ch.title}}</h2>
                </div>

                <div class="tab-bar-container">
                    <div class="tab-bar">
                        <button class="tab-btn ${{activeTab === 'master' ? 'active' : ''}}" onclick="switchTab('master')">
                            {ICONS["master_answer"]} 15-Mark Master Answer
                        </button>
                        <button class="tab-btn ${{activeTab === 'layman' ? 'active' : ''}}" onclick="switchTab('layman')">
                            {ICONS["layman"]} Layman's Intuition
                        </button>
                        <button class="tab-btn ${{activeTab === 'types' ? 'active' : ''}}" onclick="switchTab('types')">
                            {ICONS["dashboard"]} Histopathology Explorer
                        </button>
                        <button class="tab-btn ${{activeTab === 'diagrams' ? 'active' : ''}}" onclick="switchTab('diagrams')">
                            {ICONS["diagrams"]} Microscopic Spotters
                        </button>
                        <button class="tab-btn ${{activeTab === 'viva' ? 'active' : ''}}" onclick="switchTab('viva')">
                            {ICONS["viva"]} Examiner Viva Pearls
                        </button>
                        <button class="tab-btn ${{activeTab === 'quiz' ? 'active' : ''}}" onclick="switchTab('quiz')">
                            {ICONS["quiz"]} Active Recall Flashcards
                        </button>
                        <button class="tab-btn ${{activeTab === 'exam' ? 'active' : ''}}" onclick="switchTab('exam')">
                            {ICONS["cheat_sheet"]} Exam Rubric Simulator
                        </button>
                        <button class="tab-btn ${{activeTab === 'notes' ? 'active' : ''}}" onclick="switchTab('notes')">
                            {ICONS["notes"]} My Pathology Notes
                        </button>
                    </div>
                </div>

                <div id="tabContentContainer">
                    ${{getTabHTML(ch, activeTab)}}
                </div>
            `;
        }}

        function switchTab(tab) {{
            activeTab = tab;
            document.querySelectorAll('.tab-btn').forEach(btn => {{
                if (btn.innerText.toLowerCase().includes(tab.toLowerCase())) btn.classList.add('active');
                else btn.classList.remove('active');
            }});
            document.querySelectorAll('.mobile-bottom-tab').forEach(btn => {{
                if (btn.innerText.toLowerCase().includes(tab.toLowerCase())) btn.classList.add('active');
                else btn.classList.remove('active');
            }});

            const ch = CHAPTERS[currentChapterIdx];
            const container = document.getElementById('tabContentContainer');
            if (container && ch) {{
                container.innerHTML = getTabHTML(ch, tab);
            }}
        }}

        function getTabHTML(ch, tab) {{
            if (tab === 'master') {{
                return `
                    <div class="master-essay-content">
                        <div class="pearl-card">
                            <strong style="color: var(--accent-primary);">Histopathological Pearl:</strong> ${{ch.clinical_pearl}}
                        </div>
                        ${{ch.sections.map(sec => `
                            <div class="essay-section-card">
                                <div class="essay-section-header">
                                    <h3 class="essay-section-title">${{sec.title}}</h3>
                                </div>
                                <div class="essay-body">${{parseMarkdown(sec.content)}}</div>
                            </div>
                        `).join('')}}
                    </div>
                `;
            }} else if (tab === 'layman') {{
                const layman = ch.analogy || {{ title: 'Pathological Intuition', analogy: ch.clinical_pearl }};
                return `
                    <div class="master-essay-content">
                        <div class="layman-card">
                            <div class="layman-header">
                                <span class="layman-badge">INTUITIVE PATHOLOGY ANALOGY</span>
                                <h3 class="layman-title">${{layman.title}}</h3>
                            </div>
                            <div class="layman-body">${{layman.analogy}}</div>
                        </div>
                    </div>
                `;
            }} else if (tab === 'types') {{
                const cls = ch.classification;
                return `
                    <div>
                        <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 14px;">${{cls.title}}</h3>
                        <div class="types-grid">
                            ${{cls.types.map(t => `
                                <div class="type-card">
                                    <span class="type-card-badge">${{t.badge}}</span>
                                    <div class="type-card-title">${{t.name}}</div>
                                    <div class="type-card-stat">${{t.hemodynamics}}</div>
                                    <div class="type-card-summary">${{t.summary}}</div>
                                </div>
                            `).join('')}}
                        </div>
                    </div>
                `;
            }} else if (tab === 'diagrams') {{
                return `
                    <div>
                        <div class="diagram-container">
                            <div class="diagram-title">${{ch.title}}: Vector Microscopic Spotter &amp; Histology Schematic</div>
                            <div class="diagram-viewer-box" onclick="openDiagramModal('${{ch.id}}')">
                                ${{ch.schematic_svg}}
                            </div>
                            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 10px; text-align: right;">Click diagram to expand to full-screen inspection mode</div>
                        </div>
                    </div>
                `;
            }} else if (tab === 'viva') {{
                return `
                    <div class="master-essay-content">
                        <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 16px;">Examiner Viva Voce High-Yield Pearls</h3>
                        ${{ch.viva_questions.map((q, idx) => `
                            <div class="viva-item">
                                <div class="viva-q">
                                    <span>Q${{idx + 1}}: ${{q}}</span>
                                    <button class="viva-speaker-btn" onclick="speakVivaPearl(this, '${{q.replace(/'/g, "\\'")}}')">
                                        {ICONS["volume"]}
                                    </button>
                                </div>
                                <button class="viva-reveal-btn" onclick="toggleVivaAnswer(this)">Tap to Reveal Answer</button>
                                <div class="viva-ans">
                                    <strong>Pathognomonic Answer:</strong> ${{ch.flashcards[idx] ? ch.flashcards[idx].a : ch.clinical_pearl}}
                                </div>
                            </div>
                        `).join('')}}
                    </div>
                `;
            }} else if (tab === 'quiz') {{
                currentFlashcardIdx = 0;
                isFlashcardFlipped = false;
                const card = ch.flashcards[0] || {{ q: 'No flashcard available.', a: '' }};
                return `
                    <div class="flashcard-wrap">
                        <div class="flashcard" id="activeFlashcard" onclick="flipFlashcard()">
                            <span class="flashcard-tag" id="flashcardTag">QUESTION (CARD 1 OF ${{ch.flashcards.length}})</span>
                            <div class="flashcard-text" id="flashcardText">${{card.q}}</div>
                            <span class="flashcard-instruction">Click anywhere to flip</span>
                        </div>
                        <div class="flashcard-controls">
                            <button class="nav-btn" onclick="prevFlashcard()">← Previous</button>
                            <button class="nav-btn nav-btn-primary" onclick="nextFlashcard()">Next Card →</button>
                        </div>
                    </div>
                `;
            }} else if (tab === 'exam') {{
                return `
                    <div class="master-essay-content">
                        <div class="exam-sim-card">
                            <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">25-Minute Timed University Exam Simulator</h3>
                            <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 20px;">Evaluate your structured 15-mark essay against the university examiner 10-point scoring matrix.</p>
                            <div class="rubric-row">
                                <div class="rubric-info">
                                    <h4>1. Definition, Origin &amp; WHO Classification (2 Marks)</h4>
                                    <p>Exact cell of origin, embryonic tissue remnants, and standard WHO classification table.</p>
                                </div>
                                <div class="rubric-slider"><input type="range" min="0" max="10" value="8" oninput="updateRubricScore()"></div>
                            </div>
                            <div class="rubric-row">
                                <div class="rubric-info">
                                    <h4>2. Pathogenesis &amp; Molecular Genetics (3 Marks)</h4>
                                    <p>Mutations (BRAF, PTCH1, GNAS, TP53), signaling pathways, and Layman's explanation.</p>
                                </div>
                                <div class="rubric-slider"><input type="range" min="0" max="10" value="8" oninput="updateRubricScore()"></div>
                            </div>
                            <div class="rubric-row">
                                <div class="rubric-info">
                                    <h4>3. Clinical &amp; Radiographic Hallmarks (3 Marks)</h4>
                                    <p>Age, sex, site predilection, expansion pattern (BL vs AP), and radiographic multilocularity.</p>
                                </div>
                                <div class="rubric-slider"><input type="range" min="0" max="10" value="8" oninput="updateRubricScore()"></div>
                            </div>
                            <div class="rubric-row">
                                <div class="rubric-info">
                                    <h4>4. Pathognomonic Histopathology (4 Marks)</h4>
                                    <p>Detailed architectural pattern, cell morphology, special stains, and DIF findings.</p>
                                </div>
                                <div class="rubric-slider"><input type="range" min="0" max="10" value="9" oninput="updateRubricScore()"></div>
                            </div>
                            <div class="rubric-row">
                                <div class="rubric-info">
                                    <h4>5. Management &amp; Recurrence Risk (3 Marks)</h4>
                                    <p>Enucleation vs resection margins, Carnoy's solution, and long-term surveillance protocol.</p>
                                </div>
                                <div class="rubric-slider"><input type="range" min="0" max="10" value="8" oninput="updateRubricScore()"></div>
                            </div>
                            <div style="margin-top: 24px; display: flex; justify-content: space-between; align-items: center;">
                                <div style="font-size: 1.1rem; font-weight: 700;">Simulated Exam Score: <span id="examScoreTotal" style="color: var(--accent-primary);">12.5 / 15 Marks (Honors)</span></div>
                                <button class="nav-btn nav-btn-primary" onclick="alert('Score calculated based on 10-point university rubric standard.')">Save Evaluation</button>
                            </div>
                        </div>
                    </div>
                `;
            }} else if (tab === 'notes') {{
                const savedNotes = localStorage.getItem('oral_pathology_notes_' + ch.id) || '';
                return `
                    <div class="master-essay-content">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <h3 style="font-size: 1.2rem; font-weight: 700;">My Pathology Notes</h3>
                            <span id="notesStatus" style="font-size: 0.78rem; color: var(--accent-primary);">Auto-saved locally</span>
                        </div>
                        <textarea class="notes-textarea" id="notesTextarea" placeholder="Type chairside microscopic notes, mnemonics, or revision reminders for this lesion..." oninput="saveTopicNotes('${{ch.id}}', this.value)">${{savedNotes}}</textarea>
                    </div>
                `;
            }}
            return '';
        }}

        function parseMarkdown(md) {{
            if (!md) return '';
            let html = md
                .replace(/^### (.*$)/gim, '<h4>$1</h4>')
                .replace(/^## (.*$)/gim, '<h3 style="font-size:1.15rem; font-weight:700; margin:18px 0 8px 0; color:var(--text-primary);">$1</h3>')
                .replace(/^# (.*$)/gim, '<h2 style="font-size:1.3rem; font-weight:800; margin:20px 0 10px 0; color:var(--text-primary);">$1</h2>')
                .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong style="color:var(--text-primary);">$1</strong>')
                .replace(/\\*(.*?)\\*/gim, '<em>$1</em>')
                .replace(/```([\\s\\S]*?)```/gim, '<pre>$1</pre>')
                .replace(/^\\* (.*$)/gim, '<li>$1</li>')
                .replace(/\\n/gim, '<br>');
            return html;
        }}

        function toggleTopicComplete(chId) {{
            if (completedTopics[chId]) delete completedTopics[chId];
            else completedTopics[chId] = true;
            localStorage.setItem('oral_pathology_completed_topics', JSON.stringify(completedTopics));
            renderSidebar();
        }}

        function onSearchInput() {{
            renderSidebar();
        }}

        function setCategoryFilter(cat) {{
            currentCategory = cat;
            document.querySelectorAll('#categoryPillBar .filter-chip').forEach(btn => {{
                if (btn.innerText.toLowerCase().includes(cat.toLowerCase()) || (cat === 'All' && btn.innerText.includes('All'))) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});
            renderSidebar();
        }}

        function toggleMobileSidebar(force) {{
            const sb = document.getElementById('sidebar');
            if (force !== undefined) {{
                if (force) sb.classList.add('open');
                else sb.classList.remove('open');
            }} else {{
                sb.classList.toggle('open');
            }}
        }}

        function toggleVivaAnswer(btn) {{
            const ans = btn.nextElementSibling;
            if (ans) {{
                ans.classList.toggle('revealed');
                btn.innerText = ans.classList.contains('revealed') ? 'Hide Answer' : 'Tap to Reveal Answer';
            }}
        }}

        function flipFlashcard() {{
            const ch = CHAPTERS[currentChapterIdx];
            if (!ch || !ch.flashcards || ch.flashcards.length === 0) return;
            const card = ch.flashcards[currentFlashcardIdx];
            isFlashcardFlipped = !isFlashcardFlipped;

            const textEl = document.getElementById('flashcardText');
            const tagEl = document.getElementById('flashcardTag');
            if (isFlashcardFlipped) {{
                textEl.innerText = card.a;
                tagEl.innerText = `ANSWER (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                tagEl.style.color = '#c084fc';
            }} else {{
                textEl.innerText = card.q;
                tagEl.innerText = `QUESTION (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                tagEl.style.color = '';
            }}
        }}

        function prevFlashcard() {{
            const ch = CHAPTERS[currentChapterIdx];
            if (!ch || !ch.flashcards) return;
            if (currentFlashcardIdx > 0) {{
                currentFlashcardIdx--;
                isFlashcardFlipped = false;
                const card = ch.flashcards[currentFlashcardIdx];
                document.getElementById('flashcardText').innerText = card.q;
                document.getElementById('flashcardTag').innerText = `QUESTION (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                document.getElementById('flashcardTag').style.color = '';
            }}
        }}

        function nextFlashcard() {{
            const ch = CHAPTERS[currentChapterIdx];
            if (!ch || !ch.flashcards) return;
            if (currentFlashcardIdx + 1 < ch.flashcards.length) {{
                currentFlashcardIdx++;
                isFlashcardFlipped = false;
                const card = ch.flashcards[currentFlashcardIdx];
                document.getElementById('flashcardText').innerText = card.q;
                document.getElementById('flashcardTag').innerText = `QUESTION (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                document.getElementById('flashcardTag').style.color = '';
            }}
        }}

        function saveTopicNotes(chId, val) {{
            localStorage.setItem('oral_pathology_notes_' + chId, val);
            const status = document.getElementById('notesStatus');
            if (status) status.innerText = 'Saved ' + new Date().toLocaleTimeString();
        }}

        function updateRubricScore() {{
            const sliders = document.querySelectorAll('.rubric-slider input');
            let total = 0;
            sliders.forEach(s => total += parseInt(s.value));
            const scaled = ((total / (sliders.length * 10)) * 15).toFixed(1);
            document.getElementById('examScoreTotal').innerText = `${{scaled}} / 15 Marks (${{scaled >= 11 ? 'Honors' : 'Pass'}})`;
        }}

        function openPdfModal() {{
            document.getElementById('pdfModal').style.display = 'flex';
        }}
        function closePdfModal() {{
            document.getElementById('pdfModal').style.display = 'none';
        }}

        function openDiagramModal(chId) {{
            const ch = CHAPTERS.find(c => c.id === chId) || CHAPTERS[currentChapterIdx];
            document.getElementById('modalDiagramTitle').innerText = ch.title + ': Full Microscopic Schematic';
            document.getElementById('modalDiagramBody').innerHTML = ch.schematic_svg;
            document.getElementById('modal').style.display = 'flex';
        }}
        function closeDiagramModal() {{
            document.getElementById('modal').style.display = 'none';
        }}

        function toggleTheme() {{
            document.body.classList.toggle('dark');
            const isDark = document.body.classList.contains('dark');
            localStorage.setItem('oral_pathology_theme', isDark ? 'dark' : 'light');
            document.getElementById('themeToggleBtn').innerHTML = isDark ? '{ICONS["sun"]}' : '{ICONS["moon"]}';
        }}

        // Keyboard Shortcuts
        window.addEventListener('keydown', e => {{
            if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {{
                e.preventDefault();
                const search = document.getElementById('searchInput');
                if (search) search.focus();
            }} else if (e.key === 'Escape') {{
                closePdfModal();
                closeDiagramModal();
                toggleMobileSidebar(false);
            }}
        }});

        // Initialization
        if (localStorage.getItem('oral_pathology_theme') === 'dark') {{
            document.body.classList.add('dark');
            document.getElementById('themeToggleBtn').innerHTML = '{ICONS["sun"]}';
        }}
        initVoiceList();
        renderSidebar();
        renderChapterView();
    </script>
</body>
</html>
"""
    return html

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Loaded {len(ALL_CHAPTERS)} Oral Pathology chapters.")

    # 1. Generate Markdown
    md_path = os.path.join(base_dir, "Oral_Pathology_Master_Notes.md")
    print(f"Generating {md_path}...")
    md_content = generate_markdown(ALL_CHAPTERS)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Markdown generated: {len(md_content)} characters.")

    # 2. Generate Print-ready HTML
    print_html_path = os.path.join(base_dir, "Oral_Pathology_Master_Notes.html")
    print(f"Generating {print_html_path}...")
    print_html_content = generate_print_html(ALL_CHAPTERS)
    with open(print_html_path, "w", encoding="utf-8") as f:
        f.write(print_html_content)
    print(f"Print HTML generated: {len(print_html_content)} characters.")

    # 3. Generate Interactive Study App (index.html)
    app_html_path = os.path.join(base_dir, "index.html")
    print(f"Generating {app_html_path}...")
    app_html_content = generate_interactive_dashboard(ALL_CHAPTERS)
    with open(app_html_path, "w", encoding="utf-8") as f:
        f.write(app_html_content)
    print(f"Interactive App HTML generated: {len(app_html_content)} characters.")

    # 4. Compile PDF via Headless Edge
    pdf_path = os.path.join(base_dir, "Oral_Pathology_Master_Notes.pdf")
    print(f"Compiling typeset PDF to {pdf_path}...")
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "msedge"
    ]
    edge_bin = None
    for ep in edge_paths:
        if os.path.exists(ep) or ep == "msedge":
            edge_bin = ep
            break

    if edge_bin:
        cmd = [
            edge_bin,
            "--headless",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={pdf_path}",
            f"file:///{print_html_path.replace(os.sep, '/')}"
        ]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
            if os.path.exists(pdf_path):
                size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
                print(f"PDF successfully compiled: {size_mb:.2f} MB")
            else:
                print("PDF compilation completed without file output.")
        except Exception as e:
            print(f"Error compiling PDF: {e}")
    else:
        print("Microsoft Edge not found for headless PDF compilation.")

if __name__ == "__main__":
    main()

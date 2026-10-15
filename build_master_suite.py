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
from content.caries_and_developmental import CHAPTERS as c2
from content.salivary_and_neoplasms import CHAPTERS as c3
from content.infections_blood_bone_forensic import CHAPTERS as c4
from content.formatter import ICONS, FAVICON_SVG, clean_latex, parse_markdown_to_html
from content.interactive_data import COMPARISON_MATRICES, SPOTTER_CARDS, VIVA_QUIZ

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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {{
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {{
        content: counter(page);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #78350f;
    }}
    @bottom-left {{
        content: "Oral Pathology & Microbiology Master Monograph | University Exam Preparation";
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #78350f;
    }}
}}

*, *::before, *::after {{
    box-sizing: border-box;
}}

body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    line-height: 1.6;
    font-size: 10pt;
    margin: 0;
    padding: 0;
}}

.cover-page {{
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px;
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 50%, #fde68a 100%);
    border: 4px double #d97706;
}}

.cover-badge {{
    display: inline-block;
    background: #d97706;
    color: #ffffff;
    font-weight: 700;
    font-size: 10pt;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 6px 16px;
    border-radius: 999px;
    margin-bottom: 24px;
}}

.cover-title {{
    font-size: 26pt;
    font-weight: 800;
    color: #92400e;
    line-height: 1.2;
    margin: 0 0 16px 0;
}}

.cover-subtitle {{
    font-size: 13pt;
    color: #b45309;
    max-width: 650px;
    margin: 0 0 32px 0;
    line-height: 1.5;
}}

.cover-meta {{
    font-size: 9.5pt;
    color: #78350f;
    border-top: 1px solid #fcd34d;
    padding-top: 20px;
    display: flex;
    gap: 30px;
}}

.toc-page {{
    page-break-after: always;
    padding: 20px 0;
}}

.toc-title {{
    font-size: 18pt;
    font-weight: 800;
    color: #92400e;
    border-bottom: 2px solid #d97706;
    padding-bottom: 8px;
    margin-bottom: 20px;
}}

.toc-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px 24px;
}}

.toc-item {{
    font-size: 9pt;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dotted #cbd5e1;
    padding-bottom: 4px;
}}

.chapter-container {{
    page-break-before: always;
    margin-bottom: 30px;
}}

.chapter-header {{
    background: #fffbeb;
    border-left: 6px solid #d97706;
    padding: 16px 20px;
    margin-bottom: 20px;
    border-radius: 0 8px 8px 0;
}}

.chapter-cat {{
    font-size: 8.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #d97706;
    margin-bottom: 4px;
}}

.chapter-title {{
    font-size: 17pt;
    font-weight: 800;
    color: #92400e;
    margin: 0 0 8px 0;
}}

.chapter-meta-line {{
    font-size: 8.5pt;
    color: #64748b;
}}

.keypoints-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 20px;
}}

.keypoints-title {{
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
}}

.keypoints-list {{
    margin: 0;
    padding-left: 20px;
    font-size: 9pt;
}}

.keypoints-list li {{
    margin-bottom: 6px;
}}

.clinical-pearl-box {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #d97706;
    border-radius: 6px;
    padding: 12px 16px;
    margin-bottom: 20px;
    font-size: 9pt;
    color: #92400e;
}}

.clinical-pearl-box strong {{
    color: #b45309;
}}

.section-block {{
    margin-bottom: 18px;
}}

.section-title {{
    font-size: 12pt;
    font-weight: 700;
    color: #92400e;
    border-bottom: 1px solid #fcd34d;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
}}

.section-content {{
    font-size: 9.5pt;
    line-height: 1.6;
    color: #334155;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.5pt;
}}

th, td {{
    border: 1px solid #e2e8f0;
    padding: 6px 10px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: #fffbeb;
    color: #92400e;
    font-weight: 700;
}}

tr:nth-child(even) td {{
    background-color: #f8fafc;
}}

pre, code {{
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8pt;
}}

pre {{
    background-color: #0f172a;
    color: #f1f5f9;
    padding: 12px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 12px 0;
    line-height: 1.4;
}}

h1, h2, h3, h4, h5, h6 {{
    page-break-after: avoid;
}}

table, pre, .keypoints-box, .clinical-pearl-box {{
    page-break-inside: avoid;
}}
</style>
</head>
<body>
    <div class="cover-page">
        <div class="cover-badge">University Exam Preparation Monograph</div>
        <h1 class="cover-title">ORAL PATHOLOGY & MICROBIOLOGY</h1>
        <div class="cover-subtitle">Complete 15-Mark Essay Models, Clinical Histopathological Diagnostic Criteria, Microscopic Spotters & Forensic Odontology Suite</div>
        <div class="cover-meta">
            <div><strong>Curriculum:</strong> BDS 3rd Year / MS Exam Standards</div>
            <div><strong>Chapters:</strong> 20 Comprehensive Monographic Chapters</div>
            <div><strong>Format:</strong> 100% Copyable & Searchable PDF</div>
        </div>
    </div>

    <div class="toc-page">
        <div class="toc-title">Curriculum Table of Contents</div>
        <div class="toc-grid">
""")

    for i, ch in enumerate(chapters, 1):
        html_parts.append(f"""
            <div class="toc-item">
                <span><strong>{i}.</strong> {ch['title']}</span>
                <span>Ch {i}</span>
            </div>
        """)

    html_parts.append("""
        </div>
    </div>
""")

    for i, ch in enumerate(chapters, 1):
        html_parts.append(f"""
        <div class="chapter-container">
            <div class="chapter-header">
                <div class="chapter-cat">{ch['category']} • Chapter {i}</div>
                <h2 class="chapter-title">{ch['title']}</h2>
                <div class="chapter-meta-line">Standard: {ch['badge']} | Estimated Reading Time: {ch['reading_time']}</div>
            </div>

            <div class="keypoints-box">
                <div class="keypoints-title">Core High-Yield Exam Facts</div>
                <ul class="keypoints-list">
        """)
        for kp in ch["key_points"]:
            html_parts.append(f"<li>{parse_markdown_to_html(clean_latex(kp))}</li>")

        html_parts.append(f"""
                </ul>
            </div>

            <div class="clinical-pearl-box">
                <strong>Clinical & Histopathological Pearl:</strong> {parse_markdown_to_html(clean_latex(ch['clinical_pearl']))}
            </div>
        """)

        for sec in ch["sections"]:
            html_parts.append(f"""
            <div class="section-block">
                <div class="section-title">{sec['title']}</div>
                <div class="section-content">{parse_markdown_to_html(clean_latex(sec['content']))}</div>
            </div>
            """)

        html_parts.append("</div>")

    html_parts.append("""
</body>
</html>
""")
    return "".join(html_parts)

def generate_interactive_dashboard(chapters):
    chapters_json = json.dumps(chapters)
    matrices_json = json.dumps(COMPARISON_MATRICES)
    spotters_json = json.dumps(SPOTTER_CARDS)
    quiz_json = json.dumps(VIVA_QUIZ)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="{FAVICON_SVG}">
<title>Oral Pathology & Microbiology | Interactive Study Portal & Exam Suite</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {{
    --bg-dark: #09090b;
    --surface-dark: #121215;
    --card-dark: #18181b;
    --border-dark: #27272a;
    --text-primary: #f4f4f5;
    --text-secondary: #a1a1aa;
    --text-muted: #71717a;
    --primary: #d97706;
    --primary-hover: #b45309;
    --primary-light: rgba(217, 119, 6, 0.15);
    --accent: #f59e0b;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-primary);
    line-height: 1.5;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}}

/* Top Navigation Bar */
.topbar {{
    background-color: var(--surface-dark);
    border-bottom: 1px solid var(--border-dark);
    padding: 12px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-shrink: 0;
}}

.logo-group {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.logo-badge {{
    background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
    color: #fff;
    font-weight: 800;
    font-size: 0.85rem;
    padding: 4px 10px;
    border-radius: 6px;
    letter-spacing: 0.5px;
}}

.logo-title {{
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text-primary);
}}

.logo-subtitle {{
    font-size: 0.8rem;
    color: var(--text-muted);
}}

.nav-tabs {{
    display: flex;
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 8px;
    padding: 4px;
    gap: 4px;
}}

.nav-tab {{
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-family: inherit;
    font-size: 0.85rem;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
}}

.nav-tab.active {{
    background-color: var(--primary);
    color: #ffffff;
}}

.top-actions {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.pdf-download-btn {{
    display: flex;
    align-items: center;
    gap: 6px;
    background-color: var(--card-dark);
    color: var(--accent);
    border: 1px solid var(--border-dark);
    font-family: inherit;
    font-size: 0.85rem;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 6px;
    text-decoration: none;
    transition: all 0.2s ease;
}}

.pdf-download-btn:hover {{
    background-color: var(--primary-light);
    border-color: var(--primary);
}}

/* Main App Workspace */
.main-workspace {{
    flex: 1;
    display: flex;
    overflow: hidden;
}}

/* Left Sidebar - Topic Explorer */
.sidebar {{
    width: 380px;
    background-color: var(--surface-dark);
    border-right: 1px solid var(--border-dark);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
}}

.search-box-container {{
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-dark);
}}

.search-input {{
    width: 100%;
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.85rem;
    padding: 8px 12px;
    border-radius: 6px;
    outline: none;
    transition: border-color 0.2s;
}}

.search-input:focus {{
    border-color: var(--primary);
}}

.category-filter-pills {{
    padding: 8px 16px;
    display: flex;
    gap: 6px;
    overflow-x: auto;
    border-bottom: 1px solid var(--border-dark);
}}

.category-pill {{
    background-color: var(--card-dark);
    color: var(--text-secondary);
    border: 1px solid var(--border-dark);
    border-radius: 999px;
    padding: 4px 10px;
    font-size: 0.72rem;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
}}

.category-pill.active {{
    background-color: var(--primary-light);
    color: var(--accent);
    border-color: var(--primary);
}}

.topic-list {{
    flex: 1;
    overflow-y: auto;
    padding: 8px;
}}

.topic-card {{
    background-color: var(--card-dark);
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 8px;
    cursor: pointer;
    transition: all 0.15s ease;
}}

.topic-card:hover {{
    border-color: var(--border-dark);
    background-color: rgba(39, 39, 42, 0.6);
}}

.topic-card.active {{
    border-color: var(--primary);
    background-color: var(--primary-light);
}}

.topic-card-category {{
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--accent);
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}}

.topic-card-title {{
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 6px;
    line-height: 1.35;
}}

.topic-card-meta {{
    font-size: 0.75rem;
    color: var(--text-muted);
    display: flex;
    justify-content: space-between;
}}

/* Right Panel - Essay Viewer */
.content-viewer {{
    flex: 1;
    overflow-y: auto;
    padding: 24px 36px 60px 36px;
    background-color: var(--bg-dark);
}}

.viewer-header {{
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 24px;
}}

.viewer-cat {{
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}}

.viewer-title {{
    font-size: 1.6rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 12px;
    line-height: 1.25;
}}

.viewer-badge-row {{
    display: flex;
    gap: 10px;
    margin-bottom: 16px;
}}

.badge-item {{
    font-size: 0.75rem;
    font-weight: 600;
    background-color: var(--surface-dark);
    border: 1px solid var(--border-dark);
    color: var(--text-secondary);
    padding: 4px 10px;
    border-radius: 6px;
}}

.clinical-pearl-banner {{
    background: linear-gradient(135deg, rgba(217, 119, 6, 0.15) 0%, rgba(180, 83, 9, 0.08) 100%);
    border-left: 4px solid var(--primary);
    border-radius: 6px;
    padding: 14px 18px;
    font-size: 0.88rem;
    color: #fde68a;
    line-height: 1.5;
}}

.keypoints-section {{
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 24px;
}}

.keypoints-heading {{
    font-size: 0.95rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
}}

.keypoints-ul {{
    padding-left: 20px;
    color: var(--text-secondary);
    font-size: 0.88rem;
}}

.keypoints-ul li {{
    margin-bottom: 8px;
}}

.section-card {{
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 20px;
}}

.sec-title {{
    font-size: 1.15rem;
    font-weight: 700;
    color: #ffffff;
    border-bottom: 1px solid var(--border-dark);
    padding-bottom: 8px;
    margin-bottom: 14px;
}}

.sec-body {{
    color: var(--text-secondary);
    font-size: 0.92rem;
    line-height: 1.65;
}}

.sec-body table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 0.84rem;
}}

.sec-body th, .sec-body td {{
    border: 1px solid var(--border-dark);
    padding: 8px 12px;
    text-align: left;
}}

.sec-body th {{
    background-color: var(--surface-dark);
    color: var(--accent);
    font-weight: 700;
}}

.sec-body tr:nth-child(even) td {{
    background-color: rgba(255, 255, 255, 0.02);
}}

.sec-body pre {{
    background-color: #0c0a09;
    border: 1px solid var(--border-dark);
    color: #f59e0b;
    padding: 14px;
    border-radius: 6px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    line-height: 1.45;
    margin: 14px 0;
}}

/* Interactive Lab View */
.lab-container {{
    display: none;
    flex: 1;
    overflow-y: auto;
    padding: 30px;
    background-color: var(--bg-dark);
}}

.lab-section-title {{
    font-size: 1.3rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}}

.calculator-card {{
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 30px;
}}

.calc-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 20px;
}}

.calc-field {{
    display: flex;
    flex-direction: column;
    gap: 6px;
}}

.calc-label {{
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-secondary);
}}

.calc-select {{
    background-color: var(--surface-dark);
    border: 1px solid var(--border-dark);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.85rem;
    padding: 8px 12px;
    border-radius: 6px;
    outline: none;
}}

.calc-select:focus {{
    border-color: var(--primary);
}}

.calc-result-banner {{
    background: linear-gradient(135deg, rgba(217, 119, 6, 0.2) 0%, rgba(180, 83, 9, 0.1) 100%);
    border: 1px solid var(--primary);
    border-radius: 8px;
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.calc-result-number {{
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--accent);
}}

/* Spotters Flashcards */
.spotter-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 18px;
    margin-bottom: 36px;
}}

.spotter-card {{
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 10px;
    padding: 18px;
    transition: transform 0.2s, border-color 0.2s;
}}

.spotter-card:hover {{
    transform: translateY(-2px);
    border-color: var(--primary);
}}

.spotter-header {{
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 6px;
}}

.spotter-title {{
    font-size: 1.05rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}}

.spotter-condition {{
    background-color: var(--surface-dark);
    border: 1px solid var(--border-dark);
    color: #fde68a;
    font-weight: 600;
    font-size: 0.85rem;
    padding: 4px 10px;
    border-radius: 6px;
    margin-bottom: 12px;
    display: inline-block;
}}

.spotter-features {{
    padding-left: 18px;
    font-size: 0.82rem;
    color: var(--text-secondary);
    margin-bottom: 12px;
}}

.spotter-features li {{
    margin-bottom: 4px;
}}

.spotter-viva {{
    background-color: rgba(217, 119, 6, 0.1);
    border-left: 3px solid var(--primary);
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 0.78rem;
    color: #fcd34d;
}}

/* Quiz Engine */
.quiz-card {{
    background-color: var(--card-dark);
    border: 1px solid var(--border-dark);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
}}

.quiz-q {{
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 16px;
}}

.quiz-opts {{
    display: flex;
    flex-direction: column;
    gap: 10px;
}}

.quiz-opt {{
    background-color: var(--surface-dark);
    border: 1px solid var(--border-dark);
    color: var(--text-secondary);
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 0.88rem;
    cursor: pointer;
    transition: all 0.15s ease;
    text-align: left;
    font-family: inherit;
}}

.quiz-opt:hover {{
    border-color: var(--primary);
    color: var(--text-primary);
}}

.quiz-opt.correct {{
    background-color: rgba(34, 197, 94, 0.2);
    border-color: #22c55e;
    color: #86efac;
}}

.quiz-opt.incorrect {{
    background-color: rgba(239, 68, 68, 0.2);
    border-color: #ef4444;
    color: #fca5a5;
}}

.quiz-exp {{
    margin-top: 12px;
    font-size: 0.82rem;
    color: #fcd34d;
    background-color: var(--surface-dark);
    padding: 10px 14px;
    border-radius: 6px;
    display: none;
}}
</style>
</head>
<body>

    <!-- Top Navigation -->
    <header class="topbar">
        <div class="logo-group">
            <span class="logo-badge">ORAL PATH</span>
            <div>
                <div class="logo-title">Oral Pathology & Microbiology</div>
                <div class="logo-subtitle">BDS 3rd Year University Exam Preparation Portal</div>
            </div>
        </div>

        <nav class="nav-tabs">
            <button class="nav-tab active" id="tabCurriculum" onclick="switchTab('curriculum')">Curriculum & 15-Mark Essays</button>
            <button class="nav-tab" id="tabLab" onclick="switchTab('lab')">Diagnostic Lab, Spotters & Quiz</button>
        </nav>

        <div class="top-actions">
            <a href="Oral_Pathology_Master_Notes.pdf" class="pdf-download-btn" target="_blank" download>
                <span>Download Typeset PDF</span>
            </a>
        </div>
    </header>

    <!-- Main Workspace -->
    <main class="main-workspace" id="curriculumWorkspace">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="search-box-container">
                <input type="text" class="search-input" id="topicSearch" placeholder="Search 20 chapters, histological signs, cysts..." oninput="filterTopics()">
            </div>
            <div class="category-filter-pills" id="categoryPills">
                <button class="category-pill active" onclick="filterCategory('All')">All (20)</button>
                <button class="category-pill" onclick="filterCategory('Odontogenic')">Odontogenic</button>
                <button class="category-pill" onclick="filterCategory('Caries')">Caries & Development</button>
                <button class="category-pill" onclick="filterCategory('Salivary')">Salivary & OPMD</button>
                <button class="category-pill" onclick="filterCategory('Infections')">Infections & Bone</button>
                <button class="category-pill" onclick="filterCategory('Forensic')">Forensic</button>
            </div>
            <div class="topic-list" id="topicList"></div>
        </aside>

        <!-- Right Content Viewer -->
        <section class="content-viewer" id="contentViewer"></section>
    </main>

    <!-- Interactive Lab Workspace -->
    <main class="lab-container" id="labWorkspace">
        <!-- Gustafson Age Calculator -->
        <div class="lab-section-title">Gustafson's Dental Age Estimation Calculator (1950)</div>
        <div class="calculator-card">
            <div style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:16px;">
                Formula: <strong>Age = 11.43 + 4.56 &times; X</strong>, where Total Score <em>X = A + P + S + C + R + T</em> (Standard error &plusmn;3.63 years).
            </div>
            <div class="calc-grid">
                <div class="calc-field">
                    <label class="calc-label">Attrition (A)</label>
                    <select class="calc-select" id="calcA" onchange="calculateGustafson()">
                        <option value="0">A0: No wear</option>
                        <option value="1">A1: Enamel wear only</option>
                        <option value="2">A2: Dentin exposed</option>
                        <option value="3">A3: Pulp chamber exposed</option>
                    </select>
                </div>
                <div class="calc-field">
                    <label class="calc-label">Periodontitis (P)</label>
                    <select class="calc-select" id="calcP" onchange="calculateGustafson()">
                        <option value="0">P0: Normal attachment</option>
                        <option value="1">P1: Early attachment loss</option>
                        <option value="2">P2: Loss along 1/3 root</option>
                        <option value="3">P3: Loss along >2/3 root</option>
                    </select>
                </div>
                <div class="calc-field">
                    <label class="calc-label">Secondary Dentin (S)</label>
                    <select class="calc-select" id="calcS" onchange="calculateGustafson()">
                        <option value="0">S0: Normal pulp chamber</option>
                        <option value="1">S1: Slightly reduced pulp</option>
                        <option value="2">S2: Moderately reduced</option>
                        <option value="3">S3: Pulp chamber closed</option>
                    </select>
                </div>
                <div class="calc-field">
                    <label class="calc-label">Cementum Apposition (C)</label>
                    <select class="calc-select" id="calcC" onchange="calculateGustafson()">
                        <option value="0">C0: Normal cementum</option>
                        <option value="1">C1: Slightly thickened</option>
                        <option value="2">C2: Marked hypercementosis</option>
                        <option value="3">C3: Massive hypercementosis</option>
                    </select>
                </div>
                <div class="calc-field">
                    <label class="calc-label">Root Resorption (R)</label>
                    <select class="calc-select" id="calcR" onchange="calculateGustafson()">
                        <option value="0">R0: No resorption</option>
                        <option value="1">R1: Isolated spots</option>
                        <option value="2">R2: Deeper resorption bays</option>
                        <option value="3">R3: Extensive cementoclasia</option>
                    </select>
                </div>
                <div class="calc-field">
                    <label class="calc-label">Root Transparency (T) - Highest Correlation!</label>
                    <select class="calc-select" id="calcT" onchange="calculateGustafson()">
                        <option value="0">T0: No transparency</option>
                        <option value="1">T1: Apical root transparent</option>
                        <option value="2">T2: Middle third involved</option>
                        <option value="3">T3: >2/3 of root transparent</option>
                    </select>
                </div>
            </div>
            <div class="calc-result-banner">
                <div>
                    <div style="font-size:0.82rem; color:var(--text-secondary);">Calculated Total Score (X): <span id="scoreX" style="color:#fff; font-weight:700;">0</span></div>
                    <div style="font-size:0.75rem; color:var(--text-muted);">Standard Error: &plusmn;3.63 years</div>
                </div>
                <div>
                    <div style="font-size:0.8rem; color:var(--text-secondary); text-align:right;">Estimated Age</div>
                    <div class="calc-result-number" id="estimatedAge">11.4 years</div>
                </div>
            </div>
        </div>

        <!-- Microscopic Spotters Grid -->
        <div class="lab-section-title">Microscopic Spotter Flashcards (Oral Pathology & Biopsy Hallmarks)</div>
        <div class="spotter-grid" id="spotterGrid"></div>

        <!-- Viva Voce Quiz -->
        <div class="lab-section-title">High-Yield University Viva Voce Quiz Engine</div>
        <div id="quizContainer"></div>
    </main>

    <script>
        const CHAPTERS = {chapters_json};
        const MATRICES = {matrices_json};
        const SPOTTERS = {spotters_json};
        const QUIZ = {quiz_json};

        let currentCategory = 'All';
        let currentChapterIndex = 0;

        function switchTab(tab) {{
            const curriculumTab = document.getElementById('tabCurriculum');
            const labTab = document.getElementById('tabLab');
            const curriculumWorkspace = document.getElementById('curriculumWorkspace');
            const labWorkspace = document.getElementById('labWorkspace');

            if (tab === 'curriculum') {{
                curriculumTab.classList.add('active');
                labTab.classList.remove('active');
                curriculumWorkspace.style.display = 'flex';
                labWorkspace.style.display = 'none';
            }} else {{
                labTab.classList.add('active');
                curriculumTab.classList.remove('active');
                curriculumWorkspace.style.display = 'none';
                labWorkspace.style.display = 'block';
                renderLabContent();
            }}
        }}

        function filterCategory(cat) {{
            currentCategory = cat;
            document.querySelectorAll('.category-pill').forEach(btn => {{
                if (btn.innerText.includes(cat) || (cat === 'All' && btn.innerText.includes('All'))) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});
            renderTopicList();
        }}

        function filterTopics() {{
            renderTopicList();
        }}

        function renderTopicList() {{
            const listEl = document.getElementById('topicList');
            const query = (document.getElementById('topicSearch').value || '').toLowerCase();

            listEl.innerHTML = '';
            CHAPTERS.forEach((ch, idx) => {{
                const matchesCat = (currentCategory === 'All') || 
                                   (currentCategory === 'Odontogenic' && ch.category.includes('Odontogenic')) ||
                                   (currentCategory === 'Caries' && (ch.category.includes('Caries') || ch.category.includes('Developmental'))) ||
                                   (currentCategory === 'Salivary' && (ch.category.includes('Salivary') || ch.category.includes('Oncology'))) ||
                                   (currentCategory === 'Infections' && (ch.category.includes('Microbiology') || ch.category.includes('Bone') || ch.category.includes('Mucosal'))) ||
                                   (currentCategory === 'Forensic' && ch.category.includes('Forensic'));

                const matchesQuery = ch.title.toLowerCase().includes(query) || 
                                     ch.category.toLowerCase().includes(query) ||
                                     ch.key_points.some(kp => kp.toLowerCase().includes(query));

                if (matchesCat && matchesQuery) {{
                    const card = document.createElement('div');
                    card.className = `topic-card ${{idx === currentChapterIndex ? 'active' : ''}}`;
                    card.onclick = () => selectChapter(idx);
                    card.innerHTML = `
                        <div class="topic-card-category">${{ch.category}}</div>
                        <div class="topic-card-title">${{idx + 1}}. ${{ch.title}}</div>
                        <div class="topic-card-meta">
                            <span>${{ch.badge}}</span>
                            <span>${{ch.reading_time}}</span>
                        </div>
                    `;
                    listEl.appendChild(card);
                }}
            }});
        }}

        function selectChapter(idx) {{
            currentChapterIndex = idx;
            renderTopicList();
            renderViewer();
        }}

        function renderViewer() {{
            const viewerEl = document.getElementById('contentViewer');
            const ch = CHAPTERS[currentChapterIndex];
            if (!ch) return;

            let sectionsHtml = '';
            ch.sections.forEach(sec => {{
                sectionsHtml += `
                    <div class="section-card">
                        <div class="sec-title">${{sec.title}}</div>
                        <div class="sec-body">${{markdownToHtml(sec.content)}}</div>
                    </div>
                `;
            }});

            viewerEl.innerHTML = `
                <div class="viewer-header">
                    <div class="viewer-cat">${{ch.category}} • Chapter ${{currentChapterIndex + 1}}</div>
                    <h1 class="viewer-title">${{ch.title}}</h1>
                    <div class="viewer-badge-row">
                        <span class="badge-item">${{ch.badge}}</span>
                        <span class="badge-item">${{ch.reading_time}}</span>
                    </div>
                    <div class="clinical-pearl-banner">
                        <strong>Clinical & Histopathological Pearl:</strong> ${{ch.clinical_pearl}}
                    </div>
                </div>

                <div class="keypoints-section">
                    <div class="keypoints-heading">Core High-Yield Exam Facts</div>
                    <ul class="keypoints-ul">
                        ${{ch.key_points.map(kp => `<li>${{markdownToHtml(kp)}}</li>`).join('')}}
                    </ul>
                </div>

                ${{sectionsHtml}}
            `;
            viewerEl.scrollTop = 0;
        }}

        function renderLabContent() {{
            // Spotters
            const spotterGrid = document.getElementById('spotterGrid');
            if (spotterGrid.innerHTML === '') {{
                SPOTTERS.forEach(sp => {{
                    const card = document.createElement('div');
                    card.className = 'spotter-card';
                    card.innerHTML = `
                        <div class="spotter-header">Histological Spotter</div>
                        <div class="spotter-title">${{sp.title}}</div>
                        <div class="spotter-condition">${{sp.condition}}</div>
                        <ul class="spotter-features">
                            ${{sp.features.map(f => `<li>${{f}}</li>`).join('')}}
                        </ul>
                        <div class="spotter-viva"><strong>Viva Pearl:</strong> ${{sp.viva_tip}}</div>
                    `;
                    spotterGrid.appendChild(card);
                }});
            }}

            // Quiz
            const quizContainer = document.getElementById('quizContainer');
            if (quizContainer.innerHTML === '') {{
                QUIZ.forEach((q, idx) => {{
                    const card = document.createElement('div');
                    card.className = 'quiz-card';
                    card.innerHTML = `
                        <div class="quiz-q">${{idx + 1}}. ${{q.question}}</div>
                        <div class="quiz-opts">
                            ${{q.options.map((opt, oIdx) => `
                                <button class="quiz-opt" onclick="checkAnswer(this, ${{idx}}, ${{oIdx}})">${{opt}}</button>
                            `).join('')}}
                        </div>
                        <div class="quiz-exp" id="exp_${{idx}}">${{q.explanation}}</div>
                    `;
                    quizContainer.appendChild(card);
                }});
            }}
        }}

        function checkAnswer(btn, qIdx, optIdx) {{
            const q = QUIZ[qIdx];
            const opts = btn.parentElement.querySelectorAll('.quiz-opt');
            opts.forEach(o => o.disabled = true);
            const expEl = document.getElementById(`exp_${{qIdx}}`);

            if (optIdx === q.correct) {{
                btn.classList.add('correct');
            }} else {{
                btn.classList.add('incorrect');
                opts[q.correct].classList.add('correct');
            }}
            expEl.style.display = 'block';
        }}

        function calculateGustafson() {{
            const a = parseInt(document.getElementById('calcA').value);
            const p = parseInt(document.getElementById('calcP').value);
            const s = parseInt(document.getElementById('calcS').value);
            const c = parseInt(document.getElementById('calcC').value);
            const r = parseInt(document.getElementById('calcR').value);
            const t = parseInt(document.getElementById('calcT').value);

            const x = a + p + s + c + r + t;
            const age = 11.43 + (4.56 * x);

            document.getElementById('scoreX').innerText = x;
            document.getElementById('estimatedAge').innerText = age.toFixed(1) + ' years';
        }}

        function markdownToHtml(md) {{
            if (!md) return '';
            let html = md
                .replace(/^### (.*$)/gim, '<h4 style="font-size:1.05rem; font-weight:700; margin:1rem 0 0.5rem 0; color:#fde68a;">$1</h4>')
                .replace(/^## (.*$)/gim, '<h3 style="font-size:1.15rem; font-weight:700; margin:1.2rem 0 0.6rem 0; color:#fff;">$1</h3>')
                .replace(/^# (.*$)/gim, '<h2 style="font-size:1.3rem; font-weight:800; margin:1.5rem 0 0.8rem 0; color:#fff;">$1</h2>')
                .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong style="color:#ffffff;">$1</strong>')
                .replace(/\\*(.*?)\\*/gim, '<em>$1</em>')
                .replace(/```([\\s\\S]*?)```/gim, '<pre>$1</pre>')
                .replace(/^\\* (.*$)/gim, '<li>$1</li>')
                .replace(/\\n/gim, '<br>');
            return html;
        }}

        // Initial setup
        renderTopicList();
        renderViewer();
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

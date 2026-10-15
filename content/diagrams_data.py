# -*- coding: utf-8 -*-
"""
High-resolution histopathological SVG schematics, Layman analogies, and Flashcards for Oral Pathology.
"""

def generate_svg_schematic(ch_id, title):
    """Generates clean, responsive inline SVG histopathological and clinical schematics."""
    
    if "ameloblastoma" in ch_id:
        return f'''<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="420" fill="#0b1120" rx="12"/>
            <text x="400" y="34" fill="#f43f5e" font-size="16" font-weight="700" text-anchor="middle">AMELOBLASTOMA: VICKERS-GORLIN CRITERIA &amp; HISTOPATHOLOGICAL ISLAND</text>
            
            <!-- Follicular Island Boundary -->
            <path d="M 120 180 C 120 90, 360 80, 480 120 C 580 150, 680 100, 680 220 C 680 320, 520 370, 380 340 C 240 310, 120 300, 120 180 Z" fill="#1e1b4b" stroke="#a855f7" stroke-width="3"/>

            <!-- Peripheral Columnar Cells (Pre-ameloblast-like) -->
            <g fill="#9333ea" stroke="#c084fc" stroke-width="1.5">
                <rect x="140" y="160" width="16" height="32" rx="3"/>
                <circle cx="148" cy="184" r="5" fill="#f43f5e"/> <!-- Nucleus polarized away from BM -->
                <rect x="160" y="145" width="16" height="32" rx="3"/>
                <circle cx="168" cy="169" r="5" fill="#f43f5e"/>
                <rect x="180" y="135" width="16" height="32" rx="3"/>
                <circle cx="188" cy="159" r="5" fill="#f43f5e"/>
                <rect x="200" y="128" width="16" height="32" rx="3"/>
                <circle cx="208" cy="152" r="5" fill="#f43f5e"/>
                <rect x="220" y="122" width="16" height="32" rx="3"/>
                <circle cx="228" cy="146" r="5" fill="#f43f5e"/>
                <rect x="240" y="118" width="16" height="32" rx="3"/>
                <circle cx="248" cy="142" r="5" fill="#f43f5e"/>
                <rect x="260" y="115" width="16" height="32" rx="3"/>
                <circle cx="268" cy="139" r="5" fill="#f43f5e"/>
            </g>

            <!-- Central Stellate Reticulum -->
            <g stroke="#38bdf8" stroke-width="1.5" fill="#0284c7">
                <circle cx="340" cy="220" r="4"/>
                <line x1="340" y1="220" x2="380" y2="200" stroke="#38bdf8" stroke-dasharray="2,2"/>
                <circle cx="380" cy="200" r="4"/>
                <line x1="380" y1="200" x2="420" y2="230" stroke="#38bdf8" stroke-dasharray="2,2"/>
                <circle cx="420" cy="230" r="4"/>
                <line x1="420" y1="230" x2="460" y2="190" stroke="#38bdf8" stroke-dasharray="2,2"/>
                <circle cx="460" cy="190" r="4"/>
                <line x1="460" y1="190" x2="500" y2="220" stroke="#38bdf8" stroke-dasharray="2,2"/>
                <circle cx="500" cy="220" r="4"/>
            </g>
            <text x="420" y="260" fill="#7dd3fc" font-size="12" font-weight="600" text-anchor="middle">Central Stellate Reticulum-like Meshwork</text>

            <!-- Annotations Callouts -->
            <!-- Vickers-Gorlin 1: Palisading -->
            <line x1="220" y1="110" x2="220" y2="60" stroke="#f43f5e" stroke-width="2"/>
            <rect x="120" y="45" width="200" height="30" fill="#881337" rx="6"/>
            <text x="220" y="65" fill="#fff" font-size="10.5" font-weight="700" text-anchor="middle">1. TALL COLUMNAR PALISADING</text>

            <!-- Vickers-Gorlin 2: Reversed Polarity -->
            <line x1="148" y1="200" x2="80" y2="240" stroke="#f43f5e" stroke-width="2"/>
            <rect x="20" y="240" width="180" height="42" fill="#881337" rx="6"/>
            <text x="110" y="258" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">2. REVERSED POLARITY</text>
            <text x="110" y="274" fill="#fca5a5" font-size="9" text-anchor="middle">Nuclei oriented away from BM</text>

            <!-- Vickers-Gorlin 3: Subnuclear Vacuolization -->
            <line x1="170" y1="180" x2="110" y2="330" stroke="#f43f5e" stroke-width="2"/>
            <rect x="20" y="330" width="190" height="42" fill="#881337" rx="6"/>
            <text x="115" y="348" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">3. SUBNUCLEAR VACUOLES</text>
            <text x="115" y="364" fill="#fca5a5" font-size="9" text-anchor="middle">Clear spaces beneath nuclei</text>

            <!-- Surgical Margin Box -->
            <rect x="520" y="290" width="240" height="90" fill="#1e293b" stroke="#f59e0b" rx="8"/>
            <text x="640" y="315" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">SURGICAL MARGIN PRINCIPLE</text>
            <text x="535" y="340" fill="#cbd5e1" font-size="10">• Microscopic cortical infiltration</text>
            <text x="535" y="358" fill="#cbd5e1" font-size="10">• Requires 1.0–1.5 cm safe bone margin</text>
            <text x="535" y="374" fill="#ef4444" font-size="9.5" font-weight="700">• Curettage recurrence rate: 60–90%</text>
        </svg>'''

    elif "cyst" in ch_id:
        return f'''<svg viewBox="0 0 800 390" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="390" fill="#0b1120" rx="12"/>
            <text x="400" y="34" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">ODONTOGENIC KERATOCYST (OKC): HISTOPATHOLOGICAL HALLMARKS</text>
            
            <g transform="translate(60, 70)">
                <!-- Cyst Lumen -->
                <rect x="0" y="0" width="680" height="70" fill="#312e81" stroke="#6366f1" rx="8"/>
                <text x="340" y="38" fill="#c7d2fe" font-size="13" font-weight="700" text-anchor="middle">CYSTIC LUMEN: CHEESY PARAKERATIN FLAKES (Low Protein &lt; 4.0 g/dL)</text>
                
                <!-- Corrugated Parakeratin Lining -->
                <path d="M 0 70 Q 20 60, 40 70 T 80 70 T 120 70 T 160 70 T 200 70 T 240 70 T 280 70 T 320 70 T 360 70 T 400 70 T 440 70 T 480 70 T 520 70 T 560 70 T 600 70 T 640 70 T 680 70" fill="none" stroke="#f43f5e" stroke-width="4"/>
                <text x="340" y="95" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">1. WAVY, CORRUGATED PARAKERATIN SURFACE LAYER</text>

                <!-- 6-8 Cell Layers Stratified Squamous Epithelium -->
                <rect x="0" y="105" width="680" height="50" fill="#4338ca" opacity="0.6"/>
                <text x="340" y="135" fill="#ffffff" font-size="11.5" font-weight="600" text-anchor="middle">2. UNIFORM 6 TO 8 CELL LAYERS THICKNESS (No Rete Pegs / Flat Interface)</text>

                <!-- Palisaded Basal Layer (Picket Fence) -->
                <rect x="0" y="160" width="680" height="30" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
                <text x="340" y="180" fill="#e9d5ff" font-size="11" font-weight="700" text-anchor="middle">3. PALISADED BASAL LAYER: HYPERCHROMATIC 'PICKET-FENCE' / 'TOMBSTONE' NUCLEI</text>

                <!-- Fibrous Capsule & Satellite Microcysts -->
                <rect x="0" y="195" width="680" height="75" fill="#1e293b" stroke="#334155" rx="4"/>
                
                <!-- Satellite / Daughter Cyst -->
                <circle cx="200" cy="235" r="22" fill="#312e81" stroke="#f43f5e" stroke-width="2"/>
                <circle cx="200" cy="235" r="12" fill="#4338ca"/>
                <text x="235" y="240" fill="#fca5a5" font-size="10.5" font-weight="700">Daughter / Satellite Cyst in Capsule (High Recurrence!)</text>

                <circle cx="500" cy="235" r="18" fill="#312e81" stroke="#a855f7" stroke-width="1.5"/>
                <text x="530" y="240" fill="#c084fc" font-size="10.5">Odontogenic Rests of Serres</text>
            </g>

            <rect x="60" y="340" width="680" height="36" fill="#1e293b" rx="6"/>
            <text x="400" y="362" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Recurrence Prevention: Enucleation + Carnoy's Solution (chemical cautery) or Cryotherapy to eradicate satellite cysts.</text>
        </svg>'''

    elif "salivary" in ch_id:
        return f'''<svg viewBox="0 0 800 390" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="390" fill="#0b1120" rx="12"/>
            <text x="400" y="34" fill="#a855f7" font-size="16" font-weight="700" text-anchor="middle">SALIVARY NEOPLASMS: PLEOMORPHIC ADENOMA vs ADENOID CYSTIC CARCINOMA</text>
            
            <!-- Left: Pleomorphic Adenoma -->
            <g transform="translate(40, 65)">
                <rect x="0" y="0" width="345" height="255" fill="#1e1b4b" stroke="#c084fc" stroke-width="2" rx="10"/>
                <rect x="0" y="0" width="345" height="36" fill="#7e22ce" rx="10"/>
                <text x="172" y="23" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">PLEOMORPHIC ADENOMA (Benign Mixed)</text>
                
                <text x="16" y="65" fill="#f5d0fe" font-size="11" font-weight="700">• Epithelial &amp; Myoepithelial Ducts:</text>
                <text x="24" y="85" fill="#cbd5e1" font-size="10.5">Ductal lumens filled with pink eosinophilic mucin.</text>

                <text x="16" y="115" fill="#f5d0fe" font-size="11" font-weight="700">• Plasmacytoid Myoepithelial Cells:</text>
                <text x="24" y="135" fill="#cbd5e1" font-size="10.5">Eccentric cartwheel nuclei in hyaline cytoplasm.</text>

                <text x="16" y="165" fill="#f5d0fe" font-size="11" font-weight="700">• Chondromyxoid Stroma:</text>
                <text x="24" y="185" fill="#cbd5e1" font-size="10.5">Cells residing within pseudo-cartilage lacunae.</text>

                <rect x="16" y="205" width="313" height="38" fill="#4c1d95" rx="6"/>
                <text x="172" y="222" fill="#fde047" font-size="10" font-weight="700" text-anchor="middle">Capsular Pseudopods:</text>
                <text x="172" y="236" fill="#e9d5ff" font-size="9" text-anchor="middle">Enucleation contraindicated; do superficial parotidectomy.</text>
            </g>

            <!-- Right: Adenoid Cystic Carcinoma -->
            <g transform="translate(415, 65)">
                <rect x="0" y="0" width="345" height="255" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="10"/>
                <rect x="0" y="0" width="345" height="36" fill="#991b1b" rx="10"/>
                <text x="172" y="23" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">ADENOID CYSTIC CARCINOMA (Cylindroma)</text>
                
                <text x="16" y="65" fill="#fca5a5" font-size="11" font-weight="700">• Cribriform 'Swiss-Cheese' Pattern:</text>
                <text x="24" y="85" fill="#cbd5e1" font-size="10.5">Basaloid cells surrounding sharply punched-out spaces.</text>

                <text x="16" y="115" fill="#fca5a5" font-size="11" font-weight="700">• Cylindrical Pseudocysts:</text>
                <text x="24" y="135" fill="#cbd5e1" font-size="10.5">Reduplicated basement membrane &amp; basophilic mucin.</text>

                <text x="16" y="165" fill="#fca5a5" font-size="11" font-weight="700">• Perineural Invasion (Neurotropism):</text>
                <text x="24" y="185" fill="#cbd5e1" font-size="10.5">Invasion of epineurium causing facial numbness &amp; pain.</text>

                <rect x="16" y="205" width="313" height="38" fill="#7f1d1d" rx="6"/>
                <text x="172" y="222" fill="#fde047" font-size="10" font-weight="700" text-anchor="middle">Cannonball Lung Metastases:</text>
                <text x="172" y="236" fill="#fecaca" font-size="9" text-anchor="middle">Late distant hematogenous spread despite local control.</text>
            </g>

            <rect x="40" y="335" width="720" height="36" fill="#1e293b" rx="6"/>
            <text x="400" y="357" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Key Rule: Parotid is #1 site for Pleomorphic Adenoma (85%); Minor salivary glands (Palate) are #1 for Adenoid Cystic Carcinoma.</text>
        </svg>'''

    elif "pemphigus" in ch_id or "vesiculo" in ch_id:
        return f'''<svg viewBox="0 0 800 390" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="390" fill="#0b1120" rx="12"/>
            <text x="400" y="34" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">VESICULOBULLOUS DIFFERENTIATION: PEMPHIGUS vs PEMPHIGOID</text>
            
            <!-- Left: Pemphigus -->
            <g transform="translate(40, 65)">
                <rect x="0" y="0" width="345" height="255" fill="#1e1b4b" stroke="#f43f5e" stroke-width="2" rx="10"/>
                <rect x="0" y="0" width="345" height="36" fill="#be123c" rx="10"/>
                <text x="172" y="23" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">PEMPHIGUS VULGARIS (Intraepithelial)</text>
                
                <text x="16" y="65" fill="#fda4af" font-size="11" font-weight="700">• Cleavage Level:</text>
                <text x="24" y="85" fill="#fff" font-size="11" font-weight="700">INTRAPITHELIAL (Suprabasal Cleft)</text>

                <text x="16" y="115" fill="#fda4af" font-size="11" font-weight="700">• Target Autoantigen:</text>
                <text x="24" y="135" fill="#cbd5e1" font-size="10.5">Desmoglein 3 (Dsg3) desmosomal cadherins.</text>

                <text x="16" y="165" fill="#fda4af" font-size="11" font-weight="700">• Cytology &amp; Histology:</text>
                <text x="24" y="185" fill="#cbd5e1" font-size="10.5">Acantholytic Tzanck cells + 'Row of Tombstones'.</text>

                <rect x="16" y="205" width="313" height="38" fill="#881337" rx="6"/>
                <text x="172" y="222" fill="#fde047" font-size="10" font-weight="700" text-anchor="middle">Direct Immunofluorescence (DIF):</text>
                <text x="172" y="236" fill="#fecdd3" font-size="9" text-anchor="middle">Intercellular 'Fishnet' / 'Chicken-Wire' IgG pattern.</text>
            </g>

            <!-- Right: Pemphigoid -->
            <g transform="translate(415, 65)">
                <rect x="0" y="0" width="345" height="255" fill="#1e293b" stroke="#0ea5e9" stroke-width="2" rx="10"/>
                <rect x="0" y="0" width="345" height="36" fill="#0369a1" rx="10"/>
                <text x="172" y="23" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">MUCOUS MEMBRANE PEMPHIGOID (Subepithelial)</text>
                
                <text x="16" y="65" fill="#7dd3fc" font-size="11" font-weight="700">• Cleavage Level:</text>
                <text x="24" y="85" fill="#fff" font-size="11" font-weight="700">SUBEPITHELIAL (Basement Membrane Split)</text>

                <text x="16" y="115" fill="#7dd3fc" font-size="11" font-weight="700">• Target Autoantigen:</text>
                <text x="24" y="135" fill="#cbd5e1" font-size="10.5">BP180 (Type XVII Collagen) &amp; Laminin 332.</text>

                <text x="16" y="165" fill="#7dd3fc" font-size="11" font-weight="700">• Bulla Quality &amp; Ocular Risk:</text>
                <text x="24" y="185" fill="#cbd5e1" font-size="10.5">Tense, intact bulla. Risk of ocular symblepharon / blindness.</text>

                <rect x="16" y="205" width="313" height="38" fill="#0c4a6e" rx="6"/>
                <text x="172" y="222" fill="#fde047" font-size="10" font-weight="700" text-anchor="middle">Direct Immunofluorescence (DIF):</text>
                <text x="172" y="236" fill="#bae6fd" font-size="9" text-anchor="middle">Smooth Continuous LINEAR BAND of IgG/C3 at BMZ.</text>
            </g>

            <rect x="40" y="335" width="720" height="36" fill="#1e293b" rx="6"/>
            <text x="400" y="357" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Bedside Sign: Nikolsky's sign is strongly positive in Pemphigus Vulgaris (firm shearing force dislodges mucosa).</text>
        </svg>'''

    else:
        return f'''<svg viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="360" fill="#0b1120" rx="12"/>
            <text x="400" y="36" fill="#f43f5e" font-size="15" font-weight="700" text-anchor="middle">{title.upper()}: CLINICAL &amp; HISTOPATHOLOGICAL WORKFLOW</text>
            
            <rect x="50" y="70" width="200" height="90" fill="#1e1b4b" stroke="#a855f7" rx="8"/>
            <text x="150" y="95" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">1. CLINICAL PRESENTATION</text>
            <text x="150" y="118" fill="#cbd5e1" font-size="10" text-anchor="middle">Site, Age, Gender Predilection</text>
            <text x="150" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Expansion Pattern (BL vs AP)</text>

            <line x1="250" y1="115" x2="300" y2="115" stroke="#a855f7" stroke-width="2.5"/>

            <rect x="300" y="70" width="200" height="90" fill="#1e1b4b" stroke="#f43f5e" rx="8"/>
            <text x="400" y="95" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">2. RADIOGRAPHIC MATRIX</text>
            <text x="400" y="118" fill="#cbd5e1" font-size="10" text-anchor="middle">Unilocular vs Multilocular</text>
            <text x="400" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Root Resorption &amp; Margins</text>

            <line x1="500" y1="115" x2="550" y2="115" stroke="#f43f5e" stroke-width="2.5"/>

            <rect x="550" y="70" width="200" height="90" fill="#1e1b4b" stroke="#38bdf8" rx="8"/>
            <text x="650" y="95" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">3. HISTOPATHOLOGY</text>
            <text x="650" y="118" fill="#cbd5e1" font-size="10" text-anchor="middle">Pathognomonic Microscopic Signs</text>
            <text x="650" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Special Stains &amp; Cytology</text>

            <line x1="650" y1="160" x2="650" y2="210" stroke="#38bdf8" stroke-width="2.5"/>

            <rect x="50" y="210" width="700" height="110" fill="#1e293b" stroke="#10b981" rx="8"/>
            <text x="400" y="238" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">4. DEFINITIVE SURGICAL / MEDICAL THERAPEUTICS &amp; RECURRENCE RISK</text>
            
            <g transform="translate(70, 255)">
                <rect x="0" y="0" width="200" height="48" fill="#0f172a" rx="6"/>
                <text x="100" y="20" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">SURGICAL MARGIN</text>
                <text x="100" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Enucleation vs Radical Resection</text>
            </g>

            <g transform="translate(300, 255)">
                <rect x="0" y="0" width="200" height="48" fill="#0f172a" rx="6"/>
                <text x="100" y="20" fill="#a7f3d0" font-size="10.5" font-weight="700" text-anchor="middle">ADJUVANT CAUTERY</text>
                <text x="100" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Carnoy's solution / Cryotherapy</text>
            </g>

            <g transform="translate(530, 255)">
                <rect x="0" y="0" width="200" height="48" fill="#0f172a" rx="6"/>
                <text x="100" y="20" fill="#fde68a" font-size="10.5" font-weight="700" text-anchor="middle">LONG-TERM PROGNOSIS</text>
                <text x="100" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Follow-up radiographic surveillance</text>
            </g>
        </svg>'''


LAYMAN_ANALOGIES = {
    "chap1_ameloblastoma": {
        "title": "The Root-Munching Ivy and the Inverted Pre-Ameloblasts",
        "analogy": "Imagine an aggressive English ivy creeping through the porous mortar of a brick house. In conventional ameloblastoma, the tumor nests resemble tiny islands of embryonic enamel-forming organs. However, the outer picket-fence cells are biologically 'confused' — their cell nuclei, which usually face the basement membrane, flip around backwards (reversed nuclear polarity). Because this ivy infiltrates through the sponge-like bone marrow spaces far beyond what X-rays reveal, merely scraping it out (curettage) leaves behind living roots that grow back in 90% of patients, requiring radical bone resection."
    },
    "chap2_benign_odontogenic_tumors": {
        "title": "The Apple-Green Crystal Cave and the Tooth Bag",
        "analogy": "In Pindborg tumor (CEOT), the cells produce a bizarre proteinaceous sludge that hardens into concentric mineralized rings (Liesegang rings), like stalactites in a cave. Under polarized light, Congo red stain makes these amyloid pools glow with an eerie, radiant apple-green luminescence. Odontomas, conversely, are like a confused dental factory running without a blueprint — producing either a neat bag of twenty miniature doll-teeth (Compound) or a chaotic lump of scrambled enamel and dentin (Complex)."
    },
    "chap3_okc_gorlin": {
        "title": "The Secret Anteroposterior Tunnel and the Escaped Seeds",
        "analogy": "Unlike most cysts that swell outwards like round balloons, an OKC burrows silently length-wise down the marrow of the jaw like a high-speed underground subway tunnel, rarely expanding the outer bone until it is massive. Its thin lining is corrugated like an accordion and constantly sheds cheesy keratin flakes. Deep within the cyst's outer capsule hide microscopic 'seeds' (satellite daughter cysts). If the surgeon doesn't chemically wash the bone pocket with Carnoy's solution to dissolve these hidden seeds, they sprout into new cysts years later."
    },
    "chap4_dentigerous_inflammatory_cysts": {
        "title": "The Water Balloon Clamped Around the Crown's Neck",
        "analogy": "When a tooth fails to erupt (often a lower wisdom tooth), the protective sac that once formed its enamel (reduced enamel epithelium) gets flooded with tissue fluid. The balloon swells up, firmly attached right at the tooth's neck (cementoenamel junction). It looks like a crown floating inside a clear balloon on an X-ray. Radical surgery is unnecessary; removing the impacted tooth along with the balloon cures the condition completely."
    },
    "chap5_non_odontogenic_cysts": {
        "title": "The Trapped Tear Drops in Ancient Fusion Seams",
        "analogy": "During facial development in the womb, various facial shelves meet and fuse together like welded metal plates. Non-odontogenic cysts form when microscopic epithelial remnants get trapped inside these embryonic fusion lines — such as the nasopalatine duct or the incisive canal behind the upper front teeth, creating a heart-shaped or pear-shaped radiolucency."
    },
    "chap6_salivary_neoplasms": {
        "title": "The Chameleon Matrix and the Swiss Cheese Nerve-Hunter",
        "analogy": "Pleomorphic adenoma is called 'mixed' because its versatile myoepithelial cells act like shapeshifters, laying down ductile tubes, cartilage-like cushions, and jelly-like mucus all inside the same lump. In contrast, Adenoid Cystic Carcinoma is a stealthy predator: under the microscope, it forms countless punched-out cylindrical holes like Swiss cheese, and it has an affinity for wrapping around nerve fibers, causing facial numbness long before a visible lump appears."
    },
    "chap7_non_neoplastic_salivary": {
        "title": "The Severed Garden Hose and the Clogged Pipe",
        "analogy": "When you accidentally bite your lower lip, you sever a tiny microscopic salivary duct. Saliva continues pumping out but has nowhere to go, forming an inflaming pool in the connective tissue like a pierced garden hose leaking under the lawn — this is a Mucocele. In Sialolithiasis, a calcium stone wedges in Wharton's duct, causing the submandibular gland to balloon painfully like an obstructed pipe whenever the patient smells sour lemon or food."
    },
    "chap8_opmd_leukoplakia": {
        "title": "The Weathered Paint and the Mutinous Keratinocytes",
        "analogy": "Leukoplakia is like hardened, chalky-white marine paint on a ship deck that cannot be scraped off. Under chronic tobacco or areca nut irritation, the surface epithelium manufactures a thick armor of keratin. When individual cells start showing cellular anarchy (disorientation, enlarged dark nuclei, abnormal cell division), it enters dysplasia — a flashing yellow caution signal that invasive cancer is on the horizon."
    },
    "chap9_osmf_lichen_planus": {
        "title": "The Leather-Bound Birdcage and the Friendly Fire Army",
        "analogy": "In Oral Submucous Fibrosis (OSMF), arecoline from betel nut supercharges collagen-making fibroblasts while inhibiting collagen-dissolving enzymes. The cheek lining gradually turns into rigid, leathery raw hide, trapping the mouth like a birdcage until the patient can barely insert one finger. In Lichen Planus, a disciplined army of T-lymphocytes lines up in a dense horizontal wall along the basement membrane, attacking the skin's basal cells in an autoimmune friendly fire that leaves delicate white lace-like patterns (Wickham's striae)."
    },
    "chap10_oscc": {
        "title": "The Breached Fortress Gate and the Trapped Keratin Swirls",
        "analogy": "The oral mucosa's basement membrane is the fortress wall separating the outside world from deep muscle and blood vessels. In invasive Oral Cancer (OSCC), malignant epithelial cells break through the basement membrane and burrow deep into bone and tongue muscle. In well-differentiated cancers, these malignant cells still try to make enamel-like keratin, but because they are buried deep underground, the keratin gets trapped in concentric circular swirls called 'keratin pearls'."
    },
    "chap11_mesenchymal_soft_tissue": {
        "title": "The Insulating Wrapper and the Disorganized Cable",
        "analogy": "Nerve fibers are coated with insulating Schwann cells. In a Schwannoma (Neurilemoma), these cells multiply into a benign lump that features dense, highly orderly picket lines (Antoni A with Verocay bodies) alternating with loose watery mesh (Antoni B). Because it wears an intact fibrous capsule, a surgeon can shell it out neatly without damaging the nerve itself."
    },
    "chap12_dental_caries": {
        "title": "The Acid-Brewing Bacterial City and the Critical Demineralization Point",
        "analogy": "Dental caries is not a single infection; it is a bio-chemical war. Streptococcus mutans forms a sticky fortress (plaque) and ferments dietary sugars into lactic acid. Whenever the local pH drops below the critical threshold of 5.5, calcium hydroxyapatite crystals in the enamel dissolve into saliva. If saliva's natural mineral wash cannot neutralize the acid in time, the subsurface enamel collapses into a physical cavity."
    },
    "chap13_developmental_tooth_structure": {
        "title": "The Defective Enamel Blueprint and the Thistle-Tube Pulps",
        "analogy": "Enamel formation is like baking porcelain: you first lay down a soft organic protein scaffold, then fill it with minerals, and finally harden it. In Amelogenesis Imperfecta, genetic errors produce either paper-thin enamel (Hypoplastic), soft cheesy enamel (Hypocalcified), or dull chipped enamel (Hypomaturation). In Dentinogenesis Imperfecta, the dentin is so translucent and amber that teeth look opalescent blue-brown, with obliterated pulp chambers."
    },
    "chap14_developmental_number_size": {
        "title": "The Siamese Twins and the Tooth Within a Tooth",
        "analogy": "During tooth budding, strange developmental quirks occur. In Gemination, a single tooth germ tries to divide into two ('twinning'), resulting in a gigantic tooth with one shared root canal. In Fusion, two separate tooth germs melt together, resulting in one missing tooth from the total dental arch count. In Dens Evaginatus or Invaginatus, an outer enamel pocket invaginates deep into the pulp like a pocket turned inside out."
    },
    "chap15_developmental_jaws_soft_tissues": {
        "title": "The Unclosed Curtains and the Bird-Like Profile",
        "analogy": "During fetal development, the palate and lip close like curtains drawn from both sides towards the center. When curtains fail to meet, cleft lip and palate occur. In Pierre Robin Sequence, an underdeveloped lower jaw (micrognathia) forces the tongue upwards and backwards, blocking the roof of the mouth from closing and creating life-threatening neonatal airway obstruction."
    },
    "chap16_bacterial_fungal_infections": {
        "title": "The Walled-Off Granuloma Fortress and the Wooden Jaw",
        "analogy": "In oral tuberculosis, hardy Mycobacterium bacilli resist ordinary destruction. The immune system builds a spherical stone fortress around them: epithelioid histiocytes fused into horseshoe-shaped Langhans giant cells, rimmed by lymphocytes with a dead caseous core. In Actinomycosis, anaerobic bacteria build yellowish 'sulfur granules' that punch multiple discharging sinus tracts through the jaw like volcanic vents."
    },
    "chap17_viral_infections": {
        "title": "The Dormant Ganglion Spy and the Corrugated Tongue Hair",
        "analogy": "Herpes Simplex Virus infects the mouth once, then retreats up the sensory nerve into the trigeminal ganglion where it sleeps undisturbed for decades. Under stress or sunburn, it wakes up and travels back down the nerve to create fever blisters. In Oral Hairy Leukoplakia, Epstein-Barr virus infects the lateral border of the tongue in immunocompromised patients, causing hyperkeratotic epithelial vertical ridges that look like white corrugated hair."
    },
    "chap18_vesiculobullous_diseases": {
        "title": "The Unzipped Velcro and the Ripped Carpet",
        "analogy": "Epithelial cells stay stuck together through tiny molecular snaps called desmosomes (like microscopic Velcro). In Pemphigus Vulgaris, autoantibodies rip apart the Velcro snaps, so the top layers of cells float away (acantholysis), leaving fragile blisters that pop at the touch of a cracker. In Pemphigoid, the autoantibodies target the hemidesmosome anchors attaching the entire carpet to the concrete floor, creating deep, tense blisters that leave scarring."
    },
    "chap19_bone_diseases": {
        "title": "The Calligraphy Script and the Chaotic Jigsaw Puzzle",
        "analogy": "Bone is living architectural scaffolding. In Fibrous Dysplasia, a genetic switch produces irregular, hook-like C-shaped bone trabeculae that resemble Chinese alphabet calligraphy floating in spindle cell soup, completely devoid of osteoblastic rimming. In Paget's Disease, bone-eating and bone-making cells run wild simultaneously, producing thick chaotic bone plates patched together by scalloped blue reversal lines that fit together like a scrambled jigsaw puzzle."
    },
    "chap20_forensic_odontology": {
        "title": "The Indestructible Black Box and the Transparent Root Barometer",
        "analogy": "Teeth are the human body's indestructible flight black box — they survive fire, plane crashes, and centuries underground. In Gustafson's method of forensic age estimation, examining a ground section of a single tooth under a microscope reveals six predictable aging signs. The most reliable barometer is Root Dentin Transparency: as decades pass, peritubular dentin slowly mineralizes and fills the tubules, turning the root apex glass-clear like fiber optics."
    }
}

FLASHCARDS = {
    "chap1_ameloblastoma": [
        {"q": "What are the 3 histological criteria of the Vickers-Gorlin sign in Ameloblastoma?", "a": "1. Tall columnar basal cells with palisaded nuclei, 2. Reversed nuclear polarity (nuclei oriented away from basement membrane), 3. Subnuclear cytoplasmic vacuolization."},
        {"q": "What is the typical radiographic appearance of conventional Ameloblastoma?", "a": "Multilocular 'Soap-bubble' or 'Honeycomb' radiolucency with knife-edge root resorption and buccolingual cortical expansion."},
        {"q": "What is the recommended surgical safe bone margin for solid multicystic Ameloblastoma?", "a": "1.0 to 1.5 cm of normal bony margin beyond radiographic borders (segmental or marginal resection)."}
    ],
    "chap2_benign_odontogenic_tumors": [
        {"q": "What is the pathognomonic polarized light finding in Calcifying Epithelial Odontogenic Tumor (CEOT / Pindborg)?", "a": "Apple-green birefringence of Congo Red-stained amyloid-like extracellular proteinaceous material under polarized light."},
        {"q": "What are Liesegang rings in CEOT?", "a": "Concentric, calcified calcospherites formed by mineralization within the amyloid-like tumor matrix."},
        {"q": "What is the key histological difference between Compound and Complex Odontoma?", "a": "Compound Odontoma contains miniature, anatomically recognizable tooth-like structures (denticles); Complex Odontoma is a chaotic conglomerate mass of enamel, dentin, and cementum without dental architecture."}
    ],
    "chap3_okc_gorlin": [
        {"q": "What are the 3 classic histological hallmarks of Odontogenic Keratocyst (OKC)?", "a": "1. Corrugated, wavy parakeratinized luminal surface, 2. Uniform 6-8 cell layers thickness with flat interface, 3. Palisaded basal layer with hyperchromatic 'picket-fence' or 'tombstone' nuclei."},
        {"q": "Why does OKC possess a high recurrence rate (30-60%) after simple enucleation?", "a": "Due to a thin friable epithelial lining, budding from basal layer, and retention of satellite daughter microcysts within the fibrous capsule."},
        {"q": "What genetic mutation and clinical tetrad characterize Gorlin-Goltz Syndrome?", "a": "PTCH1 gene mutation on chromosome 9q. Tetrad: Multiple OKCs, Multiple Nevoid Basal Cell Carcinomas, Bifid ribs, and Calcified falx cerebri."}
    ],
    "chap4_dentigerous_inflammatory_cysts": [
        {"q": "Where does the lining of a Dentigerous Cyst attach to the involved tooth?", "a": "Exclusively at the Cementoenamel Junction (CEJ) around the anatomical neck of an unerupted or impacted tooth."},
        {"q": "What is the tissue of origin of a Dentigerous Cyst?", "a": "Reduced Enamel Epithelium (REE) following completion of crown formation."},
        {"q": "What are Rushton bodies in inflammatory odontogenic cysts?", "a": "Curvilinear, linear, or hairpin-shaped eosinophilic hyaline structures found within the hyperplastic epithelial lining."}
    ],
    "chap5_non_odontogenic_cysts": [
        {"q": "What is the most common non-odontogenic developmental cyst of the oral cavity?", "a": "Nasopalatine Duct Cyst (Incisive Canal Cyst) — presenting as a well-circumscribed heart-shaped radiolucency between maxillary central incisors."},
        {"q": "What is a 'Globulomaxillary Cyst' currently recognized as in modern oral pathology?", "a": "An anatomical radiolucency (inverted pear-shaped between maxillary lateral incisor and canine), usually representing a Radicular Cyst, OKC, or AOT rather than a distinct fissural entity."},
        {"q": "What cyst arises from remnants of the thyroglossal tract and moves upwards on swallowing?", "a": "Thyroglossal Duct Cyst (treated via the Sistrunk surgical procedure)."}
    ],
    "chap6_salivary_neoplasms": [
        {"q": "What is the most common benign salivary gland neoplasm and its most frequent location?", "a": "Pleomorphic Adenoma (85% located in the superficial lobe of the Parotid gland)."},
        {"q": "Why is enucleation strictly contraindicated in Pleomorphic Adenoma?", "a": "Because microscopic tumor pseudopods penetrate the thin, incomplete fibrous pseudocapsule; simple enucleation leaves pseudopods behind, leading to high recurrence."},
        {"q": "What is the pathognomonic histological pattern and clinical behavior of Adenoid Cystic Carcinoma (AdCC)?", "a": "Cribriform 'Swiss-cheese' pattern of basaloid cells with cylindrical pseudocysts; marked neurotropism (perineural invasion) and late pulmonary cannonball metastases."}
    ],
    "chap7_non_neoplastic_salivary": [
        {"q": "What is the histological difference between a Mucus Extravasation Phenomenon and a Mucus Retention Cyst?", "a": "Extravasation phenomenon has NO epithelial lining (lined only by granulation tissue and foamy histiocytes); Retention cyst has a true ductal epithelial lining."},
        {"q": "What is a Ranula?", "a": "A large, bluish, translucent mucus extravasation pseudocyst arising from the sublingual salivary gland on the floor of the mouth."},
        {"q": "Which salivary duct is most prone to sialolithiasis and why?", "a": "Wharton's duct (Submandibular gland) — due to long tortuous upward course, thick viscous mucinous secretion, and high calcium/phosphate content."}
    ],
    "chap8_opmd_leukoplakia": [
        {"q": "What is the WHO definition of Oral Leukoplakia?", "a": "A white plaque of questionable risk having excluded other known diseases or disorders that carry no increased risk for cancer."},
        {"q": "What are 5 microscopic architectural features of Oral Epithelial Dysplasia?", "a": "1. Loss of basal polarity, 2. Drop-shaped rete pegs, 3. Irregular epithelial stratification, 4. Premature dyskeratosis / keratin pearls, 5. Increased and abnormal mitotic figures."},
        {"q": "Which clinical variety of Leukoplakia carries the highest malignant transformation rate?", "a": "Proliferative Verrucous Leukoplakia (PVL) and Non-homogeneous / Speckled Leukoplakia (Erythroleukoplakia, >20-40% risk)."}
    ],
    "chap9_osmf_lichen_planus": [
        {"q": "What is the primary etiological agent in Oral Submucous Fibrosis (OSMF)?", "a": "Areca nut (betel nut) chewing. Arecoline stimulates collagen synthesis, and flavonoids inhibit collagenase."},
        {"q": "What histological triad characterizes Oral Lichen Planus (OLP)?", "a": "1. Hyperparakeratosis with Saw-Tooth rete pegs, 2. Liquefaction degeneration of the basal cell layer with Civatte bodies, 3. Dense, band-like horizontal T-lymphocytic infiltrate at the BMZ."},
        {"q": "What is the pathognomonic Direct Immunofluorescence (DIF) finding in Oral Lichen Planus?", "a": "Shaggy, fibrillar deposition of Fibrinogen in a continuous band along the basement membrane zone."}
    ],
    "chap10_oscc": [
        {"q": "What is the hallmark histological feature of Well-Differentiated Oral Squamous Cell Carcinoma (OSCC)?", "a": "Keratin pearl formation (concentric laminated swirls of keratinized squamous cells) and prominent intercellular bridges."},
        {"q": "What are Broders' four histological grading tiers for OSCC?", "a": "Grade 1 (Well): >75% differentiated cells; Grade 2 (Moderately): 50-75%; Grade 3 (Poorly): 25-50%; Grade 4 (Anaplastic): <25% differentiated cells."},
        {"q": "What is the TNM staging cutoff for a T1 vs T2 oral cavity tumor?", "a": "T1 is tumor ≤ 2 cm in greatest dimension and depth of invasion (DOI) ≤ 5 mm; T2 is tumor > 2 cm and ≤ 4 cm, or DOI > 5 mm and ≤ 10 mm."}
    ],
    "chap11_mesenchymal_soft_tissue": [
        {"q": "What are Verocay bodies and in which tumor are they pathognomonic?", "a": "Eosinophilic, acellular zones consisting of cytoplasmic processes bordered by parallel palisading spindle nuclei; pathognomonic of Schwannoma (Neurilemoma, Antoni A areas)."},
        {"q": "What is Congenital Epulis of the Newborn (Granular Cell Tumor)?", "a": "A benign mucosal mass on the maxillary alveolar ridge of newborn females composed of large polygonal cells with eosinophilic granular cytoplasm; negative for S-100."},
        {"q": "What is the most common benign soft tissue tumor of the oral cavity?", "a": "Irritation Fibroma (focal fibrous hyperplasia) — a reactive inflammatory hyperplasia caused by chronic irritation."}
    ],
    "chap12_dental_caries": [
        {"q": "What is the critical pH threshold for enamel demineralization?", "a": "pH 5.5. Below this level, saliva is undersaturated with calcium and phosphate, driving hydroxyapatite crystal dissolution."},
        {"q": "Name the 4 histological zones of an early enamel carious lesion from deep to superficial.", "a": "1. Translucent zone (advancing front, 1% pore volume), 2. Dark zone (positive zone, 2-4%), 3. Body of the lesion (bulk, 5-25%), 4. Intact surface zone (<5%)."},
        {"q": "What is the primary microbial initiator and progression organism in Dental Caries?", "a": "Initiator: Streptococcus mutans (adherence via glucans and high acidogenicity); Progression: Lactobacillus species (aciduric propagation)."}
    ],
    "chap13_developmental_tooth_structure": [
        {"q": "What are the 3 major phenotypes of Amelogenesis Imperfecta (Witkop classification)?", "a": "1. Type I: Hypoplastic (quantitative enamel defect), 2. Type II: Hypocalcified (defective calcification, cheesy soft enamel), 3. Type III: Hypomaturation (defective crystal maturation, dull/mottled)."},
        {"q": "What clinical and radiographic triad characterizes Dentinogenesis Imperfecta (DI Type II)?", "a": "1. Opalescent amber/blue-brown translucent teeth, 2. Severe enamel shearing due to abnormal DEJ, 3. Radiographic bulbous crowns with cervical constriction and rapid obliteration of pulp chambers."},
        {"q": "What is 'Ghost Teeth'?", "a": "Regional Odontodysplasia — a localized non-hereditary disturbance affecting enamel, dentin, and pulp in one quadrant, producing marked radiolucency with thin fuzzy tooth shells."}
    ],
    "chap14_developmental_number_size": [
        {"q": "How do you clinically distinguish Gemination from Fusion?", "a": "Count the teeth: If the oversized tooth is counted as one and the total tooth count is NORMAL, it is Gemination (twinning). If total tooth count is REDUCED by one, it is Fusion."},
        {"q": "What is Dens Invaginatus (Dens in Dente) and its common site?", "a": "Invagination of the enamel organ into the dental papilla before calcification; most common in Maxillary Lateral Incisors (creates high risk of pulpal necrosis without caries)."},
        {"q": "What is Taurodontism and with which genetic conditions is it associated?", "a": "Bull-like teeth with enlarged pulp chambers, apical displacement of the pulpal floor, and lack of cervical constriction; associated with Klinefelter syndrome (XXY) and Down syndrome."}
    ],
    "chap15_developmental_jaws_soft_tissues": [
        {"q": "What triad constitutes the Pierre Robin Sequence?", "a": "1. Micrognathia (mandibular hypoplasia), 2. Glossoptosis (posteriorly displaced tongue), 3. U-shaped Cleft Palate with severe neonatal respiratory distress."},
        {"q": "What is Treacher Collins Syndrome (Mandibulofacial Dysostosis)?", "a": "Autosomal dominant disorder of 1st and 2nd branchial arches: Malar hypoplasia, downward slanting palpebral fissures, lower eyelid coloboma, microtia, and conductive deafness."},
        {"q": "What are Fordyce granules?", "a": "Ectopic, sebaceous glands appearing as asymptomatic yellowish-white papules on the buccal mucosa and vermilion border of the lips."}
    ],
    "chap16_bacterial_fungal_infections": [
        {"q": "What is the characteristic microscopic appearance of an oral Tuberculosis ulcer?", "a": "Caseating granulomatous inflammation with Langhans multinucleated giant cells, epithelioid histiocytes, and peripheral lymphocytic cuffing; acid-fast bacilli on Ziehl-Neelsen stain."},
        {"q": "What are 'Sulfur Granules' in Cervicofacial Actinomycosis?", "a": "Macroscopic yellowish colonies of entangled Gram-positive branching bacterial filaments (Actinomyces israelii) with radiating eosinophilic Splendore-Hoeppli clubs."},
        {"q": "Which special stains are utilized to highlight Candida hyphae and pseudohyphae?", "a": "Periodic Acid-Schiff (PAS) and Grocott-Gomori Methenamine Silver (GMS) stains."}
    ],
    "chap17_viral_infections": [
        {"q": "What are the 3 'M' cytological features of Herpes Simplex Virus in a Tzanck smear?", "a": "1. Multinucleation (syncytia), 2. Margination of chromatin, 3. Molding of adjacent nuclei with Cowdry type A eosinophilic intranuclear inclusions."},
        {"q": "What is Oral Hairy Leukoplakia (OHL) and its causative agent?", "a": "A non-wipeable, white, vertically corrugated hyperkeratotic plaque on the lateral borders of the tongue caused by Epstein-Barr Virus (EBV) in immunocompromised patients."},
        {"q": "Which Human Papillomavirus (HPV) genotypes are high-risk for Oropharyngeal Squamous Cell Carcinoma?", "a": "HPV-16 (accounting for >85% of HPV+ tonsillar and base-of-tongue cancers) and HPV-18."}
    ],
    "chap18_vesiculobullous_diseases": [
        {"q": "What is the diagnostic sign of Tzanck cells in Pemphigus Vulgaris?", "a": "Rounded, detached acantholytic keratinocytes with hyperchromatic nuclei and perinuclear halos floating in blister fluid due to loss of intercellular desmosomes."},
        {"q": "What is the classic histological finding in Erythema Multiforme?", "a": "Subepithelial/intraepithelial split with extensive apoptotic basal keratinocytes, subepidermal edema, and targetoid perivascular lymphocytic infiltrate."},
        {"q": "What is Desquamative Gingivitis and name its 3 most common causes?", "a": "A clinical presentation of erythematous, raw, desquamating attached gingiva. Causes: 1. Cicatricial Pemphigoid, 2. Oral Lichen Planus (erosive), 3. Pemphigus Vulgaris."}
    ],
    "chap19_bone_diseases": [
        {"q": "What is the characteristic histological description of woven bone in Fibrous Dysplasia?", "a": "'Chinese characters' or C-shaped curvilinear trabeculae of immature woven bone without osteoblastic rimming, set in a cellular fibrous stroma."},
        {"q": "What is the hallmark histopathological feature of Paget's Disease of Bone?", "a": "A 'Mosaic' or 'Jigsaw puzzle' pattern of lamellar bone demarcated by prominent, deeply basophilic Reversal Lines produced by waves of osteoclastic resorption and osteoblastic repair."},
        {"q": "What clinical triad defines McCune-Albright Syndrome?", "a": "1. Polyostotic Fibrous Dysplasia, 2. Café-au-lait skin pigmentation with irregular 'Coast of Maine' borders, 3. Autonomous endocrine hyperfunction (Precocious puberty)."}
    ],
    "chap20_forensic_odontology": [
        {"q": "Name the 6 criteria evaluated in Gustafson's dental age estimation method.", "a": "1. Attrition (A), 2. Periodontitis / Gingival attachment (P), 3. Secondary Dentin apposition (S), 4. Cementum apposition (C), 5. Root Resorption (R), 6. Root Dentin Transparency (T)."},
        {"q": "What is Cheiloscopy and Rugoscopy in forensic identification?", "a": "Cheiloscopy is the study of lip print patterns (Suzuki & Tsuchihashi classification); Rugoscopy is the study of palatal rugae patterns (stable, protected by tongue and buccal fat)."},
        {"q": "Why are teeth the single most reliable anatomical structure for post-mortem disaster victim identification (DVI)?", "a": "Enamel is the hardest tissue in the human body (96% mineralized), highly resistant to thermal destruction (up to 1,100°C), physical decomposition, and protects pulpal DNA."}
    ]
}

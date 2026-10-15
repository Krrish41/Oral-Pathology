# -*- coding: utf-8 -*-
"""
Oral Pathology & Microbiology: Interactive Dashboard Data
Contains interactive spotter flashcards, diagnostic calculators, comparison matrices, and viva quizzes.
"""

COMPARISON_MATRICES = [
    {
        "id": "matrix_cysts_tumors",
        "title": "Odontogenic Lesion Triad: Ameloblastoma vs. OKC vs. Dentigerous Cyst",
        "headers": ["Diagnostic Feature", "Conventional Ameloblastoma", "Odontogenic Keratocyst (OKC)", "Dentigerous Cyst"],
        "rows": [
            ["Primary Origin", "Enamel organ / Dental lamina remnants", "Dental lamina remnants (rests of Serres)", "Reduced Enamel Epithelium (REE)"],
            ["Usual Age & Gender", "30–50 years (Mean 35); M = F", "20–30 years; Slight Male predilection", "10–30 years; Male predilection (3:2)"],
            ["Predominant Site", "Mandible (80–85%), molar-ramus area", "Mandible (70–80%), angle and ramus", "Mandibular 3rd molar (70%), Maxillary canine"],
            ["Pattern of Expansion", "BUCCO-LINGUAL cortical expansion early", "ANTERO-POSTERIOR medullary expansion; minimal cortical expansion early", "Uniform slow expansion surrounding tooth crown"],
            ["Radiographic Hallmark", "Multilocular 'Soap-bubble' or 'Honeycomb' with knife-edge root resorption", "Multilocular or unilocular with smooth scalloped corticated margins; minimal resorption", "Unilocular pericoronal radiolucency attached at cementoenamel junction (CEJ)"],
            ["Lining / Epithelium", "Peripheral tall columnar cells (Vickers-Gorlin) + central stellate reticulum", "Uniform 6–8 cell layers of parakeratinized stratified squamous epithelium; wavy corrugation", "Thin 2–4 cell layers of non-keratinized cuboidal/columnar epithelium"],
            ["Basal Cell Layer", "Palisaded with reversed nuclear polarity & subnuclear vacuolization", "Palisaded hyperchromatic 'Picket-fence' or 'Tombstone' arrangement", "Flat, indistinct basal layer without palisading"],
            ["Lumen Contents", "Solid tumor / straw-colored cystic fluid", "Cheesy, foul-smelling keratin squames (low protein <4 g/dL)", "Clear, amber, transudative fluid with high protein"],
            ["Syndrome Association", "Rare", "Gorlin-Goltz Syndrome (Nevoid Basal Cell Carcinoma)", "Cleidocranial Dysplasia (multiple)"],
            ["Recurrence Rate", "60–90% with curettage; <5% with radical resection", "30–60% with enucleation; <10% with Carnoy's / ostectomy", "Extremely rare (<1%) with enucleation"],
            ["Definitive Surgery", "Segmental/marginal mandibulectomy (1-1.5 cm safe bone margin)", "Enucleation + Peripheral Ostectomy + Carnoy's solution / Cryotherapy", "Enucleation with extraction of the impacted unerupted tooth"]
        ]
    },
    {
        "id": "matrix_pemphigus_pemphigoid",
        "title": "Vesiculobullous Master Matrix: Pemphigus Vulgaris vs. Mucous Membrane Pemphigoid",
        "headers": ["Clinical / Pathological Marker", "Pemphigus Vulgaris", "Mucous Membrane Pemphigoid (Cicatricial)"],
        "rows": [
            ["Target Autoantigen", "Desmoglein 3 (oral) & Desmoglein 1 (skin)", "BP180 (Type XVII Collagen), BP230, Laminin 332 (Laminin 5)"],
            ["Ultrastructural Target", "Desmosomes (intercellular spinous adherence)", "Hemidesmosomes & Basement Membrane Zone (BMZ)"],
            ["Histological Level of Split", "INTRAPITHELIAL (Suprabasal Cleavage)", "SUBEPITHELIAL (Lamina Lucida / BMZ Cleavage)"],
            ["Bulla Morphology", "Thin-roofed, flaccid, fragile; bursts immediately leaving ragged raw ulcers", "Thick-roofed, tense; persists intact for days before rupturing"],
            ["Tzanck Smear Cytology", "POSITIVE: Abundant rounded, nucleated acantholytic Tzanck cells", "NEGATIVE: No acantholytic cells (only normal intact cells + PMNs)"],
            ["Tombstone Appearance", "Present: Single row of intact basal cells attached to basement membrane", "Absent: Entire basal layer lifts up with the epithelial roof"],
            ["Direct Immunofluorescence (DIF)", "Intercellular 'FISHNET' or 'CHICKEN-WIRE' IgG & C3 pattern in spinous layer", "Continuous smooth LINEAR BAND of IgG & C3 along the Basement Membrane"],
            ["Oral Mucosal Involvement", "First site of presentation in 70% ('First to show, last to go')", "Classic Desquamative Gingivitis (erythematous attached gingiva)"],
            ["Ocular Involvement", "Rare (<5%), non-scarring conjunctivitis", "HIGH RISK (Symblepharon, entropion, trichiasis, corneal opacity, blindness)"],
            ["Nikolsky Sign", "Strongly Positive", "Positive on perilesional gingiva"],
            ["Primary Medical Therapy", "High-dose Systemic Corticosteroids (Prednisone 1-2 mg/kg) + Rituximab/Azathioprine", "Topical potent steroids (Clobetasol gel); Dapsone / Systemic steroids if ocular"]
        ]
    },
    {
        "id": "matrix_fibrous_paget",
        "title": "Fibro-Osseous & Metabolic Matrix: Fibrous Dysplasia vs. Paget's Disease of Bone",
        "headers": ["Parameter", "Fibrous Dysplasia (Monostotic/Polyostotic)", "Paget's Disease of Bone (Osteitis Deformans)"],
        "rows": [
            ["Etiology & Genetics", "Postzygotic activating somatic mutation in GNAS gene (chromosome 20q13)", "Genetic (SQSTM1 mutation) + Slow viral infection (Paramyxovirus/Measles)"],
            ["Typical Age of Onset", "Children & young adults (1st–2nd decade; halts after puberty)", "Elderly adults (>60 years; progressive lifelong disease)"],
            ["Jaw Predilection", "Maxilla affected twice as often as Mandible", "Maxilla affected much more commonly than Mandible"],
            ["Facial Presentation", "Unilateral painless facial asymmetry; orbital displacement", "Bilateral symmetrical enlargement (Leontiasis ossea; 'Dentures too tight')"],
            ["Skull / Cranial Signs", "Bulging cortex; sphenoid/ethmoid sclerosis", "Massive cranium enlargement ('Hat size increases'); cranial nerve compressions"],
            ["Radiographic Texture", "'Ground-Glass', 'Orange-Peel' (Peau d'orange), blending imperceptibly", "Triphasic: Osteolytic -> Mixed -> 'Cotton-Wool' radiopaque clumps"],
            ["Dental Radiograph", "Loss of lamina dura; displacement of tooth roots", "Generalized HYPERCEMENTOSIS and loss of lamina dura"],
            ["Histological Pattern", "'Chinese Characters' curvilinear woven bone WITHOUT osteoblastic rimming", "'Jigsaw Puzzle' / 'Mosaic' lamellar bone with deeply basophilic reversal lines"],
            ["Serum Alkaline Phosphatase", "Normal (or slightly elevated during rapid growth)", "MARKATELY ELEVATED (10 to 20 times normal limit)"],
            ["Malignant Risk", "Rare (<1%, often following obsolete radiation)", "Significant (~1% progress to highly aggressive Osteosarcoma)"]
        ]
    }
]

SPOTTER_CARDS = [
    {
        "id": "spotter_vickers_gorlin",
        "title": "Vickers-Gorlin Sign",
        "condition": "Ameloblastoma (Follicular Variant)",
        "features": [
            "Peripheral tall columnar cells resembling pre-ameloblasts.",
            "Basal palisading with hyperchromatic nuclei.",
            "Reversed nuclear polarity (nuclei oriented away from basement membrane).",
            "Subnuclear cytoplasmic vacuolization.",
            "Central core of loose stellate cells resembling stellate reticulum."
        ],
        "viva_tip": "Vickers-Gorlin criteria are essential to distinguish true ameloblastoma islands from non-neoplastic odontogenic rests or cystic linings."
    },
    {
        "id": "spotter_liesegang_rings",
        "title": "Liesegang Rings & Apple-Green Birefringence",
        "condition": "Calcifying Epithelial Odontogenic Tumor (CEOT / Pindborg Tumor)",
        "features": [
            "Sheets and polyhedral islands of eosinophilic epithelial cells with prominent intercellular bridges.",
            "Globular extracellular eosinophilic amyloid-like proteinaceous material.",
            "Congo Red positive exhibiting pathognomonic Apple-Green Birefringence under polarized light.",
            "Concentric calcified calcospherites known as Liesegang Rings."
        ],
        "viva_tip": "Pindborg tumor is famous for nuclear pleomorphism without clinical malignancy! The amyloid-like protein is derived from ameloblast-associated odontogenic protein (ODAM)."
    },
    {
        "id": "spotter_okc_picket_fence",
        "title": "Corrugated Parakeratin & Picket-Fence Basal Layer",
        "condition": "Odontogenic Keratocyst (OKC / KCOT)",
        "features": [
            "Uniform 6 to 8 cell layers thickness of stratified squamous epithelium.",
            "Prominent, wavy, corrugated parakeratinized luminal surface.",
            "Palisaded basal layer with polarized, hyperchromatic cylindrical nuclei ('Picket-fence' or 'Tombstone' pattern).",
            "Flat epithelial-connective tissue interface lacking rete pegs.",
            "Detachment of epithelial lining from underlying fibrous capsule."
        ],
        "viva_tip": "The thin friable lining and micro-satellite/daughter cysts in the capsule explain the notorious 30-60% recurrence rate if enucleated without chemical cauterization (Carnoy's solution)."
    },
    {
        "id": "spotter_pleomorphic_adenoma",
        "title": "Chondromyxoid Stroma & Plasmacytoid Myoepithelial Cells",
        "condition": "Pleomorphic Adenoma (Benign Mixed Tumor)",
        "features": [
            "Ductal epithelial structures containing eosinophilic PAS-positive coagulum.",
            "Proliferation of myoepithelial cells with plasmacytoid (eccentric nucleus) and spindle morphologies.",
            "Extensive loose basophilic chondromyxoid matrix with myoepithelial cells residing within false chondroid lacunae.",
            "Incomplete pseudocapsule with microscopic bosselated pseudopods."
        ],
        "viva_tip": "Enucleation is strictly contraindicated due to capsular pseudopods; superficial parotidectomy with facial nerve preservation is mandatory!"
    },
    {
        "id": "spotter_adenoid_cystic",
        "title": "Cribriform 'Swiss-Cheese' Pattern & Perineural Infiltration",
        "condition": "Adenoid Cystic Carcinoma (AdCC / Cylindroma)",
        "features": [
            "Basaloid tumor cells arranged in large nests punched out by rounded cylindrical spaces ('Swiss-Cheese' or Cribriform pattern).",
            "Cylindrical pseudocysts contain reduplicated basement membrane material and basophilic glycosaminoglycans.",
            "Remarkable Neurotropism: Infiltration into epineurium and perineural spaces of peripheral nerves.",
            "High late distant metastasis to lungs (cannonball metastases)."
        ],
        "viva_tip": "Patients present with unprovoked pain and numbness before a palpable lump appears due to early perineural invasion."
    },
    {
        "id": "spotter_chinese_letter",
        "title": "Chinese Letter Pattern without Osteoblastic Rimming",
        "condition": "Fibrous Dysplasia (FD)",
        "features": [
            "Cellular fibrous connective tissue stroma composed of benign spindle fibroblasts.",
            "Irregular, curvilinear, C-shaped or fishhook-shaped trabeculae of immature woven bone.",
            "Resembles Chinese ideograms / Chinese alphabet characters.",
            "Complete ABSENCE of osteoblastic rimming along the margins of woven bone trabeculae.",
            "Radiograph shows ground-glass or orange-peel opacity blending imperceptibly into normal bone."
        ],
        "viva_tip": "Driven by activating somatic mutations in GNAS (chromosome 20q13). McCune-Albright syndrome includes polyostotic FD + café-au-lait spots + precocious puberty."
    },
    {
        "id": "spotter_mosaic_paget",
        "title": "Mosaic (Jigsaw Puzzle) Pattern with Reversal Lines",
        "condition": "Paget's Disease of Bone (Osteitis Deformans)",
        "features": [
            "Thick, chaotic trabeculae of lamellar bone.",
            "Prominent, scalloped, deeply basophilic Reversal Lines demarcating previous bone resorption bays.",
            "Gives bone a classic Jigsaw-Puzzle or Mosaic tile appearance.",
            "Highly vascular osteogenic fibrous marrow spaces.",
            "Teeth demonstrate striking generalized Hypercementosis on radiographs."
        ],
        "viva_tip": "Serum Alkaline Phosphatase is massively elevated (10-20x normal), but serum calcium and phosphate are normal! Carries a 1% risk of transformation to osteosarcoma."
    },
    {
        "id": "spotter_saw_tooth_lichen",
        "title": "Saw-Tooth Rete Pegs & Civatte Bodies",
        "condition": "Oral Lichen Planus (OLP)",
        "features": [
            "Hyperparakeratosis or hyperorthokeratosis with granular layer thickening.",
            "Hydropic degeneration and liquefaction necrosis of the basal cell layer.",
            "Pointed, triangular 'Saw-Tooth' rete ridges.",
            "Civatte (colloid/cytoid) bodies: Shrunken apoptotic basal keratinocytes extruded into superficial dermis.",
            "Dense, band-like horizontal T-lymphocytic infiltrate strictly hugging the basement membrane."
        ],
        "viva_tip": "Direct Immunofluorescence (DIF) shows shaggy deposition of Fibrinogen along the basement membrane zone. Wickham's striae present bilaterally on posterior buccal mucosa."
    },
    {
        "id": "spotter_tzanck_acantholysis",
        "title": "Suprabasal Cleft & Acantholytic Tzanck Cells",
        "condition": "Pemphigus Vulgaris",
        "features": [
            "Intraepithelial suprabasal split due to loss of desmosomal adhesion (acantholysis).",
            "Single intact row of basal cells attached to basement membrane ('Row of Tombstones').",
            "Rounded, detached acantholytic Tzanck cells with hyperchromatic nuclei floating in vesicle fluid.",
            "DIF reveals intercellular 'Fishnet' or 'Chicken-wire' pattern of IgG and C3 throughout spinous layer."
        ],
        "viva_tip": "Autoantibodies target Desmoglein 3 (oral) and Desmoglein 1 (skin). Nikolsky sign is positive. Oral lesions precede skin blisters in 70% of cases!"
    },
    {
        "id": "spotter_sulfur_granule",
        "title": "Sulfur Granule & Splendore-Hoeppli Phenomenon",
        "condition": "Cervicofacial Actinomycosis ('Lumpy Jaw')",
        "features": [
            "Macroscopic 1 to 2 mm yellowish-tan colony of entangled bacterial filaments.",
            "Central Gram-positive branching filamentous organisms (Actinomyces israelii).",
            "Radiating, club-shaped eosinophilic peripheral fringe representing host immunoglobulins (Splendore-Hoeppli phenomenon).",
            "Surrounded by a dense sea of neutrophils forming acute microabscesses.",
            "Multiple cutaneous draining sinuses over the angle of the mandible."
        ],
        "viva_tip": "Actinomyces is a Gram-positive anaerobic BACTERIUM, not a fungus! Treatment requires prolonged high-dose Penicillin (6 to 12 months)."
    },
    {
        "id": "spotter_verocay_bodies",
        "title": "Antoni A Areas & Verocay Bodies",
        "condition": "Schwannoma (Neurilemoma)",
        "features": [
            "Encapsulated benign neural sheath neoplasm arising from Schwann cells.",
            "Antoni A Areas: Densely cellular regions of spindle cells with palisading nuclei.",
            "Verocay Bodies: Eosinophilic, acellular zones consisting of cytoplasmic processes bordered on both sides by parallel palisading nuclei.",
            "Antoni B Areas: Hypocellular, loose, myxoid disorganized tissue with microcysts."
        ],
        "viva_tip": "The tongue is the most common intraoral site. In contrast to Neurofibroma, Schwannoma is encapsulated and can be shelled out without sacrificing the nerve trunk."
    }
]

VIVA_QUIZ = [
    {
        "question": "Which of the following is the single most reliable histological sign of Ameloblastoma?",
        "options": [
            "Acanthomatous squamous metaplasia",
            "Vickers-Gorlin sign with reversed nuclear polarity",
            "Liesegang concentric calcifications",
            "Granular eosinophilic cytoplasm"
        ],
        "correct": 1,
        "explanation": "The Vickers-Gorlin sign (peripheral tall columnar cells with palisaded basal nuclei, reversed nuclear polarity, and subnuclear vacuolization) is the pathognomonic diagnostic criterion for ameloblastoma."
    },
    {
        "question": "In Gustafson's method of adult age estimation, which parameter exhibits the highest individual correlation with chronological age?",
        "options": [
            "Masticatory Attrition (A)",
            "Periodontal Attachment Loss (P)",
            "Secondary Dentin Apposition (S)",
            "Root Dentin Transparency / Sclerosis (T)"
        ],
        "correct": 3,
        "explanation": "Root Dentin Transparency (T) has the highest statistical correlation with age because peritubular hydroxyapatite deposition occurs continuously with time and is unaffected by diet, habits, or periodontal disease."
    },
    {
        "question": "An incisional biopsy of a palatal mass shows sheets of basaloid cells with numerous cylindrical spaces containing basophilic mucin ('Swiss-cheese' pattern) and tumor cells tracking along the perineurium. What is the diagnosis?",
        "options": [
            "Pleomorphic Adenoma",
            "Mucoepidermoid Carcinoma",
            "Adenoid Cystic Carcinoma",
            "Warthin's Tumor"
        ],
        "correct": 2,
        "explanation": "Adenoid Cystic Carcinoma (AdCC) characteristically presents with the Cribriform ('Swiss-cheese') pattern and an extreme propensity for Perineural Invasion (neurotropism)."
    },
    {
        "question": "A patient presents with fragile oral erosions. Direct Immunofluorescence demonstrates intercellular 'fishnet' IgG deposition in the spinous layer. What is the molecular target of the autoantibodies?",
        "options": [
            "Desmoglein 3 (Dsg3)",
            "Bullous Pemphigoid Antigen 180 (BP180)",
            "Laminin 332 (Laminin 5)",
            "Type VII Collagen"
        ],
        "correct": 0,
        "explanation": "Pemphigus Vulgaris produces autoantibodies against Desmoglein 3 (and Desmoglein 1 in mucocutaneous forms), resulting in suprabasal acantholysis and the classic intercellular fishnet DIF pattern."
    },
    {
        "question": "Which histological feature definitively excludes a diagnosis of Fibrous Dysplasia?",
        "options": [
            "Immature woven bone trabeculae",
            "Curvilinear 'Chinese character' trabecular shapes",
            "Prominent osteoblastic rimming along all bony trabeculae",
            "Cellular fibrous connective tissue stroma"
        ],
        "correct": 2,
        "explanation": "Fibrous Dysplasia is characterized by the ABSENCE of osteoblastic rimming. The presence of prominent osteoblastic rimming strongly suggests Ossifying Fibroma or osteoma, not Fibrous Dysplasia."
    },
    {
        "question": "What is the critical pH at which human enamel calcium hydroxyapatite begins to dissolve during a carious attack?",
        "options": [
            "pH 6.8",
            "pH 6.2",
            "pH 5.5",
            "pH 4.0"
        ],
        "correct": 2,
        "explanation": "The critical pH for enamel dissolution is pH 5.5. In contrast, cementum and root dentin demineralize at a much less acidic pH of 6.2 to 6.7."
    }
]

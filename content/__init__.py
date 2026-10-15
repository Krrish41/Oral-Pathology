# -*- coding: utf-8 -*-
"""
Oral Pathology & Microbiology Master Content Package
Consolidates all 20 high-yield chapters across 4 clinical domains.
"""

from .odontogenic_cysts_and_tumors import CHAPTERS as c1
from .caries_and_developmental import CHAPTERS as c2
from .salivary_and_neoplasms import CHAPTERS as c3
from .infections_blood_bone_forensic import CHAPTERS as c4

CHAPTERS = c1 + c2 + c3 + c4

__all__ = ["CHAPTERS"]

#!/usr/bin/env python3
"""
Deeper organization of assets/case-studies/Other/ into subcategories.
"""

import re
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OTHER_DIR = BASE / "assets" / "case-studies" / "Other"

# Subcategory rules: (pattern, subdir_name) — order matters, first match wins
RULES = [
    (r"\bexchange\b", "Infrastructure Exchange"),
    (r"infastructure|intrastructure|infrastructure\b", "Infrastructure"),
    (r"\bdlp\b|azure\b", "Infrastructure Security"),
    (r"\bbpo\b|proposal\s*template", "BPO Proposals"),
    (r"power\s*suite|power\s*apps|power\s*platform|viva\b", "Power Platform Viva"),
    (r"d365|dynamics|acumatica\b", "CRM Dynamics"),
    (r"city\s+of|county\b|arapahoe|port\s+of|tualatin|ramsey|king\s+county|government", "Government"),
    (r"health\b|kaiser|casey\s*family|evergreen", "Healthcare"),
    (r"college|university|foundation\s+and\s+alumni|nii\s*mbl", "Education"),
    (r"credit\s+union|bank\b|peoples\s+bank|selco|solarity|hawaii\s+bank|chevron\s+credit", "Financial Services"),
    (r"insurance\b|alaska\s*national", "Insurance"),
    (r"signage|recording|product\s*promos|event\s*support|social\s*media|boosted\s*post|catalog\b|logo\s*examples", "Creative Events"),
    (r"data\s*mart|dashboard\b|oem\s*.*data|data\s*and\s*analytics", "Data Analytics"),
    (r"msft_|microsoft", "Microsoft Customer Stories"),
    (r"contract\s*management", "Proposals"),
    (r"zen\s*desk|zendesk", "Custom Dev Integrations"),
    (r"sharepoint|ppe\s*management|resource\s*management", "Modern Workplace"),
    (r"mobility|sustainability|lenovo|power\s*platform\s*customer", "Microsoft Customer Stories"),
    (r"foundation\b|cystic\s*fibrosis|mary['\s]*s\s*place|degrees\s*of\s*change|ymca\b", "Non-Profit"),
    (r"asset\s*hub|lab\s*hub|market\s*insights|standards\s*hub|reels|mcc\s*reels", "Creative Hubs"),
    (r"dupont|hydac|resco|manufacturing", "Manufacturing"),
    (r"msft\b|da\s*msft|xbox|nbc\s*universal", "Microsoft Customer Stories"),
    (r"paid\s*ads|ppc\s*case", "Marketing"),
    (r"office\s*insiders|accessibility|compliance", "Modern Workplace Compliance"),
    (r"ferguson|bernhard", "Construction"),
    (r"\bchevron\b", "Energy"),
    (r"avista\b", "Utilities"),
    (r"trupanion", "Insurance"),
    (r"\brei\b", "Retail"),
    (r"\bsso\b", "Infrastructure Security"),
]

def classify(name: str) -> str:
    n = name.lower().replace("\xe2\x80\x93", "-")
    for pat, subdir in RULES:
        if re.search(pat, n, re.I):
            return subdir
    return "General"


def main():
    if not OTHER_DIR.exists():
        print(f"Missing {OTHER_DIR}")
        return
    files = list(OTHER_DIR.rglob("*.pptx")) + list(OTHER_DIR.rglob("*.docx")) + list(OTHER_DIR.rglob("*.pdf"))
    moves = []
    for f in files:
        sub = classify(f.stem + " " + f.name)
        subdir = OTHER_DIR / sub
        subdir.mkdir(exist_ok=True)
        dest = subdir / f.name
        if f.parent != subdir:
            moves.append((f, dest))
    for src, dest in moves:
        subprocess.run(["git", "mv", str(src), str(dest)], cwd=BASE, check=False)
    print(f"Moved {len(moves)} files into subcategories")
    for d in sorted(OTHER_DIR.iterdir()):
        if d.is_dir():
            n = len(list(d.glob("*")))
            print(f"  {d.name}: {n}")


if __name__ == "__main__":
    main()

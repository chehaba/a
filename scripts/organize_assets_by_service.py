#!/usr/bin/env python3
"""
Organize assets/case-studies by service. Creates subdirs and moves PPTXs.
Run from repo root. Uses same service extraction as parse_all_case_studies.
"""

import re
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ASSETS = BASE / "assets"
CASE_STUDIES = ASSETS / "case-studies"

SERVICE_DIRS = {
    "Modern Workplace": "Modern Workplace",
    "CRM": "CRM",
    "Data & Analytics": "Data Analytics",
    "Marketing": "Marketing",
    "Custom Dev": "Custom Dev",
    "AI / Automation": "AI Automation",
    "Infrastructure": "Infrastructure",
    "Creative": "Creative",
    "Other": "Other",
}


def get_service(path: Path) -> str:
    name = path.stem.replace("–", "-").replace("—", "-").lower() + " " + path.name.lower()
    if "sharepoint" in name or " spo " in name or " sp " in name or "m365" in name or "o365" in name or "teams" in name or "intranet" in name:
        return "Modern Workplace"
    if "salesforce" in name or "dynamics" in name or "crm" in name:
        return "CRM"
    if " bi " in name or " - bi" in name or "power bi" in name or "snowflake" in name or "data warehouse" in name:
        return "Data & Analytics"
    if "marketing" in name or "hubspot" in name or "pardot" in name or "marketo" in name or "ppc" in name or "seo" in name:
        return "Marketing"
    if "custom dev" in name or "mobile" in name or " application" in name or "portal" in name:
        return "Custom Dev"
    if " ai " in name or "copilot" in name or "agent" in name:
        return "AI / Automation"
    if "infrastructure" in name or "mdm" in name or "intune" in name or "sccm" in name:
        return "Infrastructure"
    if "creative" in name or "video" in name or "webinar" in name or "graphic" in name:
        return "Creative"
    if "website" in name or "sitefinity" in name:
        return "Creative"
    if "governance" in name or "migration" in name:
        return "Modern Workplace"
    return "Other"


def main():
    CASE_STUDIES.mkdir(parents=True, exist_ok=True)
    for d in SERVICE_DIRS.values():
        (CASE_STUDIES / d).mkdir(exist_ok=True)

    moves = []
    for f in sorted(ASSETS.glob("*.pptx")):
        svc = get_service(f)
        dest_dir = CASE_STUDIES / SERVICE_DIRS.get(svc, "Other")
        dest = dest_dir / f.name
        if f.parent != dest_dir:
            moves.append((f, dest))

    print(f"Will move {len(moves)} files")
    for src, dest in moves:
        src_rel = src.relative_to(BASE)
        dest_rel = dest.relative_to(BASE)
        subprocess.run(["git", "mv", str(src_rel), str(dest_rel)], cwd=BASE, check=False)
    print("Done. Run: git status")


if __name__ == "__main__":
    main()

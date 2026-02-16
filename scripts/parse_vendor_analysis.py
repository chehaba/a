#!/usr/bin/env python3
"""
Parse vendor_channel_persona_service_analysis.xlsx and output key insights.
Regenerates summary for reports/Vendor Channel Persona Service Analysis Report.md context.
"""

import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
XLSX = BASE / "data" / "vendor_channel_persona_service_analysis.xlsx"


def main():
    if not XLSX.exists():
        print(f"Missing {XLSX}")
        return
    xl = pd.ExcelFile(XLSX, engine="openpyxl")
    ch = pd.read_excel(xl, sheet_name="Channel_Baselines")
    vendor = pd.read_excel(xl, sheet_name="Vendor_SourceCampaign")
    seg = pd.read_excel(xl, sheet_name="Segments_Channel")
    lev = pd.read_excel(xl, sheet_name="Logistic_Levers")
    leads = pd.read_excel(xl, sheet_name="Leads_Last12mo")

    print("CHANNEL BASELINES")
    print(ch.to_string())
    print("\nVENDOR/SOURCE RECOMMENDATIONS")
    print(vendor.to_string())
    print("\nRUN/TEST SEGMENTS")
    rt = seg[seg["Recommendation"].isin(["Run", "Test"])]
    print(rt.sort_values(["Channel", "win_rate"], ascending=[True, False]).to_string())
    print("\nLOGISTIC LEVERS (top 10)")
    print(lev.head(10).to_string())
    print("\nLEADS LAST 12mo")
    print(leads.to_string())


if __name__ == "__main__":
    main()

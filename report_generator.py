import os
from datetime import datetime

def generate_report(company_name, violations, score):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{company_name}_report.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== IT ACT COMPLIANCE REPORT ===\n\n")
        f.write(f"Company: {company_name}\n")
        f.write(f"Date: {datetime.now()}\n\n")

        f.write(f"Compliance Score: {score}%\n\n")

        if not violations:
            f.write("Company is fully compliant.\n")
        else:
            f.write("Violations Found:\n\n")
            for i, v in enumerate(violations, 1):
                f.write(f"{i}. Issue: {v['issue']}\n")
                f.write(f"   Law: {v['law']}\n")
                f.write(f"   Penalty: {v['penalty']}\n\n")

    print(f"\n📄 Report saved: {filename}")
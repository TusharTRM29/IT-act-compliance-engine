from rules import check_compliance
from report_generator import generate_report
from input_handler import get_user_input
from test_profiles import startup_unsafe, startup_safe, medium_company

def run_audit(company_name, profile):
    print(f"\n🔍 Auditing: {company_name}")

    violations, score = check_compliance(profile)

    print(f"Compliance Score: {score}%")

    if not violations:
        print("✅ No violations found")
    else:
        print("❌ Violations:")
        for v in violations:
            print(f"- {v['issue']} ({v['law']})")

    generate_report(company_name, violations, score)


if __name__ == "__main__":
    print("1. Run Test Cases")
    print("2. Enter Custom Company Data")

    choice = input("Select option: ")

    if choice == "1":
        run_audit("Unsafe_Startup", startup_unsafe)
        run_audit("Safe_Startup", startup_safe)
        run_audit("Medium_Company", medium_company)

    elif choice == "2":
        name = input("Enter company name: ")
        profile = get_user_input()
        run_audit(name, profile)

    else:
        print("Invalid choice")
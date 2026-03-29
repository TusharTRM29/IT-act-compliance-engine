def check_compliance(profile):
    violations = []
    total_rules = 5
    broken = 0

    if profile.get("plaintext_passwords"):
        broken += 1
        violations.append({
            "issue": "Passwords stored in plaintext",
            "law": "IT Act 2000 - Section 43A",
            "penalty": "Compensation for negligence"
        })

    if not profile.get("data_encryption"):
        broken += 1
        violations.append({
            "issue": "No data encryption",
            "law": "IT Amendment 2008",
            "penalty": "Data breach risk"
        })

    if not profile.get("user_consent"):
        broken += 1
        violations.append({
            "issue": "User consent not taken",
            "law": "IT Privacy Rules",
            "penalty": "Legal penalty"
        })

    if not profile.get("data_breach_policy"):
        broken += 1
        violations.append({
            "issue": "No breach response policy",
            "law": "IT Security Guidelines",
            "penalty": "Non-compliance"
        })

    if not profile.get("firewall"):
        broken += 1
        violations.append({
            "issue": "Firewall not implemented",
            "law": "Reasonable Security Practices",
            "penalty": "System vulnerable"
        })

    score = ((total_rules - broken) / total_rules) * 100

    return violations, score
startup_unsafe = {
    "plaintext_passwords": True,
    "data_encryption": False,
    "user_consent": False,
    "data_breach_policy": False,
    "firewall": False
}

startup_safe = {
    "plaintext_passwords": False,
    "data_encryption": True,
    "user_consent": True,
    "data_breach_policy": True,
    "firewall": True
}

medium_company = {
    "plaintext_passwords": False,
    "data_encryption": True,
    "user_consent": False,
    "data_breach_policy": False,
    "firewall": True
}
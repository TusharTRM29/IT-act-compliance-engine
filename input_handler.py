def get_user_input():
    profile = {}

    def ask(question):
        while True:
            ans = input(question + " (yes/no): ").strip().lower()
            if ans in ["yes", "no"]:
                return ans == "yes"
            else:
                print("❌ Please enter only 'yes' or 'no'")

    print("\nEnter Company Security Details:")

    profile["plaintext_passwords"] = ask("Passwords stored in plaintext?")
    profile["data_encryption"] = ask("Data encrypted?")
    profile["user_consent"] = ask("User consent taken?")
    profile["data_breach_policy"] = ask("Breach policy available?")
    profile["firewall"] = ask("Firewall enabled?")

    return profile
import re

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty",
    "admin", "welcome", "letmein", "iloveyou"
]

def check_password(password):
    score = 0
    issues = []

    # Length check
    if len(password) < 8:
        score += 30
        issues.append("Password is too short (less than 8 characters)")

    # Uppercase
    if not re.search(r"[A-Z]", password):
        score += 15
        issues.append("No uppercase letter")

    # Lowercase
    if not re.search(r"[a-z]", password):
        score += 15
        issues.append("No lowercase letter")

    # Number
    if not re.search(r"[0-9]", password):
        score += 15
        issues.append("No number")

    # Special character
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 15
        issues.append("No special character")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score += 50
        issues.append("Password is commonly used and easily guessable")

    # Risk level
    if score >= 60:
        level = "HIGH RISK"
    elif score >= 30:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return score, level, issues


if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    score, level, issues = check_password(pwd)

    print("\nPassword Risk Report")
    print("--------------------")
    print("Risk Level:", level)
    print("Risk Score:", score)

    if issues:
        print("\nIssues found:")
        for i in issues:
            print("-", i)
    else:
        print("\nStrong password. No major issues found.")

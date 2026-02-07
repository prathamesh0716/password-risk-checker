from flask import Flask, render_template, request
import re

app = Flask(__name__)

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty",
    "admin", "welcome", "letmein", "iloveyou"
]

def check_password(password):
    score = 0
    issues = []

    if len(password) < 8:
        score += 30
        issues.append("Password is too short (less than 8 characters)")

    if not re.search(r"[A-Z]", password):
        score += 15
        issues.append("No uppercase letter")

    if not re.search(r"[a-z]", password):
        score += 15
        issues.append("No lowercase letter")

    if not re.search(r"[0-9]", password):
        score += 15
        issues.append("No number")

    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 15
        issues.append("No special character")

    if password.lower() in COMMON_PASSWORDS:
        score += 50
        issues.append("Password is commonly used and easily guessable")

    if score >= 60:
        level = "HIGH RISK"
    elif score >= 30:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return score, level, issues

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        score, level, issues = check_password(password)
        result = {
            "score": score,
            "level": level,
            "issues": issues
        }
    return render_template("index.html", result=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

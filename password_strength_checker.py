import re

def check_strength(password):
    length = len(password) >= 8
    upper = bool(re.search(r"[A-Z]", password))
    lower = len(re.findall(r"[a-z]", password)) >= 3
    digit = bool(re.search(r"\d", password))
    special = bool(re.search(r"[!@#$%^&*()_+?><\":|}{~`/.,';\[\]\\]", password))

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

while True:
    pwd = input("Enter a password (or type 'exit' to quit): ")
    if pwd.lower() == 'exit':
        break
    strength = check_strength(pwd)
    print(f"💡 Password Strength: {strength}\n")

import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Lowercase Check
    if re.search("[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.\n"

    # Uppercase Check
    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"

    # Digit Check
    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks += "Add at least one number.\n"

    # Special Character Check
    if re.search("[@#$%^&*]", password):
        strength += 1
    else:
        remarks += "Add at least one special character (@#$%^&*).\n"

    # Strength Result
    if strength == 5:
        return "Strong Password", remarks
    elif strength >= 3:
        return "Medium Password", remarks
    else:
        return "Weak Password", remarks


# Main Program
password = input("Enter your password: ")
result, suggestions = check_password_strength(password)

print("\nPassword Strength:", result)

if suggestions:
    print("\nSuggestions to Improve:")
    print(suggestions)
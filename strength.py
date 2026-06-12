import string

def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 12:
        score += 1
    if len(password) >= 20:
        score += 1

    if score <= 2:
        return "WEAK"
    elif score <= 4:
        return "MEDIUM"
    else:
        return "STRONG"
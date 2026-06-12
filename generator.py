import random
import string
from utils import ask_yes_no


def generate_password():
    while True:
        length = input("Password length (1-100): ")

        if not length.isdigit():
            print("Enter a number.")
            continue

        length = int(length)

        if 1 <= length <= 100:
            break

        print("Range: 1-100")

    lower = ask_yes_no("Lowercase? (y/n): ")
    upper = ask_yes_no("Uppercase? (y/n): ")
    digits = ask_yes_no("Digits? (y/n): ")
    symbols = ask_yes_no("Symbols? (y/n): ")

    pools = []

    if lower:
        pools.append(string.ascii_lowercase)
    if upper:
        pools.append(string.ascii_uppercase)
    if digits:
        pools.append(string.digits)
    if symbols:
        pools.append(string.punctuation)

    if not pools:
        print("Select at least one option.")
        return generate_password()

    password = [random.choice(pool) for pool in pools]

    all_chars = "".join(pools)
    password += [random.choice(all_chars) for _ in range(length - len(password))]

    random.shuffle(password)

    return "".join(password)
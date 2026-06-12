from datetime import datetime

FILE = "history.txt"


def save_password(password):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE, "a") as f:
        f.write(f"{time} | {password}\n")
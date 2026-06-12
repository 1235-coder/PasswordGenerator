def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes", "t", "tak"):
            return True
        if answer in ("n", "no", "nie"):
            return False

        print("Answer y/n.")
from generator import generate_password
from history import save_password
from utils import ask_yes_no
from strength import check_strength
import pyperclip


def menu():
    while True:
        print("\n=== PASSWORD GENERATOR ===")
        print("1. Generate password")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            password = generate_password()

            print(f"\nGenerated password: {password}")

            strength = check_strength(password)
            print(f"Strength: {strength}")

            try:
                pyperclip.copy(password)
                print("Copied to clipboard!")
            except:
                print("Clipboard error.")

            save_password(password)

            input("\nPress Enter to continue...")

        elif choice == "2":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
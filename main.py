from get_len import get_len
from pass_gen import pass_gen
from get_choice import get_choice
import pyperclip

def main():
    print("--------Password generator--------")
    while True:
        length = get_len()
        password = pass_gen(length)
        print(f"\nYour password is: {password}\n")
        choice = get_choice()

        if choice == 1:
            pyperclip.copy(password)
            print("Text copied!")

            if input("New password? (Y)es or (N)o------>").lower()[0] == 'y':
                continue
            else:
                break

        if choice == 2:
            continue

        if choice == 3:
            print("Bye!")
            break

if __name__ == '__main__':
    main()

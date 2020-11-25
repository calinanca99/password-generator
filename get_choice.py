def get_choice():
    while True:
        try:
            choice = int(input("Please choose:\n1.Copy to clipboard.\n2.Generate new password.\n3.Quit.\n------>"))

        except:
            print("Please choose a number.")
            continue

        else:
            if choice == 1 or choice == 2 or choice == 3:
                return choice

            else:
                print("Please pick one of the available options.")
                continue

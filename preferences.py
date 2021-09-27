def set_length():
    """
    Sets the length of the password.

    The length is passed as an integer and must be between 8 and 128 characters.
    """
    print("You need to select the length of your password.")
    while True:
        try:
            length = int(input("Please enter a number between 8 and 128: "))
        except:
            print("Please insert a number.")
            continue
        else:
            if length >= 8 and length <=128:
                return length
            else:
                print("The length must be between 8 and 128.")
                continue

def set_preferences():
    """
    Sets the preferences for the password; e.g.: to include (or not) symbolds, digits and lower or UPPER case.

    At least one preference has to be chosen.
    """
    symbols = False
    digits = False
    lower = False
    upper = False

    while not symbols and not digits and not lower and not upper:
        try:
            if input("Do you want to include symbols? (Y)es or (N)o: ").lower()[0] == 'y':
                symbols = True
            if input("Do you want to include digits? (Y)es or (N)o: ").lower()[0] == 'y':
                digits = True
            if input("Do you want to include lower case letters? (Y)es or (N)o: ").lower()[0] == 'y':
                lower = True
            if input("Do you want to include upper case letters? (Y)es or (N)o: ").lower()[0] == 'y':
                upper = True
        except:
            print("Choose (Y)es or (N)o.")
            continue
        else:
            if symbols or digits or lower or upper:
                return symbols, digits, lower, upper
            else:
                print("At least one has to be selected.")
                continue

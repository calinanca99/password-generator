def get_pref():
    """
    Function to get preferences about characters included in the password.
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

    #return symbols, digits, lower, upper

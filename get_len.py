def get_len():
    """
    Function to get the length of the password.
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

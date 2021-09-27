from preferences import *

def generator():
    """
    Deals with the generation of the actual password.
    """
    import random

    length = set_length()

    symbols = "!@#$%^&*"
    digits = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOQPRSTUVWXYZ"

    char = ""
    pwd = ""

    includeSymbols, includeDigits, includeLower, includeUpper = set_preferences()

    if includeSymbols:
        char += symbols

    if includeDigits:
        char += digits

    if includeLower:
        char += lower_case

    if includeUpper:
        char += upper_case

    if not includeSymbols and not includeDigits and not includeLower and not includeUpper:
        print("The password is empty!")
        return

    for i in range(0, length):
        choice = random.randint(0, len(char)-1)
        pwd += char[choice]

    return pwd

#from get_pref import get_pref
from get_pref_v2 import get_pref

def pass_gen(length):
    """
    The actual password generator.
    """
    import random

    symbols = "!@#$%^&*"
    digits = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOQPRSTUVWXYZ"

    ###Some code to get preferences. For now assume all true

    char = ""
    pwd = ""

    includeSymbols, includeDigits, includeLower, includeUpper = get_pref()

    if includeSymbols:
        char += symbols

    if includeDigits:
        char += digits

    if includeLower:
        char += lower_case

    if includeUpper:
        char += upper_case

    if not includeSymbols and not includeDigits and not includeLower and not includeUpper: #Create some code to avoid this awkward situation
        print("The password is empty!")
        return

    for i in range(0, length):
        choice = random.randint(0, len(char)-1)
        pwd += char[choice]

    return pwd

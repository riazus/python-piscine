from sys import argv


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",    "B": "-... ",  "C": "-.-. ",  "D": "-.. ",   "E": ". ",
    "F": "..-. ",  "G": "--. ",   "H": ".... ",  "I": ".. ",    "J": ".--- ",
    "K": "-.- ",   "L": ".-.. ",  "M": "-- ",    "N": "-. ",    "O": "--- ",
    "P": ".--. ",  "Q": "--.- ",  "R": ".-. ",   "S": "... ",   "T": "- ",
    "U": "..- ",   "V": "...- ",  "W": ".-- ",   "X": "-..- ",  "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
}


def main():
    """
    Driver main function
    """
    if (len(argv) != 2):
        print("AssertionError: the arguments are bad")
        return

    capitalized = argv[1].upper()
    morse_parts = []

    for ch in capitalized:
        if not ch.isalnum() and not ch.isspace():
            print("AssertionError: the arguments are bad")
            return
        morse_parts.append(NESTED_MORSE.get(ch))

    print("".join(morse_parts))


if __name__ == "__main__":
    main()

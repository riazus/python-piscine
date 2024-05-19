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
    try:
        if (len(argv) != 2):
            raise AssertionError("The arguments are bad.")

        capitalized = argv[1].upper()
        morse_parts = []

        for ch in capitalized:
            if not ch.isalnum() and not ch.isspace():
                raise AssertionError("The arguments are bad.")
            morse_parts.append(NESTED_MORSE.get(ch))

        print("".join(morse_parts))
    except AssertionError as err:
        print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")


if __name__ == "__main__":
    main()

import sys as s


def main():
    """
    Driver main function
    """
    try:
        argc = len(s.argv)
        upper_letters = 0
        lower_letters = 0
        punctuation_marks = 0
        spaces = 0
        digits = 0

        if (argc > 2):
            raise AssertionError("More than one argument is provided.")

        text = ""
        if (argc == 1):
            text = input("What is the text to count?\n") + "\n"
        else:
            text = s.argv[1]

        i = 0
        while i < len(text):
            if text[i].isdigit():
                digits += 1
            elif text[i].isupper():
                upper_letters += 1
            elif text[i].islower():
                lower_letters += 1
            elif text[i].isspace():
                spaces += 1
            else:
                punctuation_marks += 1

            i += 1

        print(f"The text contains {i} characters:")
        print(f"{upper_letters} upper letters")
        print(f"{lower_letters} lower letters")
        print(f"{punctuation_marks} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as err:
        print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")


if __name__ == "__main__":
    main()

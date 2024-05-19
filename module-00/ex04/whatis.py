import sys as s

try:
    if (len(s.argv) != 2):
        raise AssertionError("More than one argument is provided.")
    elif (not s.argv[1].lstrip('-').isdigit()):
        raise AssertionError("Argument is not an integer.")

    text = 'I\'m Even.' if int(s.argv[1]) % 2 == 0 else 'I\'m Odd.'
    print(f"{text}")
except AssertionError as err:
    print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")

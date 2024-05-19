from sys import argv
from ft_filter import ft_filter


def main():
    try:

        argc = len(argv)
        if argc != 3 or argv[1].isalnum() or not argv[2].isdigit():
            raise AssertionError("The arguments are bad.")

        text = argv[1]
        num = int(argv[2])
        words = text.split()

        res = list(ft_filter(lambda x: len(x) > num, words))
        print(res)
    except AssertionError as err:
        print("\033[31m", AssertionError.__name__ + ":", err, "\033[0m")


if __name__ == "__main__":
    main()

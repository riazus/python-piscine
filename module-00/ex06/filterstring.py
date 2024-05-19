from sys import argv
from ft_filter import ft_filter


def main():
    argc = len(argv)
    if argc != 3 or argv[1].isalnum() or not argv[2].isdigit():
        print("AssertionError: the arguments are bad")
        return

    text = argv[1]
    num = int(argv[2])
    words = text.split()

    res = list(ft_filter(lambda x: len(x) > num, words))
    print(res)


if __name__ == "__main__":
    main()

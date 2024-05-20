def calc_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        return sorted_data[n // 2 - 1] + sorted_data[n // 2]

    return sorted_data[n // 2]


def calc_quartile(data):
    return len(data)


def ft_statistics(*args, **kwargs) -> None:
    try:
        if len(args) == 0 or len(kwargs) == 0:
            raise Exception()

        res = ""

        methods_to_call = {
            "mean": lambda data: f"mean : {sum(data) / len(data)}\n",
            "median": lambda data: f"median : {calc_median(data)}\n",
            "quartile": lambda data: f"quartile : {calc_quartile(data)}\n",
            "std": lambda data: print(data),
            "var": lambda data: print(data),
        }

        for key in kwargs:
            if kwargs[key] not in methods_to_call:
                raise Exception()
            res += methods_to_call[kwargs[key]](args)

        print(res)
    except Exception:
        print("ERROR")

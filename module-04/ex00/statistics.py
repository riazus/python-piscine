def calc_mean(data):
    """
    Calculates the mean of the provided data array.
    """
    return sum(data) / len(data)


def calc_median(data):
    """
    Calculates the median of the provided data array.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        return sorted_data[n // 2 - 1] + sorted_data[n // 2]

    return sorted_data[n // 2]


def calc_quartiles(data):
    """
    Calculates the first and third quartiles of a given list of numbers.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    q1 = n // 4
    q3 = q1 * 3

    return [float(sorted_data[q1]), float(sorted_data[q3])]


def calc_std(data):
    """Calculates the standard deviation of the provided data array."""
    mean = calc_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5


def calc_var(data):
    """Calculates the variance of the provided data array."""
    mean = calc_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args, **kwargs) -> None:
    """
    The function calculates the mean, median, quartile, standard deviation,
    and variance based on the provided positional arguments.
    """
    try:
        if len(args) == 0 or len(kwargs) == 0:
            raise Exception()

        res = []

        methods_to_call = {
            "mean": lambda data: f"mean : {calc_mean(data)}",
            "median": lambda data: f"median : {calc_median(data)}",
            "quartile": lambda data: f"quartile : {calc_quartiles(data)}",
            "std": lambda data: f"std : {calc_std(data)}",
            "var": lambda data: f"var : {calc_var(data)}",
        }

        for key in kwargs:
            if kwargs[key] not in methods_to_call:
                raise Exception()
            res.append(methods_to_call[kwargs[key]](args))

        for r in res:
            print(r)
    except Exception:
        print("ERROR")

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Function for calculataing BMI.
    Takes two arrays and makes following calculations:
    weight / height ** 2
    """
    if len(height) != len(weight):
        raise AssertionError("Args are invalid.")

    res = list()
    i = 0
    while i < len(height):
        validWeight = isinstance(weight[i], (int, float))
        validHeight = isinstance(height[i], (int, float))

        if not validWeight or not validHeight:
            raise AssertionError("Args are invalid.")
        res.append(weight[i] / (height[i] ** 2))
        i += 1

    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks each BMI for limitation.
    True if the value is above limit
    """
    res = list()

    for b in bmi:
        res.append(b > limit)

    return res

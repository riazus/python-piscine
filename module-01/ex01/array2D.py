import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array and returns a truncated
    version based on start and end indices.

    Parameters:
    family (list): 2D array (list of lists)
    start (int): Start index for slicing
    end (int): End index for slicing

    Returns:
    list: Truncated 2D array
    """
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")

        new_shape = np.array(family)[start:end]
        print(f"My new shape is : {new_shape.shape}")

        return new_shape.tolist()
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""

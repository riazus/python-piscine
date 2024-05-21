def square(x: int | float) -> int | float:
    """ Returns the square of the provided number. """
    return x ** 2


def pow(x: int | float) -> int | float:
    """ Returns the power of the provided number. """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that will call the provided function with the provided
    argument and return the result.
    """
    def inner():
        """Calls the provided function with the provided argument."""
        nonlocal x
        result = function(x)
        x = result
        return result
    return inner

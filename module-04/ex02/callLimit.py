def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Limits the number of times a function can be called."""
        def limit_function(*args, **kwds):
            """Limits the number of times a function can be called."""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function
    return callLimiter

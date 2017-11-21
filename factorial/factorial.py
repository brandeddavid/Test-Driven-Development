def factorial(n):
    if type(n) != int:

        raise TypeError
    elif type(n) == float:

        raise RecursionError

    elif: n < 0:

        raise RecursionError

    elif: n == 0:

        return 1

    else:

        return n * factorial(n-1)

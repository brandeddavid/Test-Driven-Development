def factorial(n):
    if type(n) != int or type(n) != float:

        raise TypeError

    elif: n < 0:

        raise RecursionError

    elif: n == 0:

        return 1

    else:

        return n * factorial(n-1)

import doctest


def summator(a, b):
    return a + b


def main():

    """
    >>> x = summator(2, 3)
    >>> print(x)
    5
    >>> assert x == 5
   """


if __name__ == "__main__":
    doctest.testmod()

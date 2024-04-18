
def divider(a, b):
    if a != 0 and b != 0:
        return a / b
    # else:
    #     print("Не хочу заниматься постыдным грехом")


def main(x):
    """
    >>> assert divider(10, 2) == 5
    >>> assert int(divider(10, 2)) == 5
    >>> assert divider(10, 2.4) == 4
    >>> assert divider(10, 2.4) == 4.166666666666667
    >>> assert divider(10.0, 5.0) == 2.0
    >>> assert divider(10, -2) == -5
    >>> assert = divider(-10, 2) == -5
    # >>> assert divider(int(input()), int(input())) == 10
    >>> assert divider(-10, -2) == 5
    >>> assert divider(2, 100) == 0.02
    >>> assert divider (2, 100) == int(0)
    >>> assert divider(10, 0) is None #плохой тест, лучше он просто упадёт чем будет получать на выходе Non Type
    >>> assert divider(0, 100) == None #плохой тест, лучше он просто упадёт чем будет получать на выходе Non Type


    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()


def sorter(st):
    lustrate = st.split(" ")

    if len(lustrate) < 3:
        return None

    dictate = {}

    for idx in range(1, len(lustrate)-1):
        f = " ".join((lustrate[idx - 1], lustrate[idx], lustrate[idx + 1]))
        if f not in dictate:
            dictate[f] = 1
        else:
            dictate[f] += 1

    sorted_triplets = sorted(dictate.items(), key=lambda item: item[1])

    return sorted_triplets[-1][0]


def main():
    """
    >>> assert sorter("abc bca abb bba bba bba bba abb abc cde abc bca abb") == "bba bba bba"
    >>> assert sorter("abc bca abb bba bba bba bba abc bca abb abb abc cde abc bca abb") == "abc bca abb"
    >>> assert sorter("abb cde abb") == "abb cde abb"
    >>> assert sorter("abc bca") == None

    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# задать вопрос, если сам не знаешь ответ который выдаст программа наперёд, какая лучшая практика? Cначала подаёшь
# значения, потом пишешь тест указав ответ?
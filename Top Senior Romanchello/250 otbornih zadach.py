#stepik user задачка 2.18
# x = input("Введите слово у которого хотите посчитать символы ")
# y = input("Введите символ который хотите посчитать ")
#
#
# print(x.count(y))

""""""


# def counter(st, ch):
#     if not isinstance(st, str) or not (ch, str):
#         return None
#
#     c = 0
#     for char in st.lower():
#         if char == ch:
#             c += 1
#
#     return c
#
#
# def main():
#     """
#     >>> assert counter("Ереван", "е") == 2
#     >>> assert counter("Ереван", "Е") == 2 #должен падать
#     >>> assert counter("Erevan", "e") == 2
#     >>> assert counter("Erevan", "E") == 2 #должен падать
#     >>> assert not ("Erevan", "E") == 1
#     >>> assert not ("Erevan", "е") == 2 #"е" русская
#
#     """

# Следующая задачка 2.6

#
# def reversiruem(slovo):
#     if not isinstance(slovo, str):
#         return None
#
#     x = slovo[::-1]
#     return x
#
#
# def main():
#     """
#     >>> assert reversiruem("Erevan") == 'naverE'
#     >>> assert reversiruem("Ереван") == 'наверЕ'
#     >>> assert reversiruem("Ереван") == 'Ереван'
#     >>> assert reversiruem("ЕреваН") == 'наверЕ'
#     >>> assert reversiruem("7654") == '4567'
#     >>> assert reversiruem("7654") == '1'
#     >>> assert reversiruem("a") == 'a'
#     >>> assert reversiruem("-12345") == '54321-'
#     """

# Следующая задачка 2.7


# def ubirator(st):
#     if not isinstance(st, str):
#         return None
#
#     ls = []
#     c = 0
#     x = int(len(st) / 2)
#     if len(st) < 5:
#         return ""
#     elif len(st) % 2 == 0:
#         a = st.replace(st[x], "")
#         nibba = a.replace(a[x-1], "")
#     else:
#         nibba = st.replace(st[x], "")
#
#     return nibba[1:-1]
#
#
# def main():
#     """
#     >>> assert ubirator('12345') == '24'
#     >>> assert ubirator('12345678910111213') == '23456781011121'
#     >>> assert ubirator('abcde') == 'bd'
#     >>> assert ubirator('12') == ""
#     >>> assert ubirator('abcd') == ""
#     >>> assert ubirator('123456') == '25'
#
#     """

#задачка 2.24

# def floatcounter(st, sym):
#     z = list(st)
#     z.reverse()
#     c = 0
#     for i in z:
#         if i == sym:
#             c += 1
#         elif i == '.':
#             break
#
#     return c
#
# def main():
#     """
#     >>> assert floatcounter('678.9876543', '7') == 1
#
#     """

if __name__ == "__main__":
    import doctest

    doctest.testmod()

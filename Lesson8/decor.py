from datetime import datetime


def my_first_decorator(func):

    def wrapper(*args, **kwargs):
        # тут мы что-то делаем дополнительное, и такое, что подойдет для любой функции
        print(func.__name__)
        print(args)
        print(kwargs)
        # тут мы возвращаем исходную функцию (с аргументами)
        return func(*args, **kwargs)
    
    return wrapper


def my_second_decorator(func):

    # тут мы по-другому сделаем - вызовем функцию внутри обертки
    def wrapper(*args, **kwargs):
        # считаем время работы функции (любой задекорированной функции)
        start_time = datetime.now().microsecond
        result = func(*args, **kwargs)
        stop_time = datetime.now().microsecond
        print("Функция {} отработала за {} микросекунд с результатом {}".format(func.__name__, stop_time-start_time, result))
        # тут мы возвращаем функцию "положи где взял", без аргументов, а можем и не возвращать
        return func

    return wrapper


if __name__ == "__main__":
    
  @my_first_decorator
    def summator(a, b):
        return a + b
    
    summator(2, 3)        

    @my_second_decorator
    def accumulator(num):
        acc = 0
        while num > 0:
            acc = acc + num
            num -= 1

        return acc

    accumulator(77777)

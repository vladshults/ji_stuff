

def next_cube(br=15):
    acc = 1
    # Бесконечный цикл
    while True:
        if acc > br:
            return
        yield acc ** 2
        acc += 1


if __name__ == "__main__":
    for num in next_cube(8):
        print(num)

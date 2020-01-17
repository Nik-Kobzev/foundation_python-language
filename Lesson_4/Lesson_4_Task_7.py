factorial = int(input('Введите число, от которого нужно взять факториал: '))


def generator(factorial):
    for el in range(1, factorial + 1):
        yield el


for el in generator(factorial):
    if el > 15:
        break
    print(el, end=" ")


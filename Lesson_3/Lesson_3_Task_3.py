def my_func(x, y, z):
    num = [x, y, z]
    num.sort()
    sum_num = num[2] + num[1]
    if sum_num % 1 == 0:
        sum_num = int(sum_num)
    return sum_num

print(f"Сумма наибольших двух аргументов: {my_func(float(input('Введете 1-е число: ')), float(input('Введете 2-е число: ')), float(input('Введете 3-е число: ')))}")


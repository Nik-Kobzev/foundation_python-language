# Перевое решение через *
def my_func_1(x, y):
    result = 1
    i = 1
    while i <= abs(y):
        result = result * x
        i += 1
    if y < 0:
        result = 1 / result
    return result


# Второе решение не используя *
def my_func_2(x, y):
    result = 0
    i = 1
    c = x
    while i <= abs(y)-1:
        j = 1
        result = 0
        while j <= x:
            result = result + c
            j += 1
        i += 1
        c = result
    if y < 0:
        result = 1 / result
    elif y == 0:
        result = 1
    return result

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое число степени: '))
print(f'значение числа в степени реализованное через оператор *: {my_func_1(x, y)}')
print(f'значение числа в степени реализованное не через оператор *: {my_func_2(x, y)}')

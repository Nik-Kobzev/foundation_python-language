def division(x, a):
    return x / a


while True:
    try:
        x = int(input('Введите числитель: '))
        a = int(input('Введите знаменатель: '))
        result = division(x, a)
        print(f'результат деления двух чисел равен {result}')
        break
    except ZeroDivisionError:
        print('Происходит деление на 0.\nВведите заново числа.\nПросьба в знаменателе указать число нераное 0')
    except ValueError:
        print('Было введено не число, просьба ввести числа заново')  # Пусть пользователь вводит заново два числа, чтобы не расслаблялся

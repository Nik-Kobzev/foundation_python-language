
sum_result = 0
ex = True
while ex:
    text = input('Введите чилс через пробел, в случаи окончания расчета введите Q: ')
    lst = text.split()
    for num_text in lst:
        if num_text != 'Q':
            sum_result = sum_result + int(num_text)
        else:
            ex = False
    print(f'Сумма чисел равна: {sum_result}')






proceeds = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержки: '))

if proceeds > costs:
    print('Фирма работает на прибыль')
    print(f'Рентабельность составила: {proceeds/costs}')
    count_fellow_worker = int(input('Введите кол-во сотрудников в фирме: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {(proceeds - costs) / count_fellow_worker}')
else:
    print('Фирма работает на убыток')

month = int(input('Введите месяц числом от 1 до 12: '))
# через list
month_list = ['Зиме', 'Зиме', 'Весне', 'Весне', 'Весне', 'Лету', 'Лету', 'Лету', 'Осени', 'Осени', 'Осени', 'Зиме']
print(f'Решение через list - данный месяц относится к {month_list[month-1]}')

# через dict
month_dict = {1: 'Зиме', 2: 'Зиме', 3: 'Весне', 4: 'Весне', 5: 'Весне', 6: 'Лету', 7: 'Лету', 8: 'Лету', 9: 'Осени', 10: 'Осени', 11: 'Осени', 12: 'Зиме'}
print(f'Решение через dict - данный месяц относится к {month_dict.get(month)}')
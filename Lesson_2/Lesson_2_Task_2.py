
count_element_list = int(input('Введите количество элементов в списке: '))
variable_list = []
i = 0

while i < count_element_list:
    variable_list.append(input(f'Введите {i + 1}й элемент листа: '))
    if 2 <= i + 1 <= count_element_list and (i + 1) % 2 == 0:
        a = variable_list[i-1]
        variable_list[i-1] = variable_list[i]
        variable_list[i] = a
    i += 1

print(variable_list)
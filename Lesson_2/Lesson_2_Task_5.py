
my_list = [7, 5, 3, 3, 2]

print(f'Набор натуральных чисел: {my_list}')

count_input = int(input('Сколько раз будете вводить рейтинг: '))

i = 1
while i <= count_input:
    element = int(input('Введите новый элемент рейтинга: '))
    for num, name in enumerate(my_list, start=0):
        if element > name:
            my_list.insert(num, element)
            break
        elif num == len(my_list) - 1:
            my_list.append(element)
            break
    print(f'Набор натуральных чисел с добавленным рейтингом {element}: {my_list}')
    i += 1


# my_list.insert(1, element)
# print(f'Набор натуральных чисел: {my_list}')
category_count = int(input('Сколько товаров вы хотите ввести: '))

i = 1
product_list = []
while i <= category_count:
    print(f'Введите параметры {i}го товара')
    product_name = input('    Введите название товара: ')
    product_price = float(input('    Введите стоимость товара: '))
    product_count = float(input('    Введите кол-во товара: '))
    product_count_measure = input('    Введите еденицу измереня: ')
    product_list.append((i, {'Название': product_name, 'Цена': product_price, 'количество': product_count, 'eд.': product_count_measure}))
    i += 1

print(product_list)
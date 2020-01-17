import itertools

# Первая часть
# с = 0
for el in itertools.count(start=0, step=1):
    # if с > 10:
    #     break
    print(el)
    # с += 1

# Вторая часть

my_list = [4, 'g', 6]

# с = 0
for el in itertools.cycle(my_list):
    # if с > 10:
    #     break
    print(el)
    # с += 1

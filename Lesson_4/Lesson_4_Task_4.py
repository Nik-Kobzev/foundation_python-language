a = [3, 6, 12, 4, 23, 6, 4]

b = [el for el in a if a.count(el) == 1]


print(b)
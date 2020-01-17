a = [4, 2, 3, 1, 5, 6, 1, 8]

b = [value for index, value in enumerate(a) if index > 0 and a[index-1] < value]

print(b)
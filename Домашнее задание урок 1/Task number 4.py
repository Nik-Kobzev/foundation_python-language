number_input = input('Введите целое число n: ')
i = 1
number_max = number_input[0]
 
while i < len(number_input):
    if number_max < number_input[i]:
        number_max = number_input[i]
    i += 1

print(f'Самая большая цифра в числе {number_max}')
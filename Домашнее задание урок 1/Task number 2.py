# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds_input = 3754 # int(input('Введите время в секундах: '))
hours = seconds_input//3600
minutes = (seconds_input // 60) % 60
seconds = seconds_input - hours*3600 - minutes*60
print(hours)
print(minutes)
print(3754%60)
print(seconds)
# if hours < 10:
#     hours = '0' + str(hours)
# if minutes < 10:
#     minutes = '0' + str(minutes)
# if seconds < 10:
#     seconds = '0' + str(seconds)

print(f'Результат перевода секунд в формат чч:мм:сс - {str(hours).rjust(2,"0")}:{str(minutes).rjust(2,"0")}:{str(seconds).rjust(2,"0")}')

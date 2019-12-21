#  Пользователь вводит время в секундах. Переведите время в часы,
#  минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds_input = int(input('Введите время в секундах: '))
day = seconds_input // 86400
hours = (seconds_input // 3600) % 24
minutes = (seconds_input // 60) % 60
seconds = seconds_input % 60

if day == 1:
    day_text = 'днь'
elif 1 < day < 5:
    day_text = 'дня'
else:
    day_text = 'дней'


print(f'Результат перевода секунд в формат чч:мм:сс     - {(seconds_input // 3600):02}:{minutes:02}:{seconds:02}')
print(f'Если нужно еще выводить и день то вот держите   - {day} {day_text}  {hours:02}:{minutes:02}:{seconds:02}')

distance_a = int(input('Введите растояние пробежки первого дня в км.: '))
target_b = int(input('Введите растояние, которое должен достичь спртсмен в км.: '))
result = distance_a
step = 0.1
day = 

while result < target_b:
    result = result + result * step
    day += 1

print(f'На {day}-й день спортсмен достиг результата — не менее {target_b} км.')
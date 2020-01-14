# name, surname, year of birth, city of residence, email, phone.
def info_client(name, surname, year_birth, city, email, phone):
    print(
        f'Иформация о пользователе. Имя: {name}. Фамилия: {surname}. Год рождения: {year_birth}. Город проживания: {city}. Email: {email}. Телефон: {phone}.')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year_birth = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

info_client(name=name, phone=phone, surname=surname, year_birth=year_birth, city=city, email=email)

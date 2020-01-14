def int_func(text):
    return text.title()

text = input('Введите текст: ')
text_itog = ''

for t in text.split():
    text_itog = int_func(t) + ' ' + text_itog

print(text_itog)


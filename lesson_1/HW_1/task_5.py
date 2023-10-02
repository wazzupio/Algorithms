"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

import string


letter_1 = input('Введите первую букву (англ.): ')
letter_2 = input('Введите вторую букву (англ.): ')

alp = string.ascii_lowercase
count_1 = 0
count_2 = 0

for i in alp:
    count_1 += 1
    if i == letter_1:
        break

for i in alp:
    count_2 += 1
    if i == letter_2:
        break

print(f'Буква {letter_1} находится на {count_1}-м месте в алфавите')
print(f'Буква {letter_2} находится на {count_2}-м месте в алфавите')

print(f'Количество букв между буквами {letter_1} и {letter_2} = {abs(count_1 - count_2) - 1}')

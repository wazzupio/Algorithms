"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

import string

alp = string.ascii_lowercase
num = int(input('Введите номер буквы: '))
count = 0

for i in alp:
    count += 1
    if count == num:
        print(f'Буква в алфавите под номером {num} - {i}')
    if num > len(alp) or num <= 0:
        print(f'Недопустимое значение')
        break

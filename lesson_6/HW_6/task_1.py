"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для
одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в
комментариях версию Python и разрядность вашей ОС
"""

"""
В качестве примера для просчета возьмем 9ое задание из 3го урока.
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import random

M = 8
N = 4

my_list = [[0] * M for i in range(N)]
min_el_col = [] * M
els_col = []
size_els_cols = 40 + 8 * len(els_col)  # Присваиваем переменной размер пустого списка в байтах
print(f'Изначалный размер динамичной переменной переменной "els_col": {size_els_cols} байт')

for i in range(N):
    for j in range(M):
        my_list[i][j] = int(random() * 100)

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print('%3d' % my_list[i][j], end='')
    print()

for i in range(M):
    for j in range(N):
        els_col.append(my_list[j][i])
    min_el_col.append(min(els_col))
    els_col.clear()

print(f'Список минимальных элементов в колонках: {min_el_col}')
print(f'Максимальный элемент среди минимальных: {max(min_el_col)}')

size_els_cols += 24 * N
print(f'Размер динамичной переменной "els_col" в состоянии заполненного списка: {size_els_cols} байт')

size_els_cols = 40 + 8 * len(els_col)  # Переприсваиваем значение переменной, т.к. в цикле очистили список
print(f'Конечный размер динамичной переменной "els_col": {size_els_cols} байт')

size_M = 24  # Выделено памяти для переменной M
size_N = 24  # Выделено памяти для переменной N
size_my_list = ((24 * M) * N) + (40 + 8 * M)  # Выделено памяти для переменной my_list
size_min_el_col = (24 * M) + (40 + 8 * M)  # Выделено памяти для переменной min_el_col
total = sum([size_M, size_N, size_my_list, size_min_el_col])

print(f'Было выделено памяти под переменные: {total} байт')

# Вариант решения с использованием zip

M = 8
N = 4

my_list = [[0]*M for i in range(N)]
min_el_col = [] * M

for i in range(N):
    for j in range(M):
        my_list[i][j] = int(random() * 100)

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print('%3d' % my_list[i][j], end='')
    print()

print('*' * 30)
a = list(zip(*my_list))
print(a)
print('*' * 30)

for i in range(len(a)):
    for j in range(len(a[i])):
        print('%3d' % a[i][j], end='')
    print()

print('*' * 30)

min_els = []

for i in a:
    min_els.append(min(i))

print(f'Список минимальных элементов в колонках: {min_els}')
print(f'Максимальный элемент среди минимальных: {max(min_els)}')


size_M = 24  # Выделено памяти для переменной M
size_N = 24  # Выделено памяти для переменной N
size_my_list = ((24 * M) * N) + (40 + 8 * M)  # Выделено памяти для переменной my_list
size_min_el_col = (24 * M) + (40 + 8 * M)  # Выделено памяти для переменной min_el_col
size_a = (40 + 8 * M) + (24 + 8 * N) + ((24 * N) * M)
size_min_els = (40 + 8 * M) + (24 * M)

total = sum([size_M, size_N, size_my_list, size_min_el_col, size_a, size_min_els])

print(f'Было выделено памяти под переменные: {total} байт')

"""Python 3.9, разрядность - x64"""

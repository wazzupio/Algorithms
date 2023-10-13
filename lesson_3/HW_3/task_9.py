"""
9. . Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


from random import random, randint

# M = 8
# N = 4
#
# my_list = [[0]*M for i in range(N)]
# min_el_col = [] * M
#
# for i in range(N):
#     for j in range(M):
#         my_list[i][j] = int(random() * 100)
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print('%3d' % my_list[i][j], end='')
#     print()
#
# for i in range(M):
#     els_col = []
#     for j in range(N):
#         els_col.append(my_list[j][i])
#     min_el_col.append(min(els_col))
#
# print(f'Список минимальных элементов в колонках: {min_el_col}')
# print(f'Максимальный элемент среди минимальных: {max(min_el_col)}')


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

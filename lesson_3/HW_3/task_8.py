"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
ячейку строки. В конце следует вывести полученную матрицу.
"""

M = 5
N = 4

my_list = [[0]*M for i in range(N)]

for i in range(N):
    for j in range(M):
        my_list[i][j] = int(input(f"Введите {j + 1}-е число для {i + 1}-й строки: "))
        if j == M - 2:
            my_list[i][j + 1] = sum(my_list[i])
            break

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print('%5d' % my_list[i][j], end='')
    print()

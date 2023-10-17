"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
"""

from random import randint

count_nums = 10
my_list = [randint(1, 100) for i in range(count_nums)]

print(my_list)

max_el = max(my_list)
min_el = min(my_list)
my_list[my_list.index(max(my_list))] = min_el
my_list[my_list.index(min(my_list))] = max_el

print(my_list)

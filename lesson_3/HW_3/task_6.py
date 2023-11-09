"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не
включать.
"""

from random import randint

count_nums = 10
my_list = list(set(randint(1, 100) for i in range(count_nums)))

print(my_list)

min_el_idx = my_list.index(min(my_list))
max_el_idx = my_list.index(max(my_list))

if max_el_idx < min_el_idx:
    min_el_idx = my_list.index(max(my_list)) + 1
    max_el_idx = my_list.index(min(my_list))
elif max_el_idx > min_el_idx:
    min_el_idx = my_list.index(min(my_list)) + 1
    max_el_idx = my_list.index(max(my_list))

print(f"Сумма равна: {sum(my_list[min_el_idx:max_el_idx])}")

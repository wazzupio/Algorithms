"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

count_nums = 10
my_list = [randint(1, 100) for i in range(count_nums)]

print(my_list)

for i in range(1, 3):
    min_el_idx = my_list.index(min(my_list))
    del_min_el = my_list.pop(min_el_idx)
    print(f"Минимальный элемент {i} = {del_min_el}")

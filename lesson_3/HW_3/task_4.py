"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

count_nums = 15
my_list = [randint(1, 10) for i in range(count_nums)]
count_list = []

print(my_list)

for i in my_list:
    count_list.append(my_list.count(i))

print(f'Число которе встречается чаще всего в массиве: {my_list[count_list.index(max(count_list))]}')
print(f'Кол-во раз: {count_list[count_list.index(max(count_list))]}')

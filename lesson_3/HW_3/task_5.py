"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
позицию (индекс) в массиве.
"""

from random import randint

count_nums = 10
my_list = [randint(-10, -1) for i in range(count_nums)]

print(f"Список: {my_list}")
print(f"Максимальный отрицательный элемент: {min(my_list)}")
print(f"Позиция (индекс): {my_list.index(min(my_list))}")

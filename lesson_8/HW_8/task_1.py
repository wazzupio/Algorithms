"""
1. Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""

from itertools import combinations
from pprint import pprint
import hashlib

unique_els_with_hash = {}  # Словарь в которы будем добавлять уникальные подстроки и их хэши
my_string = 'hello '


def count_unique_substrings(string):
    """
    Функция для подсчета количества уникальных подстрок
    :param string:
    :return int:
    """
    count_substring = 0  # Кол-во уникальных подстрок
    for i in range(1, len(string)):
        """В каждом цикле создаем итератор со всеми возможными комбинациями элементов длинной i"""
        com = combinations(string, i)  # combinations('ABCD', 2) --> AB AC AD BC BD CD
        if i == len(string):
            break
        for el in com:
            """
            Проходимся по эл-там итератора, преобразуем эл-т в строку, получаем хэш эл-та,
            пропускаем эл-ты с пробелами, если такие есть и если такого эл-та нет в хэш-таблице
            добавляем в таблицу
            """
            el_str = ''.join(el)
            el_hash = hashlib.md5(el_str.encode('utf-8'))
            if ' ' in el:
                continue
            elif unique_els_with_hash.get(el_str):
                continue
            else:
                unique_els_with_hash[el_str] = el_hash
                count_substring += 1
    return count_substring


print(f'Кол-во различных подстрок в строке "{my_string}" = {count_unique_substrings(my_string)}')
pprint(unique_els_with_hash)

"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

# def els(count):  # Решенице через цикл
#     res = 1
#     my_sum = 1
#     while count != 1:
#         count -= 1
#         res = res / -2
#         my_sum += res
#     return my_sum
#
#
# print(els(4))


def rec(cnt, res=1.0):  # Решенице через рекурсию
    base = 1
    if cnt == base:
        return 1
    elif cnt > base:
        res = res / -2
        return res + rec(cnt - 1, res)


n = int(input('Введите число n: '))

print(f'Сумма n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 равна: {rec(n)}')

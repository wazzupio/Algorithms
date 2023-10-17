"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
- Без использования Решета Эратосфена
- Использовать алгоритм решето Эратосфена
"""
from timeit import timeit

n = int(input("Введите число: "))


# - Без использования Решета Эратосфена
def no_erat(num):
    simple_nums_list = []

    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            simple_nums_list.append(i)
    return simple_nums_list


print(f'Результат функции no_erat: {no_erat(n)}')


# - Использовать алгоритм решето Эратосфена
def erat(num):
    lst = [i for i in range(num + 1)]
    lst[1] = 0
    simple_nums = []

    i = 2
    while i <= num:
        if lst[i] != 0:
            simple_nums.append(lst[i])
            for j in range(i, num + 1, i):
                lst[j] = 0
        i += 1
    return simple_nums


print(f'Результат функции erat: {erat(n)}')

print(f'Скорость выполнения программы без Решета Эратосфена: {timeit("no_erat(n)", globals=globals())}')
print(f'Скорость выполнения программы Решета Эратосфена: {timeit("erat(n)", globals=globals())}')
print('Сложность алгоритма через цикл: O(n^2)')
print('Сложность алгоритма Решета Эратосфена: O(n*log(log*n))')

"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""

num = 5
form = int(num * (num + 1) / 2)


def rec(n):
    if n == 1:
        return n
    return n + rec(n - 1)


print(rec(num))
print(form)
print(rec(num) == form)

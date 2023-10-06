"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

num = input('Введите трехзначное число: ')
sum_num = 0
sum_prod = 1

while len(num) != 3:
    num = input('Введите трехзначное число: ')

for i in num:
    sum_num += int(i)
    sum_prod *= int(i)

print(sum_num, sum_prod)

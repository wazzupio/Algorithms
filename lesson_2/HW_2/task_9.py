"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

nums = ['23535', '213', '76']
sum_nums = []

for i in nums:
    sum_nums.append(sum(list(map(int, ''.join(i)))))

print(max(sum_nums))

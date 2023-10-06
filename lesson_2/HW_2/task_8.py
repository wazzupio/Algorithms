"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

count = int(input('Введите кол-во вводимых чисел: '))
nums = ''
nums_list = []

while count != 0:
    count -= 1
    inp = input('Введите число: ')
    nums += inp
    nums_list.append(inp)

search_num = input('Введите цифру: ')
count_num = 0

for i in nums:
    if i == search_num:
        count_num += 1

print(f'В числах: {", ".join([el for el in nums_list])} цифра {search_num} встречается {count_num} раз(а)')

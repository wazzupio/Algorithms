"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def get_right_list():
    """Функция которая запрашивает у пользователя шестнадцатеричное число, проверяет на правильность ввода значений,
    и возвращает список."""
    flag = True
    while flag:
        inp = input(f"Введите шестнадцатеричное число: ")
        for i in inp:
            if i.isdigit():
                if int(i) > 10 or int(i) <= 0:
                    print('Вы ввели неправильное значение')
                    break

            elif not i.isdigit() and i not in letters.keys():
                print('Вы ввели неправильное значение')
                break

            if inp.index(i) == len(inp) - 1:
                right_list = [el for el in inp]
                return right_list


def in_16_out_10(lst):
    """Функция которая принимает список шестнадцатеричных чисел, а возвращает список десятеричных"""
    for idx in range(len(lst)):  # В списке меняем буквенные значения на числа
        if not lst[idx].isdigit():
            lst[idx] = letters[lst[idx]]
        else:
            lst[idx] = int(lst[idx])

    def get_num_10(updated_lst):
        """Доп функция которая принимает обновленный список 16-ричных чисел, а возвращает 10-ричное число"""
        degree = len(updated_lst) - 1
        num = 0
        for el in updated_lst:
            num += el * 16 ** degree
            degree -= 1

        return num
    return get_num_10(lst)


def in_10_out_16(num):
    """Функция которая принимает 10-ричное число, а возвращает список 16-ричных чисел"""
    lst_16 = deque()
    while num != 0:
        rem_of_div = num % 16
        num = num // 16
        if rem_of_div < 10:
            lst_16.appendleft(str(rem_of_div))
        else:
            for k, v in letters.items():
                if rem_of_div == v:
                    lst_16.appendleft(str(k))

    return list(lst_16)


letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

list_1 = get_right_list()
list_2 = get_right_list()

print('-' * 50)
print(f"Первое 10-ричное число: {list_1}")
print(f"Второе 10-ричное число: {list_2}")
print('-' * 50)

num_1_in_10 = in_16_out_10(list_1)
num_2_in_10 = in_16_out_10(list_2)
sum_num_in_10 = num_1_in_10 + num_2_in_10
prod_num_in_10 = num_1_in_10 * num_2_in_10

print(f"Первое 16-ричное число: {num_1_in_10}")
print(f"Второе 16-ричное число: {num_2_in_10}")
print(f"Сумма 10-чных чисел: {sum_num_in_10}")
print(f"Произведение 10-чных чисел: {prod_num_in_10}")
print('-' * 50)
print(f"Сумма 16-чных чисел: {in_10_out_16(sum_num_in_10)}")
print(f"Произведение 16-чных чисел: {in_10_out_16(prod_num_in_10)}")
print('-' * 50)

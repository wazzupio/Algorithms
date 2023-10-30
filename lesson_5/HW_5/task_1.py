"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

count_companies = int(input("Введите кол-во компаний: "))
profit_all_companies = 0
companies = dict()
companies_higher_profits = dict()
companies_lower_profits = dict()

for i in range(count_companies):
    companies[f'{input(f"Введите название {i + 1}-й компании: ")}'] = list()

for i in companies:
    for j in range(4):
        companies[i].append(int(input(f"Введите прибыль {i} компании за {j + 1}-й квартал-: ")))

print(f"Компании, прибыль за кварталы: {companies}")

for k, v in companies.items():
    profit_company = sum(v)
    profit_all_companies += profit_company
    companies[k] = profit_company

print(f"Компании, прибыль общая: {companies}")

average_profit = profit_all_companies / count_companies

print(f"Средняя прибыль: {average_profit}")

for key, value in companies.items():
    if value > average_profit:
        companies_higher_profits[key] = value
    elif value < average_profit:
        companies_lower_profits[key] = value

print(f"Компании чья прибыль выше среднего: {companies_higher_profits}")
print(f"Компании чья прибыль ниже среднего: {companies_lower_profits}")

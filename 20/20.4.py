'''Работа за преподавателем'''
# Task 1

# scores_dict = {
#     'Ваня': 33,
#     'Петя': 60,
#     'Лена': 45
# }
#
# for i_name in scores_dict:
#     print(i_name, scores_dict[i_name])

# Task 2

# scores_dict = {
#     'Ваня': 33,
#     'Петя': 60,
#     'Лена': 45
# }
#
# for i_name, i_score in enumerate(scores_dict):
#     print(i_name, i_score)
#
# for i_name in enumerate(scores_dict):
#     print(i_name)

# Task 3

# scores_dict = {
#     'Ваня': 33,
#     'Петя': 60,
#     'Лена': 45
# }
#
# for i_name, i_score in scores_dict.items():
#     print(i_name, i_score)

# Task 4

# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678'
# }
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520}
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150}
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97}
#     ]
# }
#
# for i_title, i_code in goods.items():   # title - название
#     total_quantity = 0
#     total_cost = 0
#     for j_good in store[i_code]:
#         total_quantity += j_good['quantity']
#         total_cost += j_good['price'] * j_good['quantity']
#     print('{title} - {quantity} шт., стоимость {cost} руб.'.format(
#         title=i_title,
#         quantity=total_quantity,
#         cost=total_cost
#     ))

# Home Work
# 1 ==========================================================================
'''
Внезапно вы обнаружили, что старый скрипт, который выводит
данные о фруктах, куда-то потерялся. Необходимо его восстановить.
Дан словарь incomes с парами «название фрукта — цена»:
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
Вывести на экран словарь в следующем виде:
apple -- 5600.2
orange -- 3500.45
banana -- 5000.0
bergamot -- 3700.56
durian -- 5987.23
peach -- 10000.5
pear -- 1020.0
persimmon -- 310.0
Не используйте обращение по ключу словаря.
'''
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00
# }
#
# for i_title, i_price in incomes.items():
#     print(i_title, '--', i_price)
# 2 ==========================================================================
'''Задача 2. Сервер
У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно, 
как они представлены в словаре.
Результат работы программы:
server:
    host: 127.0.0.1
    port: 10
configuration:
    access: true
    login: Ivan
    password: qwerty
'''
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
# for i_key, i_value in server_data.items():
#     print(f'{i_key}:')
#     for j_key, j_value in i_value.items():
#         print(f'\t{j_key}: {j_value}')
# 3 ==========================================================================
'''
Задача 3. В одну строчку
Нашему другу дали задачу: «Есть словарь, в котором ключи - это числа от 0 до 4, а значения
ключей — числа 0, 100, 144 и 19 соответственно.
Нужно написать программу, которая выводит список
тех значений, у которых ключ делится на 2. Причём программа должна быть в одну строчку.» 
Программа у друга работает, но её не приняли, так как в ней не используется правило 
«не повторяйся» — это когда части кода не повторяются. Помогите другу исправить решение 
задачи так, чтобы код в строчке не повторялся.
Решение друга:
print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] % 2 == 0])

'''
print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])

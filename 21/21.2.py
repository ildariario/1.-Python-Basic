'''Работа за преподавателем'''
# Task 1

# def factorial(num):
#     fact_n_minus_1 = factorial(num - 1)
#     return num * fact_n_minus_1
#
#
# num_fact = factorial(5)
# print(num_fact)

# Task 2

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)
#
#
# num_fact = factorial(5)
# print(num_fact)

# Task 3
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# user_key = input('Какой ключ ищем? ')
# value = find_key(site, user_key)
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре сайта нет!')

# Home Work
# 1 ==========================================================================
'''Задача 1. Challenge
Обычно программисты любят, когда всё просто и понятно. Но Антон не из таких. Он любит 
устраивать себе челлендж, развиваться и сразу применять на практике то, что только что 
узнал. И в этот раз он подумал реализовать подсчёт факториала без использования циклов.
Напишите функцию, которая считает факториал числа с помощью рекурсии.
Кстати, в Python есть ограничение на количество рекурсивных вызовов. Попробуйте передать 
своей функции, например, число 1000 и посмотрите, что будет.
'''
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# num = int(input('Введите число факториал которого хотите посчитать: '))
# print(f'{num}! =', factorial(num))
# 2 ==========================================================================
''''''
# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))
# 3 ==========================================================================
'''Задача 2. Степень числа
На одном из форумов, посвящённых программированию, пользователь выложил такой код для 
расчёта степени числа без использования циклов, ** и функции math.pow():
def power(a, n):
    return a * power(a, n)

float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))
Другие пользователи отметили, что это решение нерабочее и в нём есть ошибки. Исправьте 
это решение, не используя циклы, возведение в степень через ** и функцию math.pow()

Правильный результат:
Введите вещественное число: 1.5
Введите степень числа: 5
1.5 ** 5 = 7.59375
'''
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search_of_key(struct, key):
    if key in struct:
        return struct[key]
    for i_struct in struct.values():
        if isinstance(i_struct, dict):
            result = search_of_key(i_struct, key)
            if result:
                break
    else:
        result = None
    return result


usr_key = input('Искомый ключ: ')
value = search_of_key(site, usr_key)
if value:
    print('Значение: ', value)
else:
    print('Такого ключа в структуре сайта нет.')

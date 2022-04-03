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
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# num = int(input('Введите число факториал которого хотите посчитать: '))
# print(f'{num}! =', factorial(num))
# 2 ==========================================================================
# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))
# 3 ==========================================================================
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
# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================

# 7 ==========================================================================

# 8 ==========================================================================

# 9 ==========================================================================

# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================
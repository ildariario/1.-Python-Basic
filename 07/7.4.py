# Home Work
# 1 ==========================================================================
'''Задача 1. Квадраты превратились в кубы
Напишите программу, которая выводит кубы чисел (число в третьей степени), лежащих в диапазоне от 1 до 10.
Результат:
1
8
27
64
125
216
343
512
729
1000
'''
# for num in range(1, 11):
#     print(num**3)
# 2 ==========================================================================
'''Задача 2. Сумма чисел
Напишите программу, где пользователь вводит любые два целых положительных числа. А программа суммирует 
все числа в диапазоне от первого до второго. Гарантируется, что первое введённое число всегда меньше второго.
Пример:
Введите первое число: 5
Введите второе число: 10
Сумма чисел от 5 до 10 равна 45
'''
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# sum = 0
# if num_1 > num_2:
#     print('Первое число д/б меньше второго!')
# else:
#     for number in range(num_1, num_2 + 1):
#         sum += number
# print('Сумма чисел от', num_1, 'до', num_2, 'равна', sum)
# 3 ==========================================================================
'''Задача 3. Сумма нечётных чисел
Напишите программу, похожую на разобранный предыдущий пример с суммой чисел, но только теперь нужно вычислить сумму всех нечётных чисел, лежащих в диапазоне, который укажет пользователь.
'''
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# sum = 0
# if num_1 > num_2:
#     print('Первое число д/б меньше второго!')
# else:
#     for number in range(num_1, num_2 + 1):
#         if number % 2 ==0:
#             sum += number
#     print('Сумма всех четных чисел в интервале\nот', num_1, 'до', num_2, 'равна', sum)
# 4 ==========================================================================
'''Задача 4. Поел - можно и поспать, поспал - можно и поесть
Напишите программу, разобранную в уроке.
У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью, но засыпает всегда до того, 
как наступит полночь, обычно в 23 часа. А ещё он очень любит поесть. Он ест каждый час и если съедает 
больше 2000 калорий, то он просто падает спать. Напишите программу, которая поможет Саше понять, всё ли 
с ним хорошо. Для этого нужно посчитать, сколько он всего съест калорий и сколько часов будет бодрым.
'''
# wake_up = int(input('Во сколько проснулся Саша? '))
# awake = 0   # awake - бодровствовать
# calories = 0
# for hour in range(wake_up, 23):
#     cal = int(input(f'Сколько калорий Саша съел в {hour} часов? '))
#     calories += cal
#     if calories > 2000:
#         print('Превышено 2000 калорий! Саша заснул ..Z..z..z..')
#         break
#     awake += 1
# print('За день Саша съел', calories, 'каллорий.')
# print('Саша находился бодрым', awake, 'ч.')
# 5 ==========================================================================
'''Задача 5. Простые числа (*необязательная)
С клавиатуры вводится чисто N. Напишите программу, проверяющую, простое ли это число.
Эту задачу мы подробно разберем в следующем уроке. Однако будет очень полезно, если вы перед этим 
попробуете решить ее самостоятельно. Не ищите решения в сети: все равно оно будет в следующем уроке.
'''

# Вар 1
# N = int(input('Введите число: '))
# count = 0
# for dev in range(1, N + 1):     # devider - делитель
#     if (N % dev) == 0:
#         count += 1
#     # print(f'Число {N}/{dev}={N/dev}')
# if count == 2:
#     print(f'                         Число {N} - простое!')
# else:
#     print(f'Число {N} - составное.')

# Вар 2
# total = 0
# for N in range(1000,10001):
#     count = 0
#     for dev in range(1, N+1):       # devider - делитель
#         if (N % dev) == 0:          # как только N разделется на dev без остатка 2 раза, то count станет = 2. Время расходуется
#             count += 1              # на деление на каждое число из диапазона от 1 до N+1.
#     if count == 2:
#         total += 1
#         print(f'                         Число {N} - простое!')
#     else:
#         print(f'Число {N} - составное.')
# print(f'-----------------------------------------------')
# print(f'В рассмотренном диапазоне {total} простых чисел.')
# print(f'-----------------------------------------------')
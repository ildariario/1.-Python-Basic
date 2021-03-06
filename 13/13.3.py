'''Работа за преподавателем'''
# Task 1

# x = 1
# for i in range(10000):
#     x /= 2
# print(x)

# x = 1
# for i in range(1, 1075+1):
#     x /= 2
#     print(f'{i}-я итерация: 2^-{i} = {x}')

# x = 1
# count = 0
# while x != 0:
#     x /= 2
#     count += 1
#     print('x =', x)
# print('Итераций:', count)

# x = 1
# count_1 = 0
# count_2 = 0
# while x != 0:
#     x /= 2
#     if x != 0:
#         last_non_zero_value = x
#         count_1 += 1
#     count_2 += 1
#     print(x)
# print(f'Последнее не нулевое значение {last_non_zero_value} достигнуто на {count_1}-ой итерации.')
# print(f'Значение машинного нуля достигнуто на {count_2}-ой итерации.')

# Task 2

# vFirstPlanet = 1.41228e15    # км^3
# vSecondPlanet = 6.254e13    # км^3
# pEarth = 5.5153e12     # кг/км^3

# mFirstPlanet = float(input('Масса первой планеты: '))
# mSecondPlanet = float(input('Масса второй планеты: '))

# pFirstPlanet = mFirstPlanet / vFirstPlanet
# pSecondPlanet = mSecondPlanet / vSecondPlanet
# print('Плотность первой планеты: ', pFirstPlanet)
# print('Плотность второй планеты: ', pSecondPlanet)

# if abs(pEarth - pFirstPlanet) < abs(pEarth - pSecondPlanet):
#     print('Плотность первой планеты ближе к плотности Земли')
# else:
#     print('Плотность второй планеты ближе к плотности Земли')
# Home Work
# 1 ==========================================================================
'''Задача 1. Возможности компьютера
В одной IT-компании тестируют возможности различных языков программирования, компиляторов 
и, конечно же, компьютеров. Компания дала вам задачу понять, какое самое маленькое 
возможное число можно получить путём постоянного деления числа на 2. Изначально число 
равно единице. Также, помимо самого числа, компания просит вывести количество делений. 
Реализуйте такую программу.
'''
# count = 0
# num = 1
# while True:
#     num /= 2
#     if num != 0:
#         count += 1
#         min_num = num
#     else:
#         print('Самое маленькое число: ', min_num,'\nКол-во делений: ', count)
#         break
# 2 ==========================================================================
'''Задача 2. Тестирование
Команде программистов отдали на тестирование новую модель суперкомпьютера. Для начала 
программисты решили проверить, как у компьютера обстоят дела с вычислениями вещественных 
чисел. Разработчики компьютера предупредили, что на входе он работает только с 
экспоненциальной формой числа.
Пользователь вводит число N в экспоненциальной форме, где мантисса всегда равна числу 
от 1 до 9, а порядок меньше нуля. Также есть переменная Х, которая изначально равна единице. 
Посчитайте, сколько раз нужно прибавить N к Х, чтобы оно перевалило за двойку.
Дополнительно: обеспечьте контроль ввода.
 
Пример 1:
Введите число в эксп. форме: 1e-3
Кол-во прибавлений: 1001
 
Пример 2:
Введите число в эксп. форме: 5.02e-1
Кол-во прибавлений: 2
'''
# count = 0
# x = 1
# n = float(input('Введите число в экспоненциальной форме: '))
# while x <= 2:
#     x += n
#     count += 1
# print('Кол-во прибавлений: ', count)
# 3 ==========================================================================
'''Задача 3. Урок информатики
На одном из уроков информатики учитель объяснял тему «Числа с плавающей точкой», но 
несколько учеников никак не могли понять, почему эта точка «плавает» и как вообще 
выглядят числа в такой форме. Для наглядности учитель написал программу, которая берёт 
число больше десяти и выводит его в формате плавающей точки.
Пользователь вводит положительное число x (x > 10). Напишите функцию, которая выводит 
его в формате плавающей точки, то есть x = a * 10 ** b, где 1 ≤ a < 10.
 
Пример 1:
Введите число: 16
Формат плавающей точки: x = 1.6 * 10 ** 1
 
Пример 2:
Введите число: 92345
Формат плавающей точки: x = 9.2345 * 10 ** 4
'''
def floating_point_format(num):
    a = num
    b = 0
    while num > 10:
        num /= 10
        b += 1
    print('Формат плавающей точки: ', a * 10 ** -b, '* 10 **', b)


x = float(input('Введите число положительное число > 0: '))
floating_point_format(x)

# Task 1



# Task 2



# Task 3



# Home Work
# 1 ==========================================================================
# def summa_n(N):
#     summ = 0
#     for num in range(1, N+1):
#         summ += num
#     print('Я знаю, что сумма чисел от 1 до', N, 'равна', summ)

# N = int(input('Введите число: '))
# summa_n(N)
# 2 ==========================================================================
# def test():
#     n = int(input('Введите целое число: '))
#     if n > 0:
#         positive()
#     elif n < 0:
#         negative()
    
# def positive():
#     print('Положительное.')

# def negative():
#     print('Отрицательное')

# test()
# 3 ==========================================================================
# print('=' * 50)
# import math

# def circle(R):
#     S = math.pi * R ** 2
#     print('Площадь круга равна: ', S)

# def rectangle(a, b):
#     S = a * b
#     print('Площадь прямоугольника равна: ', S)

# def triangle(a, b, alpha):
#     S = (1 / 2) * a * b * math.sin(math.radians(alpha))
#     print('Площадь треугольника равна: ', S)
    
# print('Полщать какой фигуры будем вычислять?')
# choice = int(input('1 - круга; 2 - прямоугольника; 3 - треугольника: '))
# if choice == 1:
#     R = float(input('Введите радиус круга: '))
#     circle(R)
# elif choice == 2:
#     a = float(input('Введите длину прямоугольника: '))
#     b = float(input('Введите ширину прямоугольника: '))
#     rectangle(a, b)
# elif choice == 3:
#     a = float(input('Введите длину боковой стороны треугольника: '))
#     b = float(input('Введите длину основания треугольника: '))
#     alpha = float(input('Введите угол между основанием и боковой стороной (в градусах): '))
#     triangle(a, b, alpha)
# else:
#     print('Ошибка ввода! Введите 1, 2 или 3.')
# print('=' * 50)
# 4 ==========================================================================
# print('=' * 50)
# def sumNum(number):
#     # summ = 0
#     # while True:
#     #     sym = number % 10
#     #     summ += sym
#     #     if sym == 0:
#     #         break
#     #     number //= 10                                                                   
#     # print('Сумма цифр числа: ', summ)
#     summ = 0
#     for sym in number:
#         summ += int(sym)
#     print('Сумма цифр числа: ', summ)

# def minNum(number):
#     min_num = int(number) % 10
#     for sym in number:
#         if int(sym) < min_num:
#             min_num = int(sym)
#     print('Минимальная цифра в числе: ', min_num)

# def maxNum(number):
#     max_num = 0
#     for sym in number:
#         if int(sym) > max_num:
#             max_num = int(sym)
#     print('Максимальная цифра в числе: ', max_num)
# while True:
#     number = input('Введите число: ')
#     print('Доступные над числом действия:\n1. Вывести сумму цифр числа.\n2. Вывести минимальную цифру числа.\n3. Вывести максимальную цифру числа.')
#     choice = int(input('Ваш выбор: '))
#     if choice == 1:
#         sumNum(number)
#     elif choice == 2:
#         minNum(number)
#     elif choice == 3:
#         maxNum(number)
#     else:
#         print('Ошибка выбора!')
#     print('=' * 50)
# 5 ==========================================================================
# def reverse_number(number):
#     num_rev = ''
#     while number != 0:
#         num = number % 10
#         if num != 0:
#             num_rev += str(num)
#         number = number // 10
#     print('Число наоборот:', num_rev)

# while True:
#     number = int(input('Введите число: ')) 
#     if number == 0:
#         print('Программа завершена!')
#         break
#     else:
#         reverse_number(number)
# 6 ==========================================================================
# def count_letters(text):
#     k = 0
#     n = 0
#     let_num = 0
#     num_numbers = 0
#     number = input('Какую цифру ищем? ')
#     letter = input('Какую букву ищем? ')
#     for sym in text:
#         flag = False
#         if sym != ' ':
#             for num in range(0, 10):
#                 if sym == str(num):
#                     flag = True
#                     k += 1
#                     if sym == number:
#                         num_numbers += 1
#                     break
#             if flag == False:
#                 n += 1
#                 if sym == letter:
#                     let_num += 1
#     print('Кол-во букв: ', n)
#     print('Кол-во цифр: ', k)
#     print('Количество букв', letter + ':', let_num)
#     print('Количество цифр', number + ':', num_numbers)

# text = input('Введите текст: ')
# count_letters(text)
# 7 ==========================================================================
# def second_number(X):
#     num = int((X - int(X))*100 % 10)
#     print('Вторая цифра числа', X,'после десятичной точки', num)

# X = float(input('Введите положительное действительное число: '))
# second_number(X)
# 8 ==========================================================================
# def verification(x, y):     # verification - проверка
#     if -1 <= x <= 1 and -1 <= y <= 1:
#         print('Монетка где-то рядом!')
#     else:
#         print('Монетки в области нет.')

# x = float(input('Введите координату X: '))
# y = float(input('Введите координату Y: '))
# verification(x, y)
# 9 ==========================================================================
# def greatest_number(a, b):
#     max_num = (abs(a - b) + a + b) / 2
#     print('Наибольшее число: ', max_num)

# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))
# greatest_number(a, b)
# 10 ==========================================================================
def gcd(a, b):      # greatest common divisor - Наибольший общий делитель (НОД)
    if a < b:
        minn = a
    else:
        minn = b
    for devisor in range(1, minn + 1):
        if a % devisor == 0 and b % devisor == 0:
            dev = devisor
    print('Наибольший общий делитель (НОД) равен: ', dev)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
gcd(a, b)
# 11 ==========================================================================
# def scanner(penny_one, penny_five, penny_ten, penny_fifty):
#     summ = (1 * penny_one + 5 * penny_five + 10 * penny_ten + 50 * penny_fifty) / 100
#     print('Всего у нас', summ,'рубля.')

# penny_one = int(input('Монет по 1 копейке: '))
# penny_five = int(input('Монет по 5 копеек: '))
# penny_ten = int(input('Монет по 10 копеек: '))
# penny_fifty = int(input('Монет по 50 копеек: '))
# scanner(penny_one, penny_five, penny_ten, penny_fifty)
# 12 ==========================================================================
# def mainMenu():     # Главное меню
#     print('Доступные игры:')
#     print('1. Камень, ножницы, бумага')
#     print('2. Угадай число')
#     choice = int(input('Выберете игру: '))
#     if choice == 1:
#         rock_paper_scissors()
#     elif choice == 2:
#         guess_the_number()
#     else:
#         print('Ошибка ввода: нужно ввести 1 или 2.')
#         mainMenu()

# def rock_paper_scissors():  # Игра "Камень, ножницы, бумага"
#     choice = input('Введите камень, ножницы или бумага: ')
#     victory = 'бумага'
#     print('Компьютер поставил -', victory,'\nВы поставили -', choice)
#     if choice == 'ножницы':
#         print('Поздравляем, Вы победили!')
#     elif choice == 'камень':
#         print('Вы проиграли!')
#     else:
#         print('Ничья! Попробуйте еще разок.')
#         rock_paper_scissors()

# def guess_the_number():     # Игра "Угадай число"
#     victory = 5
#     choice = int(input('Введите число: '))
#     if choice == victory:
#         print('Поздравляем, Вы угадали!')
#     else:
#         print('Не угадали! Попробуйте еще разок.')
#         guess_the_number()

# mainMenu()
# 13 ==========================================================================
# print('=' * 50)
# def mainMenu():
#     print('~' * 50)
#     print('Вас приветствует создатель этой игры, ildario')
#     print('Это текстовый квест')
#     print('Игрок находится в квартире, его задача — покинуть её.')
#     print('~' * 50)

# def bedroom():      # bedroom - спальня
#     print('-' * 50)
#     print('Вы в спальне. Куда идём?')
#     print('1 — в ванну')
#     print('2 — в коридор')
#     choice = int(input('Ваш выбор: '))
#     print()
#     if choice == 1:
#         bathroom()
#     elif choice == 2:
#         corridor()
#     else:
#         print('Ошибка ввода: нужно ввести 1 или 2.')
#         bedroom()

# def bathroom():     # bathroom - ванная комната
#     print('-' * 50)
#     print('Вы в ванне. Куда идём?')
#     print('1 — в коридор')
#     print('2 — в спальню')
#     choice = int(input('Ваш выбор: '))
#     print()
#     if choice == 1:
#         corridor()
#     elif choice == 2:
#         bedroom()
#     else:
#         print('Ошибка ввода: нужно ввести 1 или 2.')
#         bathroom()

# def corridor():     # corridor - корридор
#     print('-' * 50)
#     print('Вы в корридоре. Куда идём?')
#     print('1 — в спальню')
#     print('2 — в ванну')
#     print('3 — на кухню')
#     print('4 — в дверь')
#     choice = int(input('Ваш выбор: '))
#     print()
#     if choice == 1:
#         bedroom()
#     elif choice == 2:
#         bathroom()
#     elif choice == 3:
#         kitchen()
#     elif choice == 4:
#         print('Поздравлямба, Вы нашли выход и покинули квартиру!')
#         print('Игра окончена...')
#         print('-' * 50)
#     else:
#         print('Ошибка ввода: нужно ввести 1, 2, 3 или 4.')
#         corridor()

# def kitchen():      # kitchen - кухня
#     print('-' * 50)
#     print('Вы на кухне. Куда идём?')
#     print('1 — в окно')
#     print('2 — в коридор')
#     choice = int(input('Ваш выбор: '))
#     print()
#     if choice == 1:
#         print('Увы, Вы разбились :( и поэтому проиграли!')
#         print('Игра окончена...')
#         print('-' * 50)
#     elif choice == 2:
#         corridor()
#     else:
#         print('Ошибка ввода: нужно ввести 1 или 2.')
#         kitchen()

# mainMenu()
# bedroom()
# print('=' * 50)
# 14 ==========================================================================
# def func_2(num):
#     if num >= 5:
#         num -= 1
#         print(int(num), end = '')
#         number = int(num / 2)
#         print(number, end = '')
#         if num >= 5:
#             func_2(num)
        
# def func_1(num):
#     if num >= 3:
#         num = int(num / 2)
#         print(num, end = '')
#         if num >= 3:
#             func_1(num)

# num = float(input('Введите число: '))
# # number = num
# print(int(num), end = '')
# func_1(num)
# func_2(num)
# 15 ==========================================================================
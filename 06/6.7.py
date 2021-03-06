# Home Work
# 1 ==========================================================================
#  = int(input('Введите '))
'''Задача 1. Кубы чисел
Любителю математики Паше снова стало мало распечатанных табличек, включая последнюю со степенями двойки.
Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!
Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.
'''
# start_num = int(input('Введите с какого числа начать: '))
# end_num = int(input('Введите до какого числа считать: '))
# degree = int(input('Введите степень числа: '))
# while start_num <= end_num:
#     print(start_num**degree)
#     start_num += 1
# 2 ==========================================================================
'''Задача 2. Микроволновка
Ваня решил попрактиковаться в программировании и выбрал своей целью микроволновку. Он перепрограммировал её, 
и теперь на дисплее ведётся обратный отсчёт в секундах, а в конце проигрывается забавный звук.
Пользователь вводит число секунд seconds. Напишите программу, которая выводит на экран отсчёт от seconds до 0.

Пример:
Сколько секунд ждать? 5
5
4
3
2
1
0
'''
# seconds = int(input('Введите число секунд: '))
# counter = 0
# while seconds >= counter:
#     print(f'{seconds} c.')
#     seconds -= 1
# 3 ==========================================================================
'''Задача 3. Коллекторы
Напишите робота для коллекторов. В самом начале он спрашивает имя должника и сумму долга, а затем 
начинает требовать у него погашения до тех пор, пока он не введёт нужную сумму (равную сумме долга 
или больше). После погашения долга сообщите об этом пользователю и поблагодарите его.

Пример:
Василий, ваша задолженность составляет 100 рублей.
Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
Маловато, Василий. Давайте ещё раз.
Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
Маловато, Василий. Давайте ещё раз.
Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
Отлично, Василий! Вы погасили долг. Спасибо!
'''
# name = input('Введите Ваше имя: ')
# stop = True
# while stop:
#     print(f'Уважаемый {name}! Вы должны ПАО "Сбербанк" - 100000 рублей.')
#     sum = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
#     if sum == 100000:
#         print(f'Отлично, {name}! Вы погасили долг. Спасибо!')
#         stop = False
#     else:
#         print(f'Маловато, {name}. Давайте ещё раз.')
# print(f'А теперь, {name} можете пиздовать на все четыре стороны!')
# 4 ==========================================================================
'''Задача 4. Слишком большие числа
У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге. Напишите программу, которая считала бы для него, сколько десятичных цифр (знаков) во вводимом числе.
'''
# Вар 1
# num = int(input('Введите число: '))
# counter = 0
# while True:
#     remainder = num % 10   # remainder of devision - остаток от деления
#     if remainder != 0:
#         num //= 10
#         counter += 1
#     else:
#         print('Расчет законцен!')
#         break
# print(f'В веденном числе {counter} знаков.')

# Вар 2
# num = int(input('Введите число: '))
# counter = 0
# remainder = num % 10   # remainder of devision - остаток от деления
# while remainder != 0:
#     num //= 10
#     counter += 1
#     remainder = num % 10
# print(f'Расчет законцен!\nВ веденном числе {counter} знаков.')

# Вар 3
# num = int(input('Введите число: '))
# counter = 0
# while (num % 10) != 0:
#     num //= 10
#     counter += 1
# print(f'Расчет законцен!\nВ веденном числе {counter} знаков.')
# 5 ==========================================================================
'''Задача 5. Календари
Ваня увлекается историей, а в особенности календарями. Он изучает календари разных времён, эпох и 
народностей. Для исследования ему нужно посчитать, у кого сколько было месяцев с чётным количеством дней.
Напишите программу, которая считает количество только чётных чисел в последовательности 
(последовательность заканчивается при вводе нуля) и выводит ответ на экран.
'''
# counter = 0
# while True:
#     num = int(input('Введите число: '))
#     if num == 0:
#         break
#     elif num % 2 == 0:
#         counter += 1
# print('Количество введенных четных чисел:', counter)
# 6 ==========================================================================
'''Задача 6. Счастливый билетик
В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры, существовало 
поверье: если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх, то это к 
удаче. Напишите программу, которая получала бы на входе шестизначный номер билета и выводила, счастливый 
это билет или нет. К примеру, билеты 666 666 и 252 135 — счастливые, а 123 456 — нет. Подумайте, нужны ли 
для решения этой задачи циклы?
'''
# Вар 1
# print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
# print('=================================================')
# number = int(input('Введите шестизначный номер билета: '))
# num = number
# count = 0
# while (number % 10) != 0:
#     count += 1
#     number //= 10
# if count < 6 or count > 6:
#     print('Вы ввели нешестизначный номер билета!\nВведите номер билета правильно!')
#     print('=================================================')
# else:
#     # print(num % 10 + num % 100 // 10 + num % 1000 // 100)
#     # print(num // 1000 % 10 + num // 10000 % 10 + num // 100000)
#     if (num % 10 + num % 100 // 10 + num % 1000 // 100) == (num // 1000 % 10 + num // 10000 % 10 + num // 100000):
#         print('Поздравляем, Ваш билет счастливый!')
#         print('=================================================')
#     else:
#         print('У Вас обычный билет. Попробуйте еще раз.')
#         print('=================================================')

# Вар 2
# num = int(input('Введите шестизначный номер билета: '))
# if (num % 10 + num % 100 // 10 + num % 1000 // 100) == (num // 1000 % 10 + num // 10000 % 10 + num // 100000):
#     print('Поздравляем, Ваш билет счастливый!')
#     print('=================================================')
# else:
#     print('У Вас обычный билет. Попробуйте еще раз.')
#     print('=================================================')
# 7 ==========================================================================
'''Задача 7. Сумма арифметической последовательности
Напишите программу, которая получает на вход: число a — первый член прогрессии, d — разность 
арифметической прогрессии и число n — количество членов в прогрессии. Программа выводит каждый 
член прогрессии и их сумму в конце.

Пример:
Введите первый член прогрессии: 5
Введите разность: 3
Введите количество членов прогрессии: 4
5
8
11
14
Сумма арифметической прогрессии: 38
'''
# a_1 = int(input('Введите первый член прогрессии: '))
# d = int(input('Введите разность арифметической прогрессии: '))
# n = int(input('Введите количество членов в прогрессии: '))
# count = 0
# while count < n:
#     count += 1
#     print(a_1 + (count-1)*d)
# print(((2*a_1 + (count-1)*d)/2)*n)
# 8 ==========================================================================
'''Задача 8. Продолжаем бегать
В первый день спортсмен пробежал X километров, а затем он каждый день увеличивал пробег на 10% от 
предыдущего значения. По данному числу X определите номер дня, на который пробег спортсмена составит 
не менее Y километров.
'''
# print('=========================================================')
# Y = int(input('Введите пробег спортсмена: '))
# X = int(input('Сколько спортсмен пробежал в первый день? '))
# i = 1
# print(f'В {i}-й день спортсмен пробежал {X} км.')
# while True:
#     i += 1
#     X = X + X*0.1
#     print(f'В {i}-й день спортсмен пробежал {X} км.')
#     if X >= Y:
#         print('=========================================================')
#         print(f'На {i}-й день спортсмен пробежит больше (не менее) {Y} км.')
#         break
# print('=========================================================')
# 9 ==========================================================================
'''Задача 9. Поставьте оценку!
Вася выложил своё новое приложение на платформу для начинающих разработчиков, на ней пользователи 
могут ставить оценку приложению от −100 до 100. Ему захотелось сравнить количество положительных 
и отрицательных отзывов, для этого он заранее отфильтровал все отзывы так, чтобы в конце были те, 
которые равны нулю.
Напишите программу, которая находит количество положительных и количество отрицательных чисел в 
последовательности. Последовательность заканчивается на числе 0.

Пример:
Введите число: −4
Введите число: −90
Введите число: 6
Введите число: 0
Кол-во положительных чисел: 1
Кол-во отрицательных чисел: 2
'''
# positive = 0
# negative = 0
# while True:
#     num = int(input('Введите число: '))
#     if num == 0:
#         break
#     elif num < 0:
#         negative += 1
#     elif num > 0:
#         positive += 1
# print('Кол-во положительных чисел: ', positive)
# print('Кол-во отрицательных чисел: ', negative)
# 10 ==========================================================================
'''Задача 10. Обычный день на работе
Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему 
несколько задач, которые нужно решить до следующего рабочего часа. И вдобавок каждый час Максиму 
звонит супруга. Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
Напишите программу, в которой считается, сколько задач выполнил Максим за день (8 часов). Если он 
хоть раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
Пример:
Начался 8-часовой рабочий день
1 час
Сколько задач решит Максим? 1
Звонит жена. Взять трубку? 0
2 час
Сколько задач решит Максим? 2
Звонит жена. Взять трубку? 0
3 час
Сколько задач решит Максим? 3
Звонит жена. Взять трубку? 0
4 час
Сколько задач решит Максим? 4
Звонит жена. Взять трубку? 1
5 час
Сколько задач решит Максим? 5
Звонит жена. Взять трубку? 0
6 час
Сколько задач решит Максим? 1
Звонит жена. Взять трубку? 0
7 час
Сколько задач решит Максим? 2
Звонит жена. Взять трубку? 1
8 час
Сколько задач решит Максим? 3
Звонит жена. Взять трубку? 0
Рабочий день закончился. Всего выполнено задач: 21
Нужно зайти в магазин
'''
# print('=========================================================')
# print('Начался 8-часовой рабочий день')
# total = 0
# count = 0
# while count < 8:
#     count += 1
#     print(f'{count} час')
#     num = int(input('Сколько задач решит Максим? '))
#     total += num
#     telephone = int(input('Звонит жена. Взять трубку? (1/0) '))
#     if telephone == 1:
#         flag = 1
# print('Рабочий день закончился. Всего выполнено задач: ', total)
# if flag == 1:
#     print('Нужно зайти в магазин.')
# 11 ==========================================================================
'''Задача 11. Рекорд температуры
На метеостанции на экваторе постоянно замеряют температуру окружающей среды. Этот край известен тем, что 
там постоянно бьются рекорды высокой температуры. Специально для этого нужно написать программу, которая 
получает некоторую последовательность значений температур и определяет в ней самую высокую.
Напишите программу, которая определяет значение наибольшего элемента последовательности (последовательность 
заканчивается при вводе нуля).
'''
# t_max = 0
# while True:
#     t = int(input('Введите значение температуры: '))
#     if t == 0:
#         break
#     elif t > t_max:
#         t_max = t
# print('Самая высока температура =', t_max)
# 12 ==========================================================================
'''Задача 12. Вклады
Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть 
копеек отбрасывается. Определите, через сколько лет вклад составит не менее Y рублей. Напишите программу, 
которая по данным числам X, Y, P определяет, сколько лет пройдёт, прежде чем сумма достигнет значения Y.
'''
# print('=======================================================================')
# x = int(input('Введите сумму вклада: '))
# start = x
# p = float(input('Введите сумму ежегодного процента: '))
# y = int(input('Введите сумму до которой будем копить: '))
# print('          ----------------------------------')
# print('          |    Год    | Сумма на вкладе, руб.')
# print('          ----------------------------------')
# count = 0
# while True:
#     count += 1
#     x = x + x*p/100
#     print(f'          | {count}-й       | {x} ')
#     if x > y:
#         break
# print('          ----------------------------------')
# print('=======================================================================')
# print(f'Вклад в {start} рублей достигнет суммы в {y} рублей через {count} лет.')
# print('=======================================================================')
# 13 ==========================================================================
'''Задача 13. Игра «Угадай число»
В одном из домашних заданий мы делали задачу, где папа-программист написал для сына программу, которая просит 
его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, 
чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно 
немного улучшить саму игру.
Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите 
сообщения в соответствии с примером.
Пример (загадали число 7):
Введите число: 3
Число меньше, чем нужно. Попробуйте ещё раз!
Введите число: 10
Число больше, чем нужно. Попробуйте ещё раз!
Введите число: 8
Число больше, чем нужно. Попробуйте ещё раз!
Введите число: 7
Вы угадали! Число попыток: 4
'''
# print('=======================================================================')
# i = 0
# while True:
#     i += 1
#     num = int(input('Загадайте число от 0 до 10: '))
#     if num == 7:
#         print(f'Вы угадали! Число попыток: {i}')
#         break
#     elif num > 7:
#         print(f'Число больше, чем нужно. Попробуйте ещё раз!')
#     elif num < 7:
#         print(f'Число меньше, чем нужно. Попробуйте ещё раз!')
# 14 ==========================================================================
'''Задача 14. Игра «Компьютер угадывает число» (необязательная)
Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь мальчик загадывает число 
между 1 и 100 (включительно). Компьютер может спросить у мальчика: «Твое число равно, меньше или больше, 
чем число N?», где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из трёх 
чисел: 1 — равно, 2 — больше, 3 — меньше.
Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
'''
# Вар 1
# Функциям пока не учили, но я просто сделал т.к. уже есть знания от Нетологии
# Этот вариант я выполнил без подсказок, сам
# def compare(numm, n_nextt):                      # compare - сравнение
#     if num == n_next:
#         x = 1
#         print(f'{numm} = {n_nextt}')
#     elif num > n_next:
#         x = 2
#         print(f'{numm} > {n_nextt}')
#     else:
#         x = 3
#         print(f'{numm} < {n_nextt}')
#     return x
# print('====================================================================================')
# num = int(input('Загадай число от 1 до 100: '))
# print('====================================================================================')
# if num > 50:
#     n_prev = int(100 / 2)                           # 50 - начальное/опорное значение
#     n_next = int(n_prev + (100 - n_prev) / 2)       # 75
# else:
#     n_prev = int(100 / 2)                           # 50 - начальное/опорное значение
#     n_next = int(n_prev - (100 - n_prev) / 2)       # 25
# delta = (abs(n_next - n_prev) / 2)                  # 25
# i = 0
# j = 7
# while True:
#     i += 1
#     print(f'Осталось {j} попыток.')
#     print(f'n_prev = {n_prev}  |  n_next = {n_next}  |  delta = {delta}')
#     x = int(input(f'Загаданное Вами число равно, больше или меньше, чем {n_next}? (1 — равно, 2 — больше, 3 — меньше): '))
#     if num == 50:
#         print(f'Ура! Число угадано с {i}-й попытки и равно:', 50)
#         print('====================================================================================')
#         break
#     # x = compare(num, n_next)
#     if n_next % 2 == 0:
#         print(f'{n_next} - четное.')
#         if x == 2:
#             n_prev = n_next
#             n_next = int(n_prev + delta)
#         elif x == 3:
#             n_prev = n_next
#             n_next = int(n_next - delta)
#         elif x == 1:
#             print(f'Ура! Число угадано с {i}-й попытки и равно:', n_next)
#             print('====================================================================================')
#             break
#     else:
#         print(f'{n_next} - не четное.')
#         # n_next = int(n_next)
#         if x == 2:
#             n_prev = n_next
#             n_next = int(n_prev + delta)
#         elif x == 3:
#             n_prev = n_next
#             n_next = int(n_next - delta)
#         elif x == 1:
#             print(f'Ура! Число угадано с {i}-й попытки и равно:', n_next)
#             print('====================================================================================')
#             break
#
#     delta = (abs(n_next - n_prev) / 2)
#
#     if delta == 0.5:
#         delta = 2*0.5
#
#     # if i > 10:
#     #     break
#
#     print('====================================================================================')
#
#     j -= 1
#     if j == 0:
#         print(f'======================================')
#         print(f'Все мужик, ты проебал все {i} попыток, сорян!')
#         break

# Вар 2
# Правильное решение методом бинарного поиска (Решение от SkillBox)
# print('===================================================================================================')
# i = 0
# N_left = 1                                  #
# N_right = 100                               #
# while True:
#     i += 1
#     N_aver = (N_left + N_right) // 2
#     print(f'| {i}-я  п о п ы т к а: Левая граница = {N_left}  |  Середина = {N_aver}  |  Правая граница = {N_right}                |')
#     print(f'  ```` ````````````````')
#     print(f'|      Твое число равно, больше или меньше, чем {N_aver}?                                               |')
#     answer = int(input('|      1 — равно, 2 — больше, 3 — меньше:                                                         |\n                                Ваш ответ - '))
#     if answer == 1:
#         print(' =================================================================================================')
#         print(f'|                                 Ура! Я угадал с {i}-й попытки.                                    |')
#         print('|                                ``````````````````````````````                                   |')
#         print(' =================================================================================================')
#         break
#     elif answer == 2:
#         N_left = N_aver + 1                 #
#     elif answer == 3:
#         N_right = N_aver - 1               #
#     else:
#         print('|  Введите ответ по инструкции: 1 — равно, 2 — больше, 3 — меньше!  |')
#     print('===================================================================================================')

# Вар 3
# Редактирование своего варианта на основе правильного решения
# print('====================================================================================')
# num = int(input('Загадай число от 1 до 100: '))
# print('====================================================================================')
#
# n_prev = 1                           # 50 - начальное/опорное значение
# n_next = 100
# i = 0
# j = 7
# while True:
#     i += 1
#     print(f'Осталось {j} попыток.')
#     N = (n_next + n_prev) // 2                  #
#     print(f'n_prev = {n_prev}  |  n_next = {n_next}  |  Aver = {N}')
#     x = int(input(f'Загаданное Вами число равно, больше или меньше, чем {N}? (1 — равно, 2 — больше, 3 — меньше): '))
#     if x == 2:
#         n_prev = N
#         N = (n_next + n_prev) // 2
#     elif x == 3:
#         n_next = N
#         N = (n_next + n_prev) // 2
#     elif x == 1:
#         print(f'Ура! Число угадано с {i}-й попытки и равно:', n_next)
#         print('====================================================================================')
#         break
#     else:
#         print('|  Введите ответ по инструкции: 1 — равно, 2 — больше, 3 — меньше!  |')
#     print('====================================================================================')
#     j -= 1
#     if j == 0:
#         print(f'======================================')
#         print(f'Все мужик, ты потратил все {i} попыток, сорян!')
#         break

# Вар 4
# Редактирование своего варианта на основе правильного решения
# print('====================================================================================')
# num = int(input('Загадай число от 1 до 100: '))
# print('====================================================================================')
# n_prev = 1
# n_next = 100
# i = 0
# j = 7
# while True:
#     i += 1
#     print(f'{i}-я итерация:\n`````````````')
#     aver = (n_prev + n_next) // 2        # 50 - начальное/опорное значение
#     delta = (abs(aver) // 2)             # 25
#     print(f'n_prev = {n_prev}  |  n_next = {n_next}|  aver = {aver}  |  delta = {delta}')
#     x = int(input(f'Загаданное Вами число равно, больше или меньше, чем {aver}? (1 — равно, 2 — больше, 3 — меньше): '))
#     if x == 2:
#         n_prev = aver + 1
#     elif x == 3:
#         n_next = aver - 1
#     elif x == 1:
#         print(f'Ура! Число угадано с {i}-й попытки и равно:', aver)
#         print('====================================================================================')
#         break
#     else:
#         print(f'Неверное число!')
#     print('====================================================================================')

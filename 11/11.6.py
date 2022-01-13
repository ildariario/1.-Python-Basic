# Task 1



# Task 2



# Task 3



# Home Work
# 1 ==========================================================================
# buy = float(input('Введите стоимость покупки в евро: ')) # buy - покупка

# price_Dollar = 60.87                # Цена за доллар в рублях
# price_Euro = 1.25 * price_Dollar    # Цена за евро в рублях

# price_Doll = buy * 1.25             # Цена покупки в долларах
# price_Rub = buy * price_Euro        # Цена покупки в рублях

# print('Стоимость покупки в долларах: ', price_Doll)
# print('Стоимость покупки в рублях: ', price_Rub)
# 2 ==========================================================================
# p0 = float(input('Введите давление p0 измеренное при 0 градусов: '))
# temp = float(input('Введите температуру воздуха: '))

# p = p0 * (273 + temp) / 273
# print('Давление в шинах: ', p)
# 3 ==========================================================================
# import math

# quantity = int(input('Введите количество чисел в последовательности: '))
# for sequence in range(quantity):
#     num = float(input(f'Введите {sequence+1}-е число последовательности: '))
#     if num < 0:
#         num = math.floor(num)
#         print('x =', num, end = ' ')
#         print('exp(x) =', math.exp(num), end = '')
#     else:
#         num = math.ceil(num)
#         print('x =', num, end = ' ')
#         print('log(x) =', math.log(num), end = '')
#     print()
# 4.1 ==========================================================================
# N = int(input('Сколько символов в сообщении? '))

# K = 0
# while True:
#     K += 1
#     if 2 ** K >= N:
#         break
#     else:
#         print(f'{K} бит недостаточно для шифровки сообщения из {N}-ти символов!')
# print(f'Минимальное кол-во бит для кодирования {N} символов равно: ', K)
# 4.2 ==========================================================================
# import math

# N = int(input('Сколько символов в сообщении? '))

# for K in range(1, N+1):
#     if math.log2(N) <= K:
#         print(f'Минимальное кол-во бит для кодирования {N} символов равно: ', K)
#         break
#     elif math.log2(N) != K:
#         print(f'{K} бит недостаточно для шифровки сообщения из {N}-ти символов!')
# 5 ==========================================================================
# import math

# size = float(input('Укажите размер файла для скачивания (в мегабайтах): '))
# speed = float(input('Какова скорость вашего соединения (в мегабайтах в секунду): '))
# sec = 0
# current_size = 0

# while current_size < size:
#     sec += 1
#     current_size = int(speed * sec)
#     cur_size_in_percent = math.ceil(current_size * 100 / size)
#     if current_size >= size:
#         print(f'Прошло {sec} сек. Скачано {int(size)} из {int(size)} Мб ({100} %)')
#     else:
#         print(f'Прошло {sec} сек. Скачано {current_size} из {int(size)} Мб ({cur_size_in_percent} %)')
# 6 ==========================================================================
# X = float(input('Действительное число: '))

# num = int(X * 10) % 10

# print(f'Первая его цифра после запятой: ', num)
# 7 ==========================================================================
# import math

# R_planet = float(input('Введите радиус случайной планеты: '))

# V_earth = 10.8321 * 10 ** 11
# V_planet = (4/3) * math.pi * R_planet ** 3
# num = round(V_earth / V_planet, 3)

# if num > 1:
#     print('Объём планеты Земля больше в', num, 'раз.')
# elif num < 1:
#     num = round(1 / num, 3)
#     print('Объём планеты Земля меньше в ', num, 'раз.')
# else:
#     print('Объём планеты Земля и объем случайной планеты равны!')
# 8 ==========================================================================
# print('=' * 50)
# lower_temp_limit = int(input('Нижняя граница: '))     # lower temperature limit - нижняя граница температуры
# upper_temp_limit = int(input('Верхняя граница: '))    # upper temperature limit - верхняя граница температуры
# step = int(input('Шаг: '))
# print()
# print('Вывод: ')
# print('-' * 17)
# print('|   C', end = '\t|')
# print('   F', '\t|')
# print('-' * 17)

# for t_C in range(lower_temp_limit, upper_temp_limit + 1, step):
#     t_F = int(1.8 * t_C + 32)
#     print('| ', t_C, end = '\t')
#     print('| ', t_F, '\t|')
#     if t_C == upper_temp_limit:
#         break
# else:
#     t_C = upper_temp_limit
#     t_F = int(1.8 * t_C + 32)
#     print('| ', t_C, end = '\t')
#     print('| ', t_F, '\t|')
# print('-' * 17)
# 9 ==========================================================================
# import math

# print('Введите размеры бруска')
# x = float(input('X: '))
# y = float(input('Y: '))
# z = float(input('Z: '))

# size_cube = 5
# k_1 = int(x / size_cube)
# k_2 = int(y / size_cube)
# k_3 = int(z / size_cube)
# num_cube = k_1 * k_2 * k_3
# kit = int(math.pow(num_cube, 1/3)) ** 3

# print('Из этого бруска можно изготовить', num_cube, 'кубиков')
# print('Из них можно составить набор из', kit, 'кубиков')
# 10 ==========================================================================
# import math

# alpha = float(input('Введите угол тангажа в градусах: '))

# if abs(alpha) > 360:
#     alpha = round(((alpha / 360) - int(alpha / 360)) * 360, 3)
#     print('Угол: ', alpha, 'градуса.')

# if alpha < -0.28 * 180 / math.pi or alpha > 0.28 * 180 / math.pi:
#     print('Угол небезопасен!')
# else:
#     print('Угол безопасен.')
# 11 ==========================================================================
# print('=' * 70)
# flag = False
# coef = 1

# print('Введите местоположение коня: ')
# x_1 = float(input('- по горизонтали: '))
# y_1 = float(input('- по вертикали: '))

# print('Введите местоположение точки на доске: ')
# x_2 = float(input('- по горизонтали: '))
# y_2 = float(input('- по вертикали: '))
# print()

# if x_1 > 0 and x_1 < 0.8 and y_1 > 0 and y_1 < 0.8:
#     xx_1 = int(x_1 * 10)
#     yy_1 = int(y_1 * 10)  
#     print(f'Конь находится в клетке: ({xx_1}, {yy_1})', end = ' ')
#     xx_2 = int(x_2 * 10)
#     yy_2 = int(y_2 * 10)  
#     print(f'Точка в клетке: ({xx_2}, {yy_2}).')

#     for i in range(1, 3):
#         if i == 2:
#             coef = -1
#         if (xx_2 == xx_1 + i and yy_2 == yy_1 - (i + coef)) or (xx_2 == xx_1 + i and yy_2 == yy_1 + (i + coef)) or (xx_2 == xx_1 - i and yy_2 == yy_1 - (i + coef)) or (xx_2 == xx_1 - i and yy_2 == yy_1 + (i + coef)): 
#             flag = True
#     if flag == True:
#         print('Да, конь может ходить в эту точку.')
#     else:
#         print('Нет, конь не может ходить в эту точку.')
# else:
#     print('Клетки с такой координатой не существует')
# print('=' * 70)
# 12 ==========================================================================
# h = float(input('Введите кол-во часов: '))
# m = float(input('Введите кол-во минут: '))
# s = float(input('Введите кол-во секунд: '))

# hours = h + (m * 1 / 60) + (s * 1 / 3600)
# angle_hour = hours * 30
# print('Общее кол-во часов: ', hours)
# print('С начала суток часовая стрелка повернулаcь на угол', angle_hour, 'градусов.')
# 13 ==========================================================================
# alpha = float(input('Введите угол на который повернута часовая стрелка: '))

# # На одно деление часовой стрелки (30 град. на циферблате) минутная делает 360 град.
# # При повороте часовой стрелки на 1 град. минутная повернется на betta = 12 град.
# # Т.О. на на 1 градус часовой стрелки приходится 12 градусов минутной стрелки
# betta = 360 / 30   

# alpha /= 30
# delta = alpha - int(alpha)
# angle_min_hand = round(delta * 30 * betta, 3)      # minute hand - минутная стрелка

# print('Минутная стрелка с начала последнего часа повернулась \nна угол', angle_min_hand, 'градусов.')
# 14 ==========================================================================
# print('='*50)
# import math as m

# a = float(input('Введите a: '))
# b = float(input('Введите b: '))
# c = float(input('Введите c: '))

# D = b ** 2 - 4 * a * c
# print('Дискриминант равен: ', D)

# if D > 0:
#     x_1 = (-b + m.sqrt(D)) / (2 * a)
#     x_2 = (-b - m.sqrt(D)) / (2 * a)
#     if x_1 > x_2:
#         print(x_2, x_1)
#     else:
#         print(x_1, x_2)
# elif D == 0:
#     x_1_2 = (-b) / (2 * a)
#     print(x_1_2)
# else:
#     print('Корней нет!')
# print('='*50)
# 15 ==========================================================================
# Сам не решил!
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

maxx = round(((a + b) + abs(a - b)) / 2, 2)

print('Наибольшее число: ', maxx)
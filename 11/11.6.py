# Home Work
# 1 ==========================================================================
'''Задача 1. Конвертация
При покупках за рубежом с помощью карты банки делают конвертацию через промежуточную валюту.
Например, если купить что-то в евро, то сначала эта сумма конвертируется в доллары, а уже
потом - в рубли.
Напишите программу, которая получает на вход стоимость покупки в евро, затем выводит ответ
в рублях. Мы живём в альтернативной реальности, где 1 евро = 1.25 доллара,
а 1 доллар = 60.87 рублей.
'''
# buy = float(input('Введите стоимость покупки в евро: ')) # buy - покупка

# price_Dollar = 60.87                # Цена за доллар в рублях
# price_Euro = 1.25 * price_Dollar    # Цена за евро в рублях

# price_Doll = buy * 1.25             # Цена покупки в долларах
# price_Rub = buy * price_Euro        # Цена покупки в рублях

# print('Стоимость покупки в долларах: ', price_Doll)
# print('Стоимость покупки в рублях: ', price_Rub)
# 2 ==========================================================================
'''Задача 2. Колёса
В одном велосипедном магазине такой наплыв покупателей, что продавцы просто не успевают 
работать. А ведь сборка велосипедов требует внимания и в том числе нужно, чтобы давление 
в шинах было самым оптимальным. При этом это давление также зависит и от температуры воздуха. 
Сама формула расчёта давления в шинах выглядит следующим образом: p = p0*(273+t)/273
Напишите программу, которая получает на вход давление p0 (это давление, измеренное 
при 0 градусов) и температуру воздуха t. Программа выводит искомое давление p.
'''
# p0 = float(input('Введите давление p0 измеренное при 0 градусов: '))
# temp = float(input('Введите температуру воздуха: '))

# p = p0 * (273 + temp) / 273
# print('Давление в шинах: ', p)
# 3 ==========================================================================
'''Задача 3. Грубая математика
В одном аналитическом центре, где занимаются разного рода математическим анализом, 
работал практикант, который написал программу для расчёта некоторых функций. Правда, 
он в тот день очень устал и немного не так прочитал техническое задание и функции 
теперь рассчитываются довольно грубо.
Вводится последовательность из N вещественных чисел. При этом положительные числа 
округляются вверх, отрицательные округляются вниз. Напишите программу, которая 
выводит натуральный логарифм от числа, если оно положительное, и экспоненту в 
степени числа, если оно отрицательное.
Пример:
Введите кол-во чисел: 3
Введите число: 1.3
x = 2   log(x) = 0.6931471805599453
Введите число: -2.1
x = -3   exp(x) = 0.049787068367863944
Введите число: -5.9
x = -6   exp(x) = 0.0024787521766663585
'''
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
# 4 ==========================================================================
'''Задача 4. Кодирование сообщений
В компьютерах символы представляются в виде двоичного кода - это нолики и единицы. 
Память компьютера состоит из бит - это один разряд двоичного кода. Сообщение состоит 
из N символов.   С помощью K бит можно закодировать 2**K различных вариантов.
Пример 1: в сообщении 8 символов. Тогда K будет равен трём. (2**3 = 8)
Пример 2: в сообщении 10 символов. Если возьмём K = 3, то 2**3 = 8, следовательно 
все символы мы не закодируем. Значит, нужно взять K = 4 (2**4 = 16)
Напишите программу, которая выводит сколько нужно минимально выделить бит для 
кодирования сообщения из N символов. Если количество символов - это не степень двойки, 
то вывести соответствующее сообщение. Для этого можно использовать проверку “если 
двоичный логарифм от N не равен K”.
'''
# Вар 1
# N = int(input('Сколько символов в сообщении? '))

# K = 0
# while True:
#     K += 1
#     if 2 ** K >= N:
#         break
#     else:
#         print(f'{K} бит недостаточно для шифровки сообщения из {N}-ти символов!')
# print(f'Минимальное кол-во бит для кодирования {N} символов равно: ', K)

# Вар 2
# import math

# N = int(input('Сколько символов в сообщении? '))

# for K in range(1, N+1):
#     if math.log2(N) <= K:
#         print(f'Минимальное кол-во бит для кодирования {N} символов равно: ', K)
#         break
#     elif math.log2(N) != K:
#         print(f'{K} бит недостаточно для шифровки сообщения из {N}-ти символов!')
# 5 ==========================================================================
'''Задача 5. Убийца Steam
Вы пишете программу-инсталлятор для компьютерной игры. Пока инсталлятор скачивает 
обновление, пользователю нужно показать сколько процентов уже скачалось, чтобы он 
мог решить пойти заварить чаю, или подождать у экрана компьютера. Обновления игры 
всегда занимают разное количество мегабайт, да и скорость интернет-соединения у игроков разная.
Напишите программу, принимающую на вход размер файла обновления в мегабайтах и 
скорость интернет соединения в мегабайтах в секунду. Для каждой секунды программа 
рассчитывает и выводит на экран сколько процентов от всего объема уже скачано, до 
тех пор пока не будет скачан весь объем. В конце программа должна показать сколько 
всего секунд заняло скачивание обновления. Обеспечьте контроль ввода.
Пример:
Укажите размер файла для скачивания: 123
Какова скорость вашего соединения? 27
Прошло 1 сек. Скачано 27 из 123 Мб (22%)
Прошло 2 сек. Скачано 54 из 123 Мб (44%)
Прошло 3 сек. Скачано 81 из 123 Мб (66%)
Прошло 4 сек. Скачано 108 из 123 Мб (88%)
Прошло 5 сек. Скачано 123 из 123 Мб (100%)
'''
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
'''Задача 6. Первая цифра
Дано положительное действительное число X. Выведите его первую цифру после десятичной 
точки. При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками.
'''
# X = float(input('Действительное число: '))

# num = int(X * 10) % 10

# print(f'Первая его цифра после запятой: ', num)
# 7 ==========================================================================
'''Задача 7. Вот это объёмы!
Для курсовой работы по физике Андрею нужно сравнить объёмы двух планет: Земли и 
какой-нибудь случайной, которая может в теории существовать в нашей вселенной. 
Андрей хорошо разбирается в формулах, а вот считать что-то, а уж тем более самому - 
это явно не его. Объём Земли ему известен заранее  - это 10.8321 * 1011 км3
А вот объём случайной планеты ему нужно будет посчитать. Благо, у него есть формула
V = (4/3) * pi * R^3
где V - это объём, pi - число пи, а R - радиус планеты.
Напишите программу, которая получает на вход радиус случайной планеты и выводит на экран во сколько раз планета Земля меньше или больше по объёму. Ответ округлите до трёх знаков после запятой
Пример:
Введите радиус случайной планеты: 3389.5
Объём планеты Земля больше в 6.641 раз
Пример 2:
Введите радиус случайной планеты: 7000
Объём планеты Земля меньше в (1/0.754) = 1.326 раз
'''
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
'''Задача 8. Метеостанция
Для удобства работы сотрудников международной метеостанции каждый день нужно 
распечатывать различные таблицы соответствия градусов по шкале Цельсия и Фаренгейта. 
Напишите программу, которая принимает на вход три целых числа в градусах Цельсия: 
нижняя граница температуры, верхняя граница температуры и шаг. Программа выводит 
на экран таблицу соответствия градусов Цельсия градусам Фаренгейта от нижней до 
верхней границы с указанным шагом. Обеспечьте контроль ввода. Верхняя граница 
должна печататься, даже если последний шаг “перепрыгнул “ ее. Известно, что 0С 
соответствует 32F, а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта. 
Пример:
Ввод:
Нижняя граница: 0
Верхняя граница: 50
Шаг: 20
Вывод:
C        F
0        32
20       68
40       104
50       122
'''
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
'''Задача 9. Игрушечная история
Вы решили открыть свой бизнес по производству игровых деревянных кубиков для детей. 
Вы узнали, что лучше всего продаются кубики со стороной 5 см в наборах по несколько 
штук, причём в одном наборе должно быть столько кубиков, чтобы из них можно было 
сложить один большой куб. Для изготовления кубиков к вам в мастерскую поступают 
деревянные бруски в форме прямоугольных параллелепипедов любых размеров.
Для оптимизации бизнес-процессов напишите программу, которая по заданным размерам 
исходного бруска определяет сколько кубиков из него можно изготовить и можно ли из 
них составить набор для продажи, и если можно, то максимальное число кубиков в этом 
наборе. Все кубики должны быть из цельного дерева, без использования клея. Размеры 
бруска - вещественные числа.
Пример:
Введите размеры бруска
X: 5
Y: 35.76
Z: 35.05
Из этого бруска можно изготовить 49 кубиков
Из них можно составить набор из 27 кубиков
'''
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
'''Задача 10. Автопилот.
Одна из базовых частей программы автопилота пассажирских самолётов - контроль угла 
тангажа. Угол тангажа - это вертикальное направление носа самолёта, то есть угол 
между продольной осью самолёта и осью Х - горизонтальной прямой, параллельной земле. 
Если тангаж положительный, значит нос самолёта смотрит вверх, а если отрицательный - 
то вниз, в этом случае самолёт пикирует. Слишком маленький и слишком большой угол 
тангажа опасны потерей управления. У самолёта SKB-1 допустимый угол тангажа лежит 
в пределах от -0.28 до 0.28 радиан. Вам поручено написать код, проверяющий лежит 
ли введённый пользователем угол в этих пределах. Пользователь вводит угол в градусах. 
Используйте как можно меньше конструкций if. Обеспечьте контроль ввода. Не забывайте, 
что угол может быть и больше 360 градусов, и меньше 0
Пример 1:
Введите угол тангажа в градусах: -28
Угол небезопасен!
Пример 2:
Введите угол тангажа в градусах: 724
Угол безопасен.
'''
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
'''Задача 11. Ход конём
В рамках разработки шахматного ИИ стоит новая задача. По заданным вещественным координатам 
коня и второй точки программа должна определить может ли конь ходить в эту точку. 
Используйте как можно меньше конструкций if и логических операторов. Обеспечьте 
контроль ввода.
Пример:
Введите местоположение коня:
0.071
0.118
Введите местоположение точки на доске:
0.213
0.068
Конь в клетке (0, 1). Точка в клетке (2, 0).
Да, конь может ходить в эту точку.
'''
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
'''Задача 12. Часы
С начала суток прошло H часов, M минут, S секунд (0≤H<12, 0≤M<60, 0≤S<60). По данным 
числам H, M, S определите угол (в градусах), на который повернулаcь часовая стрелка 
с начала суток и выведите его в виде действительного числа.
При решении этой задачи нельзя пользоваться условными операторами и циклами.
'''
# h = float(input('Введите кол-во часов: '))
# m = float(input('Введите кол-во минут: '))
# s = float(input('Введите кол-во секунд: '))

# hours = h + (m * 1 / 60) + (s * 1 / 3600)
# angle_hour = hours * 30
# print('Общее кол-во часов: ', hours)
# print('С начала суток часовая стрелка повернулаcь на угол', angle_hour, 'градусов.')
# 13 ==========================================================================
'''Задача 13. Часы 2
С начала суток часовая стрелка повернулась на угол в α градусов. Определите на какой 
угол повернулась минутная стрелка с начала последнего часа. Входные и выходные данные 
— действительные числа.
При решении этой задачи нельзя пользоваться условными операторами и циклами.
'''
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
'''Задача 14. Уравнение
Даны действительные коэффициенты a, b, c, при этом a≠0. Решите квадратное уравнение 
ax^2+bx+c=0 и выведите все его корни. Если уравнение имеет два корня, выведите два 
корня в порядке возрастания, если один корень — выведите одно число, если нет корней 
— не выводите ничего.
'''
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
'''Задача 15. За что? (необязательно)
Вы встретились со своим старым другом, который тоже изучает программирование, правда, 
в другом учебном заведении. За чашкой кофе он пожаловался вам, что сумасбродный препод 
дал им задание написать программу, которая из двух введённых чисел определяет наибольшее, 
не используя при этом условных операторов и циклов. Радуясь, что на вашем курсе такого 
не требуют, вы всё-таки решаете помочь своему другу. Напишите для него эту программу.
Пример:
Введите первое число: 10
Введите второе число: 5
Наибольшее число: 10
'''
# Решить самому не получилось!
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

maxx = round(((a + b) + abs(a - b)) / 2, 2)

print('Наибольшее число: ', maxx)

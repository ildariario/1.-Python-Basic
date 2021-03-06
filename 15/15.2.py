'''Работа за преподавателем'''
# Task 1

# scores = [8, 5, 10, 7, 6]
# print(scores)
#
# scores[1] *= 3
# x = scores[4]
# x += 10
#
# print(scores)
# print(x)

# Task 2

# monsters_count = int(input('Количество монстров: '))
# mage_index = int(input('Номер мага в списке: '))
#
# monsters_damage = []
#
# for monster in range(monsters_count):
#     print('Урон у', monster + 1, 'монстра:', end=' ')
#     damage = int(input())
#     monsters_damage.append(damage)
#
# print(monsters_damage)
#
# for i_monster in range(monsters_count):
#     if monster_damage[i_monster] < 100 and i_monster != mage_index - 1:
#         monsters_damage[i_monster] += monsters_damage[mage_index - 1]

# Home Work
# 1 ==========================================================================
'''Задача 1. Гугл
Программисты постоянно гуглят ошибки и ищут уже готовый код, который можно использовать 
для своей программы, чтобы не изобретать велосипед. Андрей поступил также и нашёл для 
своего проекта код, который должен находить минимальное и максимальное числа в списке. 
Вот этот код:
nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
 num = int(input('Очередное число: '))
 nums_list.append(num)
maximum = 0
minimum = -1
for i in nums_list:
 if maximum < i:
   maximum = i
 if minimum > i:
   minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)
Однако он столкнулся с проблемой. Если брать, к примеру, количество чисел 5, то на 
тестах -1 -2 -3 -4 -5 и 1 2 3 4 5 программа выводит неверный результат. 
Доработайте программу так, чтобы она выводила верный результат. Подсказка: для 
отладки используйте точки останова.
'''
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = 0
# minimum = -1
#
# for element in nums_list:
#     if maximum < element:
#         maximum = element
#     else:
#         maximum = -1
#     if minimum > element:
#         minimum = element
#     else:
#         minimum = 1
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)
# 2 ==========================================================================
'''Задача 2. Кратность
Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму 
индексов элементов списка, которые кратны K.

Пример:
Кол-во чисел в списке: 4
Введите 1 число: 1
Введите 2 число: 20
Введите 3 число: 30
Введите 4 число: 4

Введите делитель: 10

Индекс числа 20: 1
Индекс числа 30: 2
Сумма индексов: 3
'''
# N = int(input('Кол-во чисел в списке: '))
# list_element = []
# summ = 0
#
# for i in range(N):
#     print('Введите', i + 1, 'число: ', end='')
#     element = int(input(''))
#     list_element.append(element)
#
# K = int(input('Введите делитель: '))
#
# for i in range(N):
#     if list_element[i] % K == 0:
#         print('Индекс числа', list_element[i], ':', i)
#         summ += i
#
# print('Сумма индексов: ', summ)
# 3 ==========================================================================
'''Задача 3. Собачьи бега
В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков 
за сезон. На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен 
баг: собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.
Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и 
наименьший элементы в списке.
'''
N = int(input('Введите количество собак: '))
list_of_dog = []
flag = False

for i in range(N):
    print('Введите очки', i + 1, '- й собаки: ', end='')
    elem = int(input())
    list_of_dog.append(elem)

    if flag == False:
        maxx, minn = list_of_dog[0], list_of_dog[0]
        max_i, min_i = i, i
        flag = True

    if elem > maxx and i >= 1:
        maxx = elem
        max_i = i
    if elem < minn and i >= 1:
        minn = elem
        min_i = i

print(list_of_dog)

list_of_dog[max_i], list_of_dog[min_i] = minn, maxx

print(list_of_dog)

# Home Work
# 1 ==========================================================================
'''Задача 1. Страшный код
Вашему другу, который тоже начал изучать Python, преподаватель дал такую задачу: есть
три списка — основной и два побочных. В основном лежат элементы [1, 5, 3], а в
побочных [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.
Первый побочный закидывается в основной, там считается количество цифр 5, количество
выводится на экран, и затем они удаляются из основного списка. После этого в основной
закидывается второй побочный список, там считается количество цифр 3 и выводится на экран.
В конце также выводится и сам список.

Из интереса вы попросили вашего друга показать код его программы и поняли, что сделали
это не зря — то, что вы увидели, повергло вас в шок и ужас. Вот сам код:
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)

Используя знания о методах списков, а также о стиле программирования, помогите другу
переписать программу. Не используйте дополнительные списки.

Результат работы программы:
Кол-во цифр 5 при первом объединении: 3
Кол-во цифр 3 при втором объединении: 4
Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
'''
# Пропустил
# 2 ==========================================================================
'''Задача 2. Шеренга
Два класса стоят в две отдельные шеренги. В каждом классе ученики выстроены по росту 
(по возрастанию): в одном классе от 160 см до 176 см с шагом 2, во втором классе — 
от 162 см до 180 см с шагом 3. Спустя какое-то время два класса объединяют в одну 
шеренгу и тоже выстраивают их по возрастанию.
Напишите программу, которая генерирует списки роста для каждого в классе, затем 
объединяет их в один список и сортирует его в порядке возрастания. Выведите отсортированный 
список на экран.
'''
# Пропустил
# 3 ==========================================================================
'''Задача 3. Детали
В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], 
['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
Продавец решил, что считать количество и стоимость деталей вручную не очень удобно, 
поэтому решил попросить помощи у программиста, чтобы оптимизировать этот процесс.
Напишите программу, которая запрашивает у пользователя деталь, считает их количество, 
а также общую стоимость.

Пример:
Название детали: седло

Кол-во деталей - 3  
Общая стоимость - 4500
'''
# Пропустил
# 4 ==========================================================================
'''Задача 4. Вечеринка
В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал 
рассылать приглашения, а просто сообщил всем: «Если хотите — приходите и своих друзей 
тоже зовите». В ходе вечеринки люди приходили и уходили, ночевать остались не все. 
К тому же и сама дача не резиновая — на ней помещается всего шесть человек.
Дан изначальный список гостей — имена тех, кто пришёл к началу:
guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый 
гость, и исходя из ответа добавляет в список или удаляет из него нужное имя. При этом 
гостей может быть не больше шести. Имена запрашиваются до тех пор, пока пользователь не 
введёт сообщение «Пора спать».
Пример:
Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
Гость пришёл или ушёл? пришёл
Имя гостя: Алекс
Привет, Алекс!

Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
Гость пришёл или ушёл? пришёл
Имя гостя: Гоша
Прости, Гоша, но мест нет.

Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
Гость пришёл или ушёл? ушёл
Имя гостя: Ваня
Пока, Ваня!

Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’,  ‘Алекс’]
Гость пришёл или ушёл? Пора спать

Вечеринка закончилась, все легли спать.
'''
# Пропустил
# 5 ==========================================================================
'''Задача 5. Песни
Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен 
группы Depeche Mode. Каждая песня состоит из названия и продолжительности с точностью до 
долей минут:

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. 
И при этом ему важно, сколько времени в сумме эти N песен будут звучать.
Напишите программу, которая запрашивает у пользователя количество песен из списка и затем 
названия этих песен, а на экран выводит общее время их звучания.

Пример:
Сколько песен выбрать? 3
Название 1 песни: Halo
Название 2 песни: Enjoy the Silence
Название 3 песни: Clean

Общее время звучания песен: 14.93 минут
'''
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
# total_time = 0
#
# num_select = int(input('Сколько песен выбрать? '))
#
# for i_sel in range(num_select):
#     print('Название', i_sel + 1, 'песни: ', end='')
#     song_name = input()
#     for i_song in range(len(violator_songs)):
#         if song_name == violator_songs[i_song][0]:
#             total_time += violator_songs[i_song][1]
#
# print('Общее время звучания песен: ', round(total_time, 2))
# 6 ==========================================================================
'''Задача 6. Уникальные элементы
Даны два списка целых чисел, оба списка заполняются с клавиатуры. В первый список 
вводится три числа, во второй — семь чисел. Напишите программу, которая запрашивает 
у пользователя эти числа, затем расширяет первый список элементами второго и после этого 
оставляет в первом списке только уникальные элементы, то есть удаляет лишние повторы чисел. 
Условный оператор использовать нельзя.

Пример:
# ввод чисел опустим
Первый список: [1, 2, 3]
Второй список: [2, 4, 6, 3, 3, 2, 1]

Новый первый список с уникальными элементами: [4, 6, 3, 2, 1]

[1, 2, 3, 2, 4, 6, 3, 3, 2, 1]
'''
# first_list = []
# second_list = []
#
# for i_first in range(3):
#     num = int(input(f'Введите {i_first + 1}-е число для 1-го списка: '))
#     first_list.append(num)
# print()
# for i_sec in range(7):
#     num = int(input(f'Введите {i_sec + 1}-е число для 2-го списка: '))
#     second_list.append(num)
#
# print('Первый список: ', first_list, '\nВторой список:', second_list)
#
# first_list.extend(second_list)
#
# i_num = 0
#
# while i_num < len(first_list) - 1:
#     while first_list.count(first_list[i_num]) > 1:
#         first_list.remove(first_list[i_num])
#     i_num += 1
#
# print('Новый первый список с уникальными элементами: ', first_list)
# 7 ==========================================================================
'''Задача 7. Ролики
Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики 
любого размера, которые не меньше размера его ноги. 
Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей. 
Реализуйте код, который определяет, какое наибольшее число человек сможет одновременно 
взять ролики и пойти покататься. 

Пример:
Кол-во коньков: 4
Размер 1 пары: 41
Размер 2 пары: 40
Размер 3 пары: 39
Размер 4 пары: 42

Кол-во людей: 3
Размер ноги 1 человека: 42
Размер ноги 2 человека: 41
Размер ноги 3 человека: 42

Наибольшее кол-во людей, которые могут взять ролики: 2
'''
# skate_sizes_list = []
# leg_sizes_list = []
# count = 0

# N = int(input('Кол-во коньков: '))
# for i_pair in range(N):
#     print('Размер', i_pair + 1, 'пары: ', end='')
#     pair = int(input())
#     skate_sizes_list.append(pair)

# K = int(input('\nКол-во людей: '))
# for i_leg in range(K):
#     print('Размер ноги', i_leg + 1, 'человека: ', end='')
#     leg = int(input())
#     leg_sizes_list.append(leg)

# print(skate_sizes_list)
# print(leg_sizes_list)
#
# for leg_size in leg_sizes_list:
#     for pair_size in skate_sizes_list:
#         if leg_size == pair_size:
#             skate_sizes_list.remove(pair_size)
#             count += 1
#             break
#         elif pair_size > leg_size:
#             skate_sizes_list.remove(pair_size)
#             count += 1
#             break
#
# print(skate_sizes_list)
# print(leg_sizes_list)

# print('Наибольшее кол-во людей, которые могут взять ролики: ', count)
# 8 ==========================================================================
'''Задача 8. Считалка
N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку 
на выбывание, где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается 
со следующего за ним человека.
На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число 
от 1 до N — это номер человека, который останется в кругу последним.

Пример:
Кол-во человек: 5
Какое число в считалке? 7
Значит, выбывает каждый 7 человек

Текущий круг людей: [1, 2, 3, 4, 5]
Начало счёта с номера 1
Выбывает человек под номером 2

Текущий круг людей: [1, 3, 4, 5]
Начало счёта с номера 3
Выбывает человек под номером 5

Текущий круг людей: [1, 3, 4]
Начало счёта с номера 1
Выбывает человек под номером 1

Текущий круг людей: [3, 4]
Начало счёта с номера 3
Выбывает человек под номером 3

Остался человек под номером 4
'''
# Вариант № 1 (Мой)

# N = int(input('Кол-во человек: '))
# K = int(input('Какое число в считалке? '))
# print(f'Значит, выбывает каждый {K} человек')
#
# people_list = list(range(1, N + 1))
#
# index = 0
# count = 1
# while len(people_list) > 1:
#     print('\nТекущий круг людей: ', people_list)
#     print('Начало счёта с номера', people_list[index])
#     while count < 7:
#         if index == len(people_list) - 1:
#             index = 0
#             count += 1
#         else:
#             index += 1
#             count += 1
#     else:
#         if index == len(people_list) - 1:
#             print('Выбывает человек под номером', people_list[index])
#             people_list.remove(people_list[index])
#             count = 1
#             index = 0
#         else:
#             print('Выбывает человек под номером', people_list[index])
#             people_list.remove(people_list[index])
#             count = 1
# print('\nОстался человек под номером ', people_list[0])

# Вариант № 2 (Нашел в инете, но не понял решения)

# N = int(input('Кол-во человек: '))
# K = int(input('Какое число в считалке?: '))
# print('Значит, выбывает каждый', K, 'человек')
#
# people_list = list(range(1, N + 1))
#
# count = 0
# while len(people_list) > 1:
#     print('Текущий круг людей: ', people_list)
#     print('Начало счёта с номера:', people_list[count])
#     count = (count + K - 1) % len(people_list)
#     if people_list[count] == people_list[-1]:
#         print('Выбывает человек под номером:', people_list.pop(count))
#         count = 0
#     else:
#         print('Выбывает человек под номером:', people_list.pop(count))
#
# print('Остался человек под номером:', people_list[0])
# 9 ==========================================================================
'''Задача 9. Друзья

N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, 
кто кому и сколько должен, и они придумали систему долговых расписок. И чтобы начать новый 
год «с чистого листа», друзья решили оплатить все долговые расписки, которые накопились у 
них друг к другу. Однако выяснилось, что иногда один и тот же человек в разные дни выступал 
как в роли должника, так и в роли кредитора.
Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый 
друг выплатить другим (или получить с других).
Сначала вводится число N — количество друзей, затем вводится число K — количество долговых 
расписок, после этого следует K троек чисел: номер друга, взявшего в долг, номер друга, 
давшего деньги, и сумма. Гарантируется, что ни один друг не брал в долг сам у себя.
Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или 
отдать друзья. Положительное число означает, что друг должен получить деньги от других, 
отрицательное — должен отдать деньги.

Пример 1:
Кол-во друзей: 2
Долговых расписок: 3

1 расписка
Кому: 1
От кого: 2
Сколько: 10 

1 расписка
Кому: 1
От кого: 2
Сколько: 20

1 расписка
Кому: 1
От кого: 2
Сколько: 20

Баланс друзей:
1 : 50
2 : -50

Пример 2:
Кол-во друзей: 3
Долговых расписок: 1

1 расписка
Кому: 3
От кого: 1
Сколько: 100

Баланс друзей:
1 : 100
2 : 0
3 : -100

'''
# debt = []
#
# N = int(input('Кол-во друзей: '))
# K = int(input('Долговых расписок: '))
#
# for _ in range(N):
#     debt.append(0)
#
# for i_voucher in range(K):
#     print()
#     print(i_voucher + 1, 'расписка')
#     whom = int(input('Кому: '))             # Кому
#     from_whom = int(input('От кого: '))     # От кого
#     how_much = int(input('Сколько: '))      # Сколько
#     debt[whom - 1] += how_much
#     debt[from_whom - 1] -= how_much
#
# print('Баланс друзей:')
# for i_friends in range(len(debt)):
#     print(i_friends + 1, ':', -debt[i_friends])
# 10 ==========================================================================
'''Задача 10. Симметричная последовательность
Последовательность чисел называется симметричной, если она одинаково читается как слева 
направо, так и справа налево. Например, следующие последовательности являются симметричными:
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет, 
какое минимальное количество и каких чисел надо приписать в конец этой последовательности, 
чтобы она стала симметричной.

Пример 1:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 1
Число: 2
Число: 2

Последовательность: 1 2 1 2 2
Нужно приписать чисел: 3
Сами числа: 1 2 1	

Пример 2:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 3
Число: 4
Число: 5

Последовательность: 1 2 3 4 5
Нужно приписать чисел: 4
Сами числа: 4 3 2 1
'''
def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [3, 4, 3]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Исходный список: ', nums)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа: ', answer)

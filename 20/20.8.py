# Home Work
# 1 ==========================================================================
'''Задача 1. Ревью кода
Ваня работает middle-разработчиком на Python в IT-компании. Один кандидат на junior-разработчика
прислал ему код тестового задания. Задание состояло в следующем: есть словарь из трёх студентов.
Необходимо:
1.	Вывести на экран список пар «ID студента — возраст».
2.	Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения:
полный список интересов всех студентов и общую длину всех фамилий студентов.
3.	Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся
на экран.
Ваня — очень придирчивый программист, и после просмотра кода он понял, что этого кандидата на работу
не возьмёт, даже несмотря на то, что он выдаёт верный результат. Вот сам код кандидата:
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться (ну
только если очень захочется). Убедитесь в том, что программа работает всё так же верно. Различные
проверки на существование записей в словаре не обязательны, но приветствуются :)
'''
# def f(dict):
#     lst = [j_list for _, i_dict in dict.items() for j_keys, j_list in i_dict.items() if j_keys == 'interests']
#     lst = [j_elem for i_list in lst for j_elem in i_list]
#     length = [len(j_surname) for _, i_dict in dict.items() for j_keys, j_surname in i_dict.items() if j_keys == 'surname']
#     return lst, sum(length)
#
#
# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
# pairs = []
# for i_ID, i_dict in students.items():
#     pairs += [i_ID, i_dict['age']]    # pairs.extend([i, students['age']])
# print('Cписок пар:', pairs)
#
# print(f(students))
# 2 ==========================================================================
'''Задача 2. Универсальная программа 2
Спустя некоторое время заказчик попросил нас немного изменить скрипт для своей криптографии: теперь 
индексы элементов должны быть простыми числами.
Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, 
словаря), у которых индекс — это простое число. Для проверки на простое число напишите отдельную функцию is_prime.
Дополнительно: сделайте так, чтобы основная функция состояла только из оператора return и при этом также 
возвращала список.
'''
# Пропустил
# 3 ==========================================================================
'''Задача 3. Функция
Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент (его можно вводить с 
клавиатуры). Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём 
и заканчивающийся вторым его появлением включительно. 
Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть 
кортеж, который начинается с него и идёт до конца исходного.
'''
# Пропустил
# 4 ==========================================================================
'''Задача 4. Игроки
У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «Ф. И. — очки»:
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
Один программист попросил нас для своей базы отправить ему немного другой вариант хранения этой информации.
Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран. 
Постарайтесь использовать как можно более эффективное решение.
Результат работы программы:
[('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]
'''
# Пропустил
# 5 ==========================================================================
'''Задача 5. Одна семья
В одной базе данных хранится информация о членах нескольких разных семей. Хранение реализовано с помощью 
словаря с парами «Ф. И. — возраст».
Напишите программу, которая запрашивает у пользователя фамилию и выводит на экран возраст всех членов одной 
семьи. Учтите, что, например, у двух людей разного пола фамилии различаются окончаниями. Поиск не должен быть 
регистрозависимым.
Пример:
Введите фамилию: Сидоров

Сидоров Никита 35
Сидорова Алина 34
Сидоров Павел 10
Действие «Поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией 
и их номера телефонов. Поиск не должен зависеть от регистра символов.
'''
# data_family = {
#     ('Сидоров', 'Никита'): 35,
#     ('Сидорова', 'Алина'): 34,
#     ('Сидоров', 'Павел'): 10,
#     ('Валитов', 'Эль'): 34,
#     ('Валитова', 'Гуля'): 25,
#     ('Валитова', 'Сылу'): 2,
#     ('Ибрагимов', 'Виталий'): 50,
#     ('Ибрагимова', 'Лена'): 45,
#     ('Ибрагимова', 'Вика'): 22
# }
#
# surname = input('Введите фамилию: ').lower()
#
# for (i_surname, i_name), i_age in data_family.items():
#     if surname[:-1] in i_surname.lower():
#         print(i_surname, i_name, i_age)
# 6 ==========================================================================
'''Задача 6. По парам
Есть список из 10 случайных чисел. Напишите программу, которая делит эти числа на пары кортежей внутри списка, 
и выведите результат на экран.
Дополнительно: решите задачу несколькими способами.
Пример:
Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
'''
# from random import randint
#
# random_lst = [randint(0, 10) for _ in range(10)]
# print('Оригинальный список: ', random_lst)
#
# # Вар 1
# new_lst = []
# while random_lst:
#     temp_lst = [i_elem for i_elem in random_lst[:2]]
#     new_lst.append(tuple(temp_lst))
#     random_lst[:2] = []
# print(new_lst)
#
# # Вар 2
# for _ in random_lst:
#     temp_lst = [i_elem for i_elem in random_lst[:2]]
#     random_lst[:2] = []
#     random_lst.append(tuple(temp_lst))
# print(random_lst)
#
# # Вар 3
# random_lst = list(zip(random_lst[0::2], random_lst[1::2]))
# print('Новый список: ', random_lst)
# 7 ==========================================================================
'''Задача 7. Функция сортировки
Напишите функцию, которая сортирует кортеж, состоящий из целых чисел, по возрастанию и возвращает его. 
Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
'''
# Пропустил
# 8 ==========================================================================
'''Задача 8. Контакты 3
Мы уже помогали Степану с реализацией телефонной книги (контактов) на телефоне, однако внезапно оказалось, 
что книге не хватает ещё одной очень полезной функции: поиска!
Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить: 
добавить контакт или найти человека в списке контактов по фамилии. 
Действие «Добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона, добавляет 
их в словарь и выводит на экран текущий словарь контактов. Если этот человек уже есть в словаре, то выведите 
соответствующее сообщение.
'''
# contacts_dict = dict()
#
# while True:
#     flag = False
#     action = input('Выберите действие: \nadd - добавить контакт;\nsearch - найти человека в телефонной книге по фамилии; \nq - выйти: ')
#     if action == 'add':
#         name_surname = tuple(input('Введите имя и фамилию ч/з пробел: ').lower().split())
#         number = int(input('Введите номер телефона: '))
#         if name_surname not in contacts_dict:
#             contacts_dict[name_surname] = number
#             print('\nТелефонная книга:')
#             for (i_name, i_surname), i_number in contacts_dict.items():
#                 print('\t', i_name, i_surname, ':', i_number, end='\n\n')
#         else:
#             print('\nТакой контакт уже есть в телефонной книге!')
#     elif action == 'search':
#         if contacts_dict:
#             surname_cont = input('Введите фамилию контакта который хотите найти: ').lower()
#             for (i_name, i_surname), i_number in contacts_dict.items():
#                 if i_surname == surname_cont:
#                     print('Такой контакт есть:', i_name, i_surname, ':', i_number, end='\n\n')
#                     flag = True
#             if not flag:
#                 print('Такого контакта нет!', end='\n\n')
#         else:
#             print('Телефонная книга пока пуста!')
#     elif action == 'quit' or action == 'q':
#         break
#     else:
#         print('Несуществующая команда! Начните заново.', end='\n\n')
#
# if contacts_dict:
#     print('\nТелефонная книга:')
#     for name_surname, number in contacts_dict.items():
#         print('\t', name_surname[0], name_surname[1], ':', number)
# else:
#     print('Телефонная книга пока пуста!')
# 9 ==========================================================================
'''Задача 9. Протокол соревнований
Вы продолжаете развиваться в геймдеве, и в этот раз вам пришло действительно внушительное техническое задание, 
с описанием правил игр, входными и выходными данными. Вот как оно выглядит:
Здравствуйте! Мы собираемся устраивать соревнования по [данные засекречены] и хотим, чтобы вы написали 
эффективную программу, которая составляла бы нам протокол и определяла победителя и призёров. О логике 
работы программы ниже.
Правила соревнований:
1.	Участники имеют право играть несколько раз. Количество попыток одного участника не ограничивается. 
2.	Окончательный результат участника определяется по одной игре, лучшей для этого участника.
3.	Более высокое место в соревнованиях занимает участник, показавший лучший результат.
4.	При равенстве результатов более высокое место занимает участник, раньше показавший лучший результат.
Как проходят соревнования:
В ходе соревнований заполняется протокол, каждая строка которого описывает одну игру и содержит результат 
участника и его игровое имя. Протокол формируется в реальном времени по ходу проведения чемпионата, поэтому 
строки в нём расположены в порядке проведения игр: чем раньше встречается строка в протоколе, тем раньше 
закончилась соответствующая этой строке игра.
Напишите программу, которая по данным протокола определяет победителя и призёров. Гарантируется, что в 
чемпионате участвует не менее трёх игроков.

Описание входных данных
Первая строка содержит число N — это общее количество строк протокола. Каждая из следующих N строк содержит 
записанные через пробел результат участника (целое неотрицательное число) и игровое имя (имя не может содержать 
пробелов). Строки исходных данных соответствуют строкам протокола и расположены в том же порядке, что и в протоколе.
Описание выходных данных
Программа должна вывести имена и результаты трёх лучших игроков по форме, приведённой ниже в примере.

Пример входных и выходных данных:
Сколько записей вносится в протокол? 9
Записи (результат и имя):
1 запись: 69485 Jack 
2 запись: 95715 qwerty 
3 запись: 95715 Alex 
4 запись: 83647 M
5 запись: 197128 qwerty 
6 запись: 95715 Jack 
7 запись: 93289 Alex 
8 запись: 95715 Alex 
9 запись: 95715 M

Итоги соревнований:
1 место. qwerty (197128)
2 место. Alex (95715)
3 место. Jack (95715)
'''
# results = {}
#
# # заполняем словарь только лучшими результатами игроков
# N = int(input('Сколько записей вносится в протокол? '))
# print('Записи (результат и имя):')
# for i_log in range(N):
#     log = input(f'{i_log+1} запись: ').split()
#     if log[1] not in results:
#         results[log[1]] = [int(log[0]), i_log+1]
#     else:
#         if int(log[0]) > results[log[1]][0]:    # Если рез-ат лучше, то заменяем его в словаре
#             results[log[1]] = [int(log[0]), i_log+1]
#
# # На основе полученного выше словаря results формируем список из вложенных списков,
# # каждый из кот. содержит лучший результат каждого игрока
# result_list = [[i_name, i_score, i_log] for i_name, [i_score, i_log] in results.items()]
#
# # Сортировка списка result_list по правилу 3-4 соревнований.
# for i_index in range(len(result_list) - 1):
#     if result_list[i_index][1] < result_list[i_index + 1][1]:
#         result_list.insert(i_index, result_list.pop(i_index + 1))
#     else:
#         if result_list[i_index][1] == result_list[i_index + 1][1]:
#             if result_list[i_index][2] > result_list[i_index + 1][2]:
#                 result_list.insert(i_index, result_list.pop(i_index + 1))
#
# # Вывод результатов трёх лучших игроков
# print('\nИтоги соревнований:')
# for i_place in range(3):
#     print(f'{i_place+1} место: {result_list[i_place][0]} ({result_list[i_place][1]})')
# 10 ==========================================================================
'''Задача 10. Своя функция zip (необязательная)
В самом конце собеседования вас неожиданно спросили: «Расскажите, что делает функция zip?». В итоге, 
чтобы произвести максимальное впечатление, вы решили не только рассказать про неё, но и написать её аналог.
Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число». 
Затем выведите на экран сам генератор и кортежи.

Пример:
Строка: abcd
Кортеж чисел: (10, 20, 30, 40)

Результат:
<generator object <genexpr> at 0x00000204A4234048>
('a', 10)
('b', 20)
('c', 30)
('d', 40)

Дополнительно: создайте полный аналог функции zip, то есть сделайте так, чтобы программа работала с любыми 
итерируемыми типами данных.
'''
# # Этап 1 ======================================

# syms_str = 'abc'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = [(syms_str[i_elem], nums_tpl[i_elem])
#          for i_elem in range(len(syms_str))]
# print(pairs)

# # Этап 2 ======================================
#
# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = [(syms_str[i_elem], nums_tpl[i_elem])
#          for i_elem in range(shortest_seq_range(syms_str, nums_tpl))]
# print(pairs)

# Этап 3 ======================================

def shortest_seq_range(string, tpl):
    return min(len(string), len(tpl))


syms_str = 'abcd'
nums_tpl = (10, 20, 30, 40)

pairs = ((syms_str[i_elem], nums_tpl[i_elem])
         for i_elem in range(shortest_seq_range(syms_str, nums_tpl)))
print(pairs)
for i_elem in pairs:
    print(i_elem)

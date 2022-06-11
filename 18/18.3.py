'''Работа за преподавателем'''
# Task 1

# words_list = []
# while True:
#     word = input('Введите слово: ')
#     if word != 'end':
#         words_list.append(word)
#     else:
#         break
#
# print(words_list)

# Task 2

# text = input('Содержимое файла: ')
# words_list = text.split()
#
# print(words_list)

# Task 3

# text = input('Содержимое файла: ')
# words_list = text.split()
#
# print(words_list)
#
# new_text = ''
# for word in words_list:
#     new_text += '---' + word
#
# print(new_text[3:])

# Task 4

# text = input('Содержимое файла: ')
# words_list = text.split()
#
# print(words_list)
#
# new_text = '---'.join(words_list)
#
# print(new_text)

# Task 5

# str_1 = 'I love'
# str_2 = 'Python!'
#
# print(str_1 + str_2)
# #------------------------
# str_1 = 'I love'
# str_2 = 'Python!'
#
# print(''.join([str_1, str_2]))

# Task 6

# while True:
#     grats_template = input('Введите шаблон поздравления, '              # Шаблон поздравлений
#                            'в шаблоне нужно использовать конструкцию '
#                            '{name} и {age}:\n')
#     if '{name}' in grats_template and '{age}' in grats_template:
#         break
#     print('Ошибка: отсутствует одна или две конструкции!')
#
# names_list = input('Список людей через запятую: ').split(', ')
# # Вариант №1 =====================================================
# ages_str = input('Возраст людей через пробел: ')
# ages = [int(i_number) for i_number in ages_str.split()]
#
# for i_man in range(len(names_list)):
#     print(grats_template.format(name=names_list[i_man], age=ages[i_man]))
#
# people = [
#     ' '.join([names_list[i_man], str(ages[i_man])])
#     for i_man in range(len(names_list))
# ]
#
# people_str = ', '.join(people)
# print('\nИменинники: ', people_str)
# Вариант №2 =====================================================
# ages = input('Возраст людей через пробел: ').split()
#
# for i_man in range(len(names_list)):
#     print(grats_template.format(name=names_list[i_man], age=ages[i_man]))
#
# people = [
#     ' '.join([names_list[i_man], ages[i_man]])
#     for i_man in range(len(names_list))
# ]
#
# people_str = ', '.join(people)
# print('\nИменинники: ', people_str)

# С др {name}! С {age}-летием тебя!   Катя, Гена, Гуля, Вася    10 20 30 40
# Home Work
# 1 ==========================================================================
'''Задача 1. Улучшенная лингвистика 2
Усовершенствуйте старую программу:  
У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст 
произведения, который вводится уже в одну строку. Напишите программу, которая посчитает, 
сколько раз слова пользователя встречаются в тексте. 
'''
# user_list = [input(f'Введите {i + 1}-е слово: ') for i in range(3)]
# text = input('Введите текст: ')
# # text = 'я хочу купить машину, потому что я люблю машину'
# text = ''.join(text.split(','))     # Убираю запятые из текста
#
# answer = [
#     ': '.join([i_word, str(text.count(i_word))])
#     for i_word in user_list
# ]
# for i_elem in answer:
#     print('Слово', i_elem, 'раза.')
# 2 ==========================================================================
'''Задача 2. Бабушка
У одной бабушки, когда та переписывается с внуком, постоянно залипает кнопка пробела. 
В итоге между словами получаются огромные расстояния. Внук не знает как это поправить 
в самом телефоне, поэтому обратился к вам за помощью.
Пользователь вводит строку. Напишите программу, которая преобразовывает в этой строке 
все идущие подряд пробелы в один и выводит результат на экран.
Пример:
Введите текст: У       нас         пошёл                    снег    !     

Исправленный текст: У нас пошёл снег !
'''
# text = input('Введите текст: ')
# text = ' '.join(text.split())
# print('Исправленный текст: ', text)
# 3 ==========================================================================
'''Задача 3. Разделители символов
Человек хочет сделать рассылку поздравлений для определённого списка людей. Поздравления 
для разных людей он хочет написать по-разному. 
Напишите программу, которая запрашивает у пользователя: 
Шаблон поздравления (туда вставляется ФИ и возраст)
ФИ людей (в одну строку, разделяются запятой)
Возраст каждого человека (в одну строку через пробел)
В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.
Пример:
Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: 
С днём рождения, {name}! С {age}-летием тебя!
Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
Возраст людей через пробел: 20 30 18

С днём рождения, Иван Иванов! С 20-летием тебя!
С днём рождения, Петя Петров! С 30-летием тебя!
С днём рождения, Лена Ленова! С 18-летием тебя!

Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18
'''
while True:
    grats_template = input('Введите шаблон поздравления, шаблон должен '
                           'содержать конструкции {name} и {age}: \n')
    if '{name}' in grats_template and '{age}' in grats_template:
        break
    print('Ошибка: В шаблоне поздравления нет конструкции {name} или {age}!')

name_list = input('Список людей через запятую: ').split(',')
age_list = input('Возраст людей через пробел: ').split()

for i_grats in range(len(name_list)):
    print(grats_template.format(
        name=name_list[i_grats],
        age=age_list[i_grats])
    )

people = [
    ' '.join([name_list[i_num], age_list[i_num]])
    for i_num in range(len(name_list))
]

people = ', '.join(people)
print('Именинники: ', people)

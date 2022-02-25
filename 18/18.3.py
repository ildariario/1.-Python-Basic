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
# text = input('Введите текст: ')
# text = ' '.join(text.split())
# print('Исправленный текст: ', text)
# 3 ==========================================================================
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
# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================

# 7 ==========================================================================

# 8 ==========================================================================

# 9 ==========================================================================

# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================

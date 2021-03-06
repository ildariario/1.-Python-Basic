# Home Work
# 1 ==========================================================================
'''Задача 1. Календарь
Мы продолжаем разрабатывать удобный календарь для смартфона. Функцию определения
високосного года мы добавили, но забыли ещё много разных очевидных вещей.
Напишите программу, которая принимает от пользователя день недели в виде строки и
выводит его номер на экран.
Пример:
Введите день недели: вторник
Номер дня недели: 2
'''
# Пропустил
# 2 ==========================================================================
'''Задача 2. Я стал новым пиратом!
Старому капитану необходимо пополнить команду. Но попадут на его корабль только достойные! Он отобрал 10 человек и те, кто из них крикнет слово “Карамба”, попадут на борт.
Пользователь вводит 10 слов. Напишите программу, которая определяет, сколько из них совпадают со словом “Карамба”.
'''
# Пропустил
# 3 ==========================================================================
'''Задача 3. Кривой мессенджер
При передаче сообщений в одном мессенджере иногда возникают неполадки и в сообщение попадает 
лишний символ - звёздочка. Пользователям это изрядно надоело, и они начали просто уходить в 
другие мессенджеры. Хотя одному пользователю стало интересно, на каких обычно позициях 
появляется эта звёздочка.
 
Пользователь вводит строку, в которой встречается символ “*” ровно один раз. Напишите 
программу, которая определяет порядковый номер этого символа в строке.
Пример:
Введите текст: Пр*ивет как дела
Символ ‘*’ стоит на позиции 3
'''
# string = input('Введите текст: ')
# i = 0
# for sym in string:
#     i += 1
#     if sym == '*':
#         N = i
# print("Символ '*' стоит на позиции " , N)
# 4 ==========================================================================
'''Задача 4. Театр
Планируется построить театр под открытым небом, но для начала нужно хотя бы примерно 
понять сколько должно быть рядов, сидений в них и какое лучше сделать расстояние между рядами.
Напишите программу, которая получает на вход кол-во рядов, сидений и свободных метров 
между рядами, а затем выводит примерный макет театра на экран.

Введите количество рядов: 5
Введите количество сидений: 7
Введите количество метров между рядами: 3
Сцена
======= *** =======
======= *** =======
======= *** =======
======= *** =======
======= *** =======
'''
# a = int(input('Введите количество рядов: '))
# b = int(input('Введите количество сидений: '))
# c = int(input('Введите количество метров между рядами: '))
#
# print('\nСцена\n')
# for num in range(a):
#     print('=' * b, '*' * c, '=' * b)
# 5 ==========================================================================
'''Задача 5. Два столбца
Пользователь вводит число N. Напишите программу, которая выводит числа в два столбика: 
в первом чётные числа, во втором - нечётные.
Пример 1:
Введите число: 8
0 1
2 3
4 5
6 7
8
Пример 2:
Введите число: 5
0 1
2 3
4 5
'''
# N = int(input('Введите число N: '))
# for num in range(N+1):
#     if num == 0:
#         print(num, end = '  ')
#     elif num % 2 != 0:
#         print(num)
#     elif num % 2 == 0:
#         print(num, end = '  ')
# 6 ==========================================================================
'''Задача 6. Марсоход 2
К роботу Валли отправили ещё одного робота Билли. Это его первый поход на Марс, поэтому 
он тестируется в прямоугольном помещении размером 15 на 20 метров. Марсоход высаживается 
в центре комнаты (в точке 8, 10), после чего управление им передаётся оператору - 
пользователю вашей программы. Программа спрашивает в какую сторону оператор хочет направить 
робота: север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D). 
Оператор делает выбор, марсоход перемещается на 1 метр в эту сторону и программа сообщает 
новую позицию марсохода. Если марсоход упёрся в стену, то он не должен пытаться перемещаться 
в сторону стены, в этом случае его позиция не меняется.
Пример:
[Программа]: Марсоход находится на позиции 6, 19, введите команду:
[Оператор]: A
[Программа]: Марсоход находится на позиции 5, 19, введите команду:
[Оператор]: W
[Программа]: Марсоход находится на позиции 5, 20, введите команду:
[Оператор]: W
[Программа]: Марсоход находится на позиции 5, 20, введите команду:
'''
# x = 8
# y = 10
# while True:
#     go = input('Марсоход находится на позиции ' + str(x) + ', ' + str(y) + ' введите команду: ')
#     if go == 'a':
#         x -= 1
#     elif go == 'd':
#         x += 1
#     elif go == 'w':
#         y += 1
#     else:
#         y -= 1
#     if x == -1 or y == -1 or x == 16 or y == 21:
#         print('Марсоход уперся в стену, завершение программы ...')
#         break
# 7 ==========================================================================
'''Задача 7. Кривой мессенджер 2
Автору того самого мессенджера не очень нравится, что от него уходит аудитория. Поэтому 
он поторопился исправить это недоразумение. Правда, пока он думал, эти “звёдочки” стали 
появляться кучами.
Пользователь вводит строку, в которой символ “*” может встречаться сколько угодно раз. 
Напишите программу, которая удаляет символы “*” из строки.
Пример:
Введите текст: Пр*ив***ет
Исправленная строка: Привет
'''
# Пропустил
# 8 ==========================================================================
'''Задача 8. Анкета
При заполнении электронной анкеты фамилия и имя вводятся в одно поле через пробел. 
Напишите программу, которая делит строку на фамилию и имя и выводит их на экран.
Пример:
Введите ФИ: Петров Иван
Фамилия: Петров
Имя: Иван
'''
# text = input('Введите ФИ: ')
# name_surname = ''

# for sym in text:
#     name_surname += sym
#     if sym == ' ':
#         surname = name_surname
#         name_surname = ''
# name = name_surname

# print('Фамилия: ', surname)
# print('Имя: ', name)
# 9 ==========================================================================
'''Задача 9. Спецшифр
Два сотрудника спецслужб переписываются необычным шифром. Каждую букву они шифруют в 
виде строки, внутри которой есть длинная последовательность букв “s”, а длина самой 
длинной - это и есть номер буквы алфавита, которую хотят отправить.
Напишите программу, которая получает на вход строку, подсчитывает в ней самую длинную 
последовательность подряд идущих букв “s” и выводит ответ на экран.
Пример:
Введите строку: ssbbbsssbc
Самая длинная последовательность: 3
'''
# text = input('Введите текст: ')
# k = 1
# prev = ''
# maxx = 0

# for sym in text:
#     if sym == prev:
#         k += 1
#     else:
#         prev = sym
#         k = 1
#     if k > maxx:
#         maxx = k

# print('Самая длинная последовательность: ', maxx)
# 10 ==========================================================================
'''Задача 10. Великий и могучий
Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку. 
Особенно Паоло понравилась книга “Преступление и наказание”. И ему стало интересно, 
можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на 
своём языке.
Напишите программу, которая получает на вход текст и находит длину самого длинного 
слова в нём. Слова в тексте разделяются одним пробелом.
Пример:
Введите текст: Меня зовут Петр
Длина самого длинного слова: 5
'''
# text = input('Введите текст: ')
# text = text + ' '
# i = 0
# k = 0
# sym_word_1 = 0

# for sym in text:
#     i += 1
#     if sym == ' ':
#         k += 1
#         sym_word_2 = i - 1
#         print('Длина', k, '- го слова: ', sym_word_2)
#         if sym_word_2 < sym_word_1:
#             maxx = sym_word_1
#         else:
#             maxx = sym_word_2

#         i = 0

# print('Длина самого длинного слова: ', maxx)
# 11 ==========================================================================
'''Задача 11. Проверка слова
Напишите программу, которая проверяет, верно ли, что введенное слово начинается и 
заканчивается на одну и ту же букву и затем выводит соответствующее сообщение.
Пример:
Введите слово: буль
Первая и последняя буквы разные
Пример 2:
Введите слово: булб
Первая и последняя буквы одинаковые
'''
# num_sym = 0
# text = input('Введите слово: ')

# for sym in text:
#     num_sym += 1
#     if num_sym == 1:
#         first_sym = sym
#         print('Первая буква слова: ', first_sym)
# print('Последняя буква слова: ', sym)

# if first_sym == sym:
#     print('Первая и последняя буквы одинаковые')
# else:
#     print('Первая и последняя буквы разные')
# 12 ==========================================================================
'''Задача 12. Колонтитул
Нам нужно написать программу для печати важных объявлений. Сверху объявления должен 
располагаться вот такой колонтитул: ~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~
Восклицательные знаки всегда располагаются по центру строки, причём в зависимости от 
важности объявления количество восклицательных знаков может быть разным. Напишите 
программу, которая спрашивает у пользователя сначала общую длину колонтитула в символах, 
потом желаемое количество восклицательных знаков, после чего выводит на экран готовую строку.
'''
# footers = int(input('Введите общую длину колонтитула : '))         # footers - колонтитулы
# exclamation_point = int(input('Введите желаемое количество восклицательных знаков: '))       # exclamation_point - восклицательный знак
# a = int((footers - exclamation_point)/2)
#
# if footers > exclamation_point:
#     print('~' * a, end='')
#     print('!' * exclamation_point, end='')
#     print('~' * a)
# else:
#     print('Общая длина колонтитула не может быть меньше количества восклицательных знаков!')
# 13 ==========================================================================
'''Задача 13. Коровы
Для коров есть 10 стойл. В каждом стойле разные условия для животных, поэтому и молока они дают по-разному. 
В первом стойле производят 2 литра в день, во втором 4, в третьем - 6, потом 8, 10, 12, 14, 16, 18, 20. 
Но коровы стоят не во всех стойлах. Свободные и занятые обозначаются строкой из букв a и b, 
где a - свободное стойло, b - занятое.
Пользователь вводит строку из 10 символов a и b. Необходимо определить, сколько в итоге будет 
произведено молока за день.
'''
# milk = 0
# total_milk = 0
# i = 0

# string = input('Введите текст: ')
# for symbol in string:
#     i += 1
#     milk += 2
#     if symbol == 'b':
#         total_milk += milk
#         print('В', i,'- ом стойле, произведено молока: ', milk)
#     else:
#         print('В', i,'- ом стойле, коров нет')
# print('В итоге за день произведено молока: ', total_milk)
# 14 ==========================================================================
'''Задача 14. Подсчёт слов
В любом хорошем текстовом редакторе можно посмотреть не только общее количество символов, но также и 
количество слов в документе.
Вводится строка, состоящая из слов, разделенных пробелами. Напишите программу, которая считает количество 
слов в этой строке.
'''
# word_num = 1
# sym_num = 0
# sym_2_num = 0

# string = input('Введите текст: ')
# for sym in string:
#     if sym == ' ':
#         word_num += 1
#     else:
#         sym_2_num += 1
#     sym_num += 1

# print('Количество слов: ', word_num)
# print('Количество символов (с пробелами): ', sym_num)
# print('Количество символов (без пробелов): ', sym_2_num)
# 15 ==========================================================================
'''Задача 15. Метод бутерброда (необязательная)
Секретное агентство «Super-Secret-no» решило для шифрования переписки своих сотрудников использовать 
«метод бутерброда». Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, 
последняя буква - номер 2, вторая – номер 3, предпоследняя – номер 4, потом третья … и так для всех букв 
(см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.
Например, слово «sandwich» зашифруется в «shacnidw».
К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился. И теперь 
агенты не могут понять, что же они написали друг другу. Помогите им.
Пример:
Введите зашифрованное сообщение: shacnidw
Расшифрованное сообщение: sandwich
'''
# Вар 1
# text = 'shacnidw'
# text = 'iolidra'
# i = 1
# j = 0
# N = 0
# k = 0
# word_1, word_2, word_3 = '', '', ''

# for sym in text:
#     if i % 2 != 0: 
#         word_1 += sym
#     elif i % 2 == 0:
#         word_2 += sym
#         N += 1
#     i += 1

# while j < N:
#     k = 0
#     for sym in word_2:
#         k += 1
#         if k == N - j:
#             word_3 += sym
#     j += 1

# print('Расшифрованное сообщение: ', word_1 + word_3, end = '')
# Вар 2
# print('==================================')
# text = 'shacnidw'
# text = 'iolidra'
# i = 1
# N = 0
# k = 0

# word_1, word_2, word_3 = '', '', ''

# for sym in text:
#     if i % 2 != 0: 
#         word_1 += sym
#     elif i % 2 == 0:
#         word_2 += sym
#         N += 1
#     i += 1

# for j in range(0, N):
#     k = 0
#     for sym in word_2:
#         k += 1
#         if k == N - j:
#             word_3 += sym

# print('Расшифрованное сообщение: ', word_1 + word_3, end = '')

# Вар 3

# text = 'shacnidw'
# # text = 'iolidra'
# i = 1
# N = 0
# k = 0
# a, b, c, d, e, f = '', '', '', '', '', ''
#
# word_1, word_2, word_3 = '', '', ''
#
# for sym in text:
#     if i % 2 != 0:
#         word_1 += sym
#     elif i % 2 == 0:
#         word_2 += sym
#         N += 1
#     i += 1
#
# for sym in word_2:
#     k += 1
#     if k == 1:
#         a = sym
#     elif k == 2:
#         b = sym
#     elif k == 3:
#         c = sym
#     elif k == 4:
#         d = sym
#     elif k == 5:
#         e = sym
#     elif k == 6:
#         f = sym
# word_2 = f + e + d + c + b + a
#
# print('Расшифрованное сообщение: ', word_1 + word_2, end='')

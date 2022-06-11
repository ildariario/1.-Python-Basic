'''Работа за преподавателем'''
# Task 1

# text = input('Введите текст: ')
# summ = 0

# print('\nОтфильтрованный текст: ', end = '')
# for symbol in text:
#     if symbol == '0' or symbol == '1' or symbol == '2' or symbol == '3' or symbol == '4' or symbol == '5' or symbol == '6' or symbol == '7' or symbol == '8' or symbol == '9':
#         summ += int(symbol)
#     else:
#         print(symbol, end = '')
# print('\nСумма: ', summ)

# Task 2

string = input('Введите текст: ')
prevSym = ''
equalSym = False

for letter in string:
    if prevSym == letter:
        equalSym = True
        break
    else:
        prevSym = letter
if equalSym:
    print('Есть две одинаковые буквы подряд.')
else:
    print('Нет двух одинаковых букв подряд.')

# Task 1



# Task 2



# Task 3



# Home Work
# 1 ==========================================================================
'''
#n = int(input('До скольки вывести таблицу умножения? '))
n = 10
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j != n:
            print(j, 'x', i, '=', i * j, end = '\t')
        else:
            print(j, 'x', i, '=', i * j, end = '\n')
    # print()

# 2 ==========================================================================
def request(action):
    if action == '+':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a, '+', b, '=' a + b)
    elif action == '-':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a, '-', b, '=' a - b)
    elif action == '*':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a, '*', b, '=' a * b)
    elif action == '/':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a, '/', b, '=' a / b)
    else:
        print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
        action = input('Выберите операцию: ')
        request(action)

action = input('Выберите операцию: ')
request(action)
'''
# 3 ==========================================================================
action = input('Выберите операцию: ')
sym = ''
n = int(input('Сколько операндов? '))

if action == '+':
    result = 0
    for i in range(1, n + 1):
        num = int(input('Введите операнд ' + str(i) + ': '))
        if i < n:
            sym += str(num) + ' ' + action + ' '
        else:
            sym += str(num)
        result += num
    print(sym, '=', result)
elif action == '-':
    result = 0
    for i in range(1, n + 1):
        num = int(input('Введите операнд ' + str(i) + ': '))
        if i < n:
            sym += str(num) + ' ' + action + ' '
        else:
            sym += str(num)
        result -= num
        if i == 1:
            result *= -1
    print(sym, '=', result)
elif action == '*':
    result = 1
    for i in range(1, n + 1):
        num = int(input('Введите операнд ' + str(i) + ': '))
        if i < n:
            sym += str(num) + ' ' + action + ' '
        else:
            sym += str(num)
        result *= num
    print(sym, '=', result)
elif action == '/':
    for i in range(1, n + 1):
        num = int(input('Введите операнд ' + str(i) + ': '))
        if i == 1:
            result = num
            sym += str(num) + ' ' + action + ' '
        else:
            if i < n:
                sym += str(num) + ' ' + action + ' '
            else:
                sym += str(num)
            result /= num
    print(sym, '=', result)
else:
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
    action = input('Выберите операцию: ')
    request(action)
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
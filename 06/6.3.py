# Home Work
# 1 ==========================================================================
'''
weather = int(input('Введите значение температуры на улице: '))
meters = 0
while weather > 15:
    meters += 20 # Бегун четь чуть пробежал вперед
    weather -= 2 # Похолодало на 2 градуса
    if weather <= 15: # Если температура уменьшится до 15 град., то еще 10 м. проходить не нужно
        break
    meters += 10 # Пробежал еще не много
print(f'Пройдено {meters} метров.')

# 2.1 ==========================================================================
number = int(input('Введите число: '))
summ = 0
while number != 0:
    last_num = number % 10
    print('Последняя чифра числа: ', last_num)
    if last_num == 5:
        print('Обнаружен разрыв!')
        break
    summ += last_num
    number //= 10
print(f'Сумма: {summ}')

# 2.2 ==========================================================================

number = int(input('Введите число: '))
summ = 0
while number != 0:
    last_num = number % 10
    print('Последняя чифра числа: ', last_num)
    if last_num != 5:
        summ += last_num
        number //= 10
    else:
        print('Обнаружен разрыв!')
        break 
print(f'Сумма: {summ}')

# 3 ==========================================================================
i = 0
summ = 0
stop = True
while stop:
    num = int(input('Введите число: '))
    if num > 0:
        i += 1
        summ += num
    else:
        stop = False
    # num = int(input('Введите число: '))
print(f'Количество введенных чисел = {i}, а их сумма = {summ}.')
'''
# 4 ==========================================================================
ballance = int(input('Введите стартовую сумму: '))

while ballance < 10000:
    num_kub = int(input('Сколько выпало на кубике? '))
    if (num_kub > 6) or (num_kub < 0):
        print('Введено недопустимое число! Попробуйте еще раз')
    else:
        if num_kub == 3:
            print('Вы проиграли все!')
            ballance = 0
            break
        else:
            print('Вы выиграли 500 рублей!')
            ballance += 500
print(f'Игра закончена.\nВаш баланс: {ballance} рублей.')

# 5 ==========================================================================

# 6 ==========================================================================

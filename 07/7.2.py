# In lesson - на уроке 
# 1 ==========================================================================
'''
for number in 0,1,2,3,4,5,6,7,8,9,10:
    print(number**2)
print()
for num in 2,7,5,3,10:
    print(num**2)

# 2 ==========================================================================
winners = 0
for ticket in 345, 19, 87, 1020, 421:
    if ticket % 5 == 0:
        print(ticket, '- счастливый билет!')
        winners += 1
print('Количество победителей -', winners)

# Home Work
# 1 ==========================================================================
for meters in 100,90,95,87,102:
    if meters % 3 == 1:
        print(meters, '- подходит')
    else:
        print(meters, '- не подходит')

# 2 ==========================================================================
for num in 3,7,5,6,4:
    print(f'{num}^2 = {num**2}, {num}^3 = {num**3}, {num}^4 = {num**4}')

# 3 ==========================================================================
win = 0
for ticket in 421,19,1020,345:
    if ticket % 5 == 0 and ticket > 99 and ticket < 1000:
        print(ticket, '- выигрышный билет!')
        win += 1
print('Количество выигрышных билетов:', win)
'''
# 4 ==========================================================================
for message in 0,1,2,3,4,5,6,7:
    print('Отмерили раз: ', message)
print('Отрезаем!')

# 5 ==========================================================================

# 6 ==========================================================================
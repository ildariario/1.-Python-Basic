# Home Work
# 1 ==========================================================================
i = 0
N_left = 1                         
N_right = 100  
while True:
    i += 1
    N_aver = (N_left + N_right) // 2
    print(f'Твое число равно, больше или меньше, чем {N_aver}?')
    answer = int(input('1 — равно, 2 — больше, 3 — меньше:'))
    if answer == 1:
        print(f'Я угадал с {i}-й попытки.')
        break
    elif answer == 2:
        N_left = N_aver + 1                 # 
    elif answer == 3:
        N_right = N_aver - 1               # 

# 2 ==========================================================================

# 3 ==========================================================================

# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================








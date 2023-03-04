# Задача 3. 
# Счастливым называется билет, в шестизначном номере которого 
# сумма первых трех цифр равна сумме последних трех цифр. 
# Напишите программу, проверяющую, "счастлив" ли билет. 

# I ВАРИАНТ: через while с последовательным суммированием последних и первых цифр

ticket_number = int(input('Пожалуйста, введите 6-значный номер билета => '))

if ticket_number < 100000 or ticket_number >= 1000000 : 
    print('ОШИБКА: Введенный вами номер билета не является 6-значным')
else: 
    rest_of_number = ticket_number
    balance = 0

    while rest_of_number > 999 : 
        last_digit = rest_of_number % 10
        balance += last_digit
        rest_of_number //= 10
    
    while rest_of_number > 0 : 
        last_digit = rest_of_number % 10
        balance -= last_digit
        rest_of_number //= 10

if balance == 0 : 
    print ('Вам повезло. Ваш билет является счастливым!')
else: 
    print ('К сожалению, ваш билет не счастливый (( ')   

# II ВАРИАНТ: ЧЕРЕЗ FOR c одновременным удалением 1-й и последней цифр

ticket_number = int(input('Пожалуйста, введите 6-значный номер билета => '))

if ticket_number < 100000 or ticket_number >= 1000000 : 
    print('ОШИБКА: Введенный вами номер билета не является 6-значным')
else: 
    rest_of_number = ticket_number
    balance = 0

# В цикле из 3-х шагов каждый раз к балансу прибавляем первую цифру и вычитаем последнюю, 
# после чего оставляем середину числа без 1-й и последней цифр (rest_of_number)

    for i in range(5,0,-2) : 
        balance = balance + rest_of_number // (10**i) - rest_of_number % 10
        rest_of_number = (rest_of_number % (10**i)) // 10

if balance == 0 : 
    print ('Вам повезло. Ваш билет является счастливым!')
else: 
    print ('К сожалению, ваш билет не счастливый (( ')   


# III ВАРИАНТ: СУММИРОВАНИЕ ПЕРВЫХ И ПОСЛЕДНИХ ЦИФР

ticket_number = int(input('Пожалуйста, введите 6-значный номер билета => '))

if ticket_number < 100000 or ticket_number >= 1000000 : 
    print('ОШИБКА: Введенный вами номер билета не является 6-значным')
else: 
    sum_of_first_digits = 0
    sum_of_last_digits = 0
    rest_of_number = ticket_number

    for i in range(1,4) : 
        sum_of_last_digits += rest_of_number % 10
        rest_of_number //= 10
    
    for i in range(1,4) : 
        sum_of_first_digits += rest_of_number % 10
        rest_of_number //= 10

print (f'Сумма первых трех цифр номера билета равна {sum_of_first_digits}, ')
print (f'Сумма первых трех цифр номера билета равна {sum_of_last_digits}. ') 

if sum_of_first_digits == sum_of_last_digits : 
    print ('Вам повезло. Ваш билет является счастливым!')
else: 
    print ('К сожалению, ваш билет не счастливый (( ')


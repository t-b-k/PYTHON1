# Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. 
# Если год является високосным, выведите YES, 
# иначе - выведите NO. 
# Год является високосным, если он делится на 4, но не делится на сто, либо если он кратен 400. 

year = int(input('Введите год => '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 : 
    print('YES')
else: 
    print('NO')
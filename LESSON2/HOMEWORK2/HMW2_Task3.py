# ДОМАШНЕЕ ЗАДАНИЕ 2. ЗАДАЧА 3. 

# Вывести все целые степени двойки, не превосходящие числа N 
# Ввод: 10
# Результат: 1 2 4 8 
# Без возведения в степень

# РЕШЕНИЕ: 

n = int(input("Введите натуральное число N => "))

production = 1 

if n > 0 : 
    print(f"\nВот вам все натуральные степени числа 2, не превосходящие {n}:")
    while production <= n : 
        print(production)
        production *= 2
else: 
    print(f"\nВы ввели ненатуральное число.")

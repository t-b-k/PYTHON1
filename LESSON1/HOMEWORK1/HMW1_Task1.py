# Задача 1: Найдите сумму цифр целого положительного числа

num = int(input('Введите целое положительное число => '))
sum_of_digits = num % 10

while num > 9 : 
    num = num // 10
    sum_of_digits = sum_of_digits + num % 10

print("Сумма цифр данного числа равна {}".format(sum_of_digits))

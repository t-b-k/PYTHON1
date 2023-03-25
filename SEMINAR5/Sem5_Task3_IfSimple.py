# Напишите программу, которая принимает на вход одно число 
# и определяет, является ли оно простым. 
# Простое - это число, которое имеет только 2 делителя: 
# 1 и само это число. 

n = int(input("Введите число, которое нужно проверить на простоту => "))

if n ==1 : 
    print("Единица не является простым числом")
elif n == 2: 
    print (f"Да, {n} - это простое число!")
elif n % 2 == 0: 
    print("Четное число не может быть простым")
else : 
    if_simple = True
    for i in range(3, int(n**0.5)+1, 2) :
        if n % i == 0 : 
            if_simple = False
            print(f"Число {n} не является простым!")
            break
    print (f"Да, {n} - это простое число!")
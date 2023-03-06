# ЗАДАЧА № 3

# Синоптиков интересует, сколько дней длилась самая длинная оттепель. 
# Оттепель - это период, в котором среднесуточная температура ежедневно превышает 0 градусов. 
# Пользователь вводит общее число анализируемых дней - N. 
# В последующих строках он вводит среднесуточные температуры для этих N дней. 
# Программа анализирует введенные данные и выдает в днях продолжительность самой длинной оттепели. 
# Значение температуры находится в промежутке от -50 до 50. 

# МОЕ РЕШЕНИЕ: 

# from random import randint 

# qty_of_days = int(input("Введите общее число анализируемых дней => "))

# print("\nПредположим, что среднесуточные температуры в этот период были следующие: ")

# day = 1
# max_period_length = 0
# temp = randint(-50, 50)
# print(temp)

# while day <= qty_of_days : 
#     period_length = 0  
#     while temp > 0 and day < qty_of_days: 
#         period_length += 1
#         day += 1
#         temp = randint(-50, 50)
#         print(temp)
#     else : 
#         if temp > 0 and day == qty_of_days : 
#             period_length += 1
#         elif temp <= 0 and  day < qty_of_days : 
#             temp = randint(-50, 50)
#             print(temp)
#         day += 1

#     if max_period_length < period_length : 
#         max_period_length = period_length

# print(f'Максимальная длина оттепели в заданном Вами периоде равняется {max_period_length} дню(дням)')

# РЕШЕНИЕ НА СЕМИНАРЕ: 

number = int(input("Введите длину анализируемого периода в днях: "))

period_length = 0
result = 0

for i in range(number) :
    temp = int(input('Введите температуру => '))
    if temp > 0 : 
        period_length += 1
    else : 
        if period_length > result : 
            result = period_length
        period_length = 0 

print(f'Длина самой продолжительной оттепели в заданном периоде равна {result} дня (дней)')


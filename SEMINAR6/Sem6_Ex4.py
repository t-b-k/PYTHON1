# Задача 4. 
# Два различных натуральных числа - n и m - называются дружественными, 
# если сума делителей числа n (включая 1, но исключая само n) равна
# числу m и наоборот. 
# По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, 
# не превосходящее 10 d 5-й степени. 
# Программа должна вывести все пары дружественных чисел, 
# каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара дложна быть выведена только один раз. 

# https://ru.stackoverflow.com/questions/1348243/

# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
from time import time

# start = time()

# user_num = int(input("Input a number: "))

def sum_dev (num) : 
    list_of_divs = [1]
    cou = 1
    for i in range(2, int(num/2)+2) :
        if num % i == 0:
            cou += i 
            list_of_divs.append(i)
    print(f"Делители числа {num}: {list_of_divs}")
    return cou

print(f"Сумма делителей числа 6232: {sum_dev(6232)}")
print(f"Сумма делителей числа 6368: {sum_dev(6368)}")
print(f"Сумма делителей числа 5020: {sum_dev(5020)}")
print(f"Сумма делителей числа 5564: {sum_dev(5564)}")
print(f"Сумма делителей числа 1184: {sum_dev(1184)}")
print(f"Сумма делителей числа 1210: {sum_dev(1210)}")
print(f"Сумма делителей числа 2620: {sum_dev(2620)}")
print(f"Сумма делителей числа 2924: {sum_dev(2924)}")

# print(sum_dev(220))

# for first in range(10, user_num) : 
#     second = sum_dev(first)
#     if_first = sum_dev(second)
#     if if_first == first and first <= second: 
#         print(first, second)

# print(f"RESULT: {time()-start} мс")
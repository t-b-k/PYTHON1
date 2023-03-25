# Задача 18. 
# В массиве A[1..N] требуется найти минимальный элемент, 
# из самых близких по величине к заданному числу x. 
# Пользователь в первой строке вводит натуральное N, 
# в последующих строках - N целых чисел, 
# в последней - число x.
# можно подключить random и формироватьм массив случайных чисел

# РЕШЕНИЕ: 
# Организуем числа, введенные пользователем, в список целых чисел, 
# отсортируем этот список в порядке возрастания
# Создадим параллельный список, который будет содержать на соответствующих 
# позициях абсолютную разность между элементами исходного списка и 
# заданным пользователем числом x. 
# Определим индекс минимального элемента в этом вспомогательном списке 
# (поскольку метод index возвращает индекс первого вхождения, в качестве
# результата мы получим как раз индекс минимального элемента исходного массива)
# Ответ - элемент исходного массива с индексом min_i.

import math

n = int(input("Введите кол-во элементов в массиве => "))

print("Теперь по одному вводите элементы массива: ")

array = [int(input(f"{i+1}-й    : ")) for i in range(n)]
sorted_array = sorted(array)

print(f"Вот массив, который Вы ввели: ")
print(array)

array.sort()
print(f"Для удобства отсортируем его по возрастанию: ")
print(array)

x = int(input("Введите теперь число X, ближайший элемент к которому мы будем искать: "))

# Создадим список, содержащий абсолютные разности |array[i]-X|

aux_array = [abs(array[i]-x) for i in range(len(array))]
min_diff = min(aux_array)
# min_diff = min([abs(array[i]-x) for i in range(len(array))])
print(f"Минимальное расстояние от элементов вашего массива до {x} равно {min_diff}")

# Определим индекс первого вхождения минимального элемента в этот массив: 

min_i = aux_array.index(min([abs(array[i]-x) for i in range(len(array))]))

print('\nРЕЗУЛЬТАТ: ')
print("В заданном Вами массиве наименьшим из элементов, отстоящих")
print(f"от числа {x} на минимальное расстояние, равное {aux_array[min_i]}, является число {array[min_i]}\n")

# РЕШЕНИЕ С ИСПОЛЬЗОВАНИЕМ ФУНКЦИИ LAMBDA (разобрано на семинаре): 
# Данный код возвращает не минимальный, а самый левый элемент!!! 

from random import randint

n = int(input())
list_nums = [randint(1,50) for _ in range(n)]

print(list_nums)

b = int(input())
m = min(list_nums, key = lambda x: abs(x - b))

print(m)
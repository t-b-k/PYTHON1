# Задача 32. 
# Определите индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)

from random import randint

n = int(input("Введите длину массива: "))
array_of_int = [randint(-100, 100) for _ in range (n)]
print("\nСлучайным образом сформировали массив: ")
print(array_of_int)

min_mean = randint(-100, 99)
max_mean = randint(min_mean+1, 100)

print(f"Посмотрим, элементы с какими индексами находятся в диапазоне [{min_mean}:{max_mean}]")
print("\nРЕЗУЛЬТАТ: к заданному диапазону принадлежат элементы с индексами:")
list_of_ind = [i for i in range(n) if array_of_int[i] in range(min_mean, max_mean+1)]
print(*list_of_ind)

# Реализовано на семинаре: 

# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])

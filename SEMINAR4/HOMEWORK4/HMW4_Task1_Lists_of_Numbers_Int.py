# Задача 1. 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все числа, которые встречаются 
# в обоих наборах. 
# Пользователь вводит 2 числа: N - кол-во чисел в 1-м наборе и M - количество 
# чисел во втором набора. Затем он вводит сами элементы множеств.

# РЕШЕНИЕ:  

n = int(input("Введите кол-во элементов в 1-м наборе => "))
m = int(input("Введите кол-во элементов во 2-м наборе => "))
print()
print("Введите элементы 1-го набора: ")
set1 = {int(input(f"Введите {i}-й элемент 1-го множества: ")) for i in range(1, n+1)}
#print(f"Первый набор содержит числа: {set1}")
print()
set2 = {int(input(f"Введите {i}-й элемент 2-го множества: ")) for i in range(1, m+1)}
#print(f"Второй набор содержит числа: {set2}")

print("\nА вот их пересечение, упорядоченное по возрастанию:")
print(*sorted(set1.intersection(set2)))

# II вариант: каждый набор чисел вводится в строку через пробел. 

set1 = set(input("Введите первый набор чисел (через пробел) => ").split())
set2 = set(input("Введите второй набор чисел (через пробел) => ").split())

result = sorted([int(i) for i in set1.intersection(set2)])

print("Вот значения, входящие в оба набора, отсортированные по возрастанию:")
print(*result)

# III вариант. Разобрано на семинаре. Позволяет вводить все значения в строку, 
# разделяя пробелами: 

# n, m = input("Введите в строку через пробел длины n и m двух наборов чисел => ").split() 
# print("Введите 1-й набор чисел в строку через пробел: ")
# first = [int(i) for i in input().split()] 
# print("\nВведите 2-й набор чисел в строку через пробел: ")
# second = [int(i) for i in input().split()]
# При таком способе ввода нам n и m, по сути, не нужны. 
# print('\nРЕЗУЛЬТАТ: упорядоченное пересечение введенных наборов чисел: ')
# print(*sorted(set(first).intersection(set(second))))
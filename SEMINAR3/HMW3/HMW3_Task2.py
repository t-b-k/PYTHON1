# Задача 18. 
# В массиве A[1..N] требуется найти минимальный элемент, 
# из самых близких по величине к заданному числу x. 
# Пользователь в первой строке вводит натуральное N, 
# в последующих строках - N целых чисел, 
# в последней - число x.
# можно подключить random и формироватьм массив случайных чисел

# РЕШЕНИЕ: 
import math

n = int(input("Введите кол-во элементов в массиве => "))

print("Теперь по одному вводите элементы массива: ")

array = [int(input(f"{i+1}-й    : ")) for i in range(n)]

print(f"Вот массив, который Вы ввели: ")
print(array)

x = int(input("Введите теперь число X, ближайший элемент к которому мы будем искать: "))

result_array = [abs(array[i]-x) for i in range(n)].sort()

for i in range(n) : 


print([abs(array[i]-x) for i in range(n)].sort()[0])

# print(dir(array))

# x = int(input("Какое число будем считать? => "))

# print(f"РЕЗУЛЬТАТ: \nЧисло {x} встречается в вашем массиве {array.count(x)} раз(а).")
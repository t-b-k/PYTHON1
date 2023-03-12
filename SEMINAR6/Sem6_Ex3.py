# Задача 3. 
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

count = int(input('Введите кол-во элементов в первом массиве => '))
list1 = []
for _ in range(count) : 
    list1.append(int(input('Введите элемент массива => ')))

# unique_elements = list(set(list1))
# sums_of_entries = set()

# sum = 0
# for i in range(len(unique_elements)) : 
#     sum += list1.count(unique_elements[i])//2
# print(sum)

# Вариант через словарик

dict_list = {}.fromkeys(list1,0)
print(dict_list)

for i in list1 : 
    dict_list[i] += 1

print(sum([j//2 for j in dict_list.values() if not j%2]))
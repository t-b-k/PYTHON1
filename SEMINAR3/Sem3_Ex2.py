# Задача 2. 
# Дана последовательность из N целых чисел и число К
# Необходимо сдвинуть всю последовательность на K элементов вправо (K - положительное число)
# Input: 1 2 3 4 5
# K = 3
# Output: 3 4 5 1 2 

init_list = [1, 2, 3, 4, 5]
k = 5
for i in range(k % 5) : 
    init_list.insert(0, init_list.pop(-1))

print(init_list)
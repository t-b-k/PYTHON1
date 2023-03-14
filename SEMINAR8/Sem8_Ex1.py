# Как преобразовать список строк в список целых чисел? 

list1 = input("Введите послед-ть целых чисел через пробел => ").split()
print(*list(map(int, list1)))

list2 = [(x,x*x) for x in [int(x) for x in input("Введите послед-ть целых чисел через пробел => ").split()]]
print(list2)

def x_and_square_x (x) : 
    return (x, x*x)

data = '1 3 45 36 4 3 7'
# print(data)
# data = data.split()
print(data)
data = list(map(int, data.split()))




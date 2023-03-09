# В списке хранятся числа. 
# Нужно выбрать только четные числа и составить список пар: 
# (число, квадрат_числа)
# Пример: 
#    1 2 3 5 8 15 23 38
# => [(2,4), (8,64), (38, 1444)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data : 
    if i % 2 == 0 : 
        res.append((i, i*2))

# Попробуем улучшить наш код с использованием lambda-функции. 

data = [1, 2, 3, 5, 8, 15, 23, 38]

def select (f, col) : 
    return ([f(i) for i in col])

def where (f, col) : 
    return[x for x in col if f(x)]

def square (x) : 
    return x**2

res = select (int, data)
print(res)

res = where (lambda x: x % 2 == 0, res)
print(res)

res = select(lambda x: (x, x**2), res)
print(res)

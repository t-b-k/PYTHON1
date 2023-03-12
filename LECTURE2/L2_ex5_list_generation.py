# Генерация списков - одна из особенностей языка Python
# List coomprehension - это упрощенный подход к созданию списка, 
# который задействует цикл FOR, а также конструкции if-else для определения того, 
# что в итоге окажется в списке

# 1. Простая ситуация - список: 

# list_1 = [exp for item in iterable] # 

# 2. Выборка по заданному условию

# list_1 = [exp for item in iterable (if conditional)]

# ПРИМЕР: Создать список чисел от 1 до 100
# Традиционный подход: 

list_1 = []
for i in range(1, 101): 
    list_1.append(i)
print(list_1)

# С использованием list comprehension: 

list_1 = [i for i in range(1, 101)]
print(list_1)

# Сформируем список всех четных чисел в диапазоне от 1 до 100

list_2 = [i for i in range(1, 101) if i % 2 == 0]
print(list_2)

# Можно создать список пар четных чисел

list_2 = [(i, i) for i in range(1, 101) if i % 2 == 0]

list_2 = [i*2 for i in range(10) if i % 2 == 0]









def cacl2 (a, b) :
    return a*b

def math (op, x, y) : 
    print(op(x, y))

# def calc1 (a, b) : 
#     return (a + b)

# Lambda позволяет сильно укоротить запись: 
calc1 = lambda a, b: a+b

math (calc1, 5, 45)

# А можно, даже не определяя отдельно функцию calc1, 
# поместить ее определение прямо в то место, где мы хотим ею воспользоваться

math (lambda a, b: a+b, 5, 45)
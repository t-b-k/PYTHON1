def f(x) :
    return(x*x)

print(f(5))    # На печать будет выведено число 25
print(type(f)) # Результат будет - <'class function'>

a = f
print(type(a))  # Результат будет - <'class function'>

def calc1 (a, b) : 
    return a+b

def calc2 (a, b) : 
    return a*b

def math (op, x, y) : 
    print(op(x, y))

# Попробуем воспользоваться нашей функцией math : 

math (calc1, 5, 4)
math (calc2, 5, 4)



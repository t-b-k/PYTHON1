x = 0
y = 0

# Напишем метод, который будет отвечать за инициализацию 
# переменных x и y
def init (a, b) : 
    global x
    global y
    x = a
    y = b

# Теперь напишем метод, который будет находить их сумму: 

def do_it () : 
    return x+y

# init(11, 12)

# print(f"x = {x}")
# print(f"y = {y}")


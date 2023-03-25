# Задача: напишите программу, которая на вход получает 
# два целых числа - А и В - и возводит число А в целую степень 
# с помощью рекурсии
# Для пущего интереса будем допускать отрицательную степень

a = int(input('Введите целое число А, отличное от нуля => '))

def degree (a, b) : 
    if a == 0 : 
        return 0            # Результат 0 обозначает ошибку, сделано для целостности функции
    elif b == 0 :        
       return 1
    elif b > 0 : 
        return a*degree(a, b-1)
    else : 
        return (1/a)*degree(a, b+1)

if a == 0 : 
    print("Число А не может быть нулем! Вы не справились с вводом. ") 
# Не будем продолжать какие-либо действия, если пользователь не справился со 
# вводом первого числа
else : 
    b = int(input('Введите целое число В => '))
    print(f"{a} в степени {b} равно {degree(a, b)}")
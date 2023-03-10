# Задача. 
# Введено натуральное число N и следом - последовательность из 
# N элементов. 
# Требуется вывести эту последовательность на экран в обратном порядке. 
# ЗАМЕЧАНИЕ: В программе запрещается объявлять массивы и использовать циклы. 

# n = int(input("Введите количество чисел в последовательности => ")) 

# def print_reverse (n) : 
#     num = int(input("Введите число: "))
#     if n == 1 : 
#         print(num)
#     else : 
#         print_reverse(n-1)
#         print(num)

# Напишем вариант, при котором числа могут вводиться в строку

# def reorder (number, step=1, val1=0) :
#     if step == number : 
#         val1 = input("Введи символ: ")
#         print(val1, end = ' ')
#     else: 
#         val1 = input("Введи символ: ")
#         reorder(number, step+1, val1)
#         print(val1, end = ' ')

# nums = int(input("Введите количество чисел в последовательности => ")) 
# reorder(nums)

# Теперь сделаем через строку

def reorder (number) :
    if number == 0: 
        return ""
    stroka = input()
    return reorder(number-1) + stroka

nums = int(input("Введите количество чисел в последовательности => ")) 
print(reorder(nums))


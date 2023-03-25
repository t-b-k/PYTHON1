# Задача. 
# Хакер Василий получил доступ к классному журналу, 
# и хочет заменить все свои минимальные оценки на 
# максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: максимальные - на минимальные. 

import random
n = int(input("Введите количество оценок => "))

grades = [random.randint(1,5) for i in range(n)]

print(grades)

min_grade = min(grades)
max_grade = max(grades)

# new_grades = [min_grade if i == max_grade else i for i in grades]
# print(new_grades)

# Вариант с рекурсией

def Hacker (grades_list, ind) : 
    if grades_list[ind] == max_grade : 
        grades_list[ind] == min_grade
    if ind == 0 : 
        return grades_list
    else : 
        return Hacker(grades_list, ind-1)
    
new_grades = Hacker(grades, len(grades)-1)
print(new_grades)
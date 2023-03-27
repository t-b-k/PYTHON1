def input_surname () : 
    max_attempts = 3
    attempt_count = 1
    print("Введите фамилию (у вас {max_attempts} попытки(ок)): ")
    for i in range(max_attempts) : 
        surname = input(f"{i+1} - ")
        if surname != "" and surname.isalpha() : 
            return surname.title()
    return ""
    
print (input_surname())
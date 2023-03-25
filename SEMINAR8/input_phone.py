# Функция возвращает строку с номером телефона внутри населенного пункта. 
# Если пользователь не справился с вводом, возвращает пустую строку
# Номер телефона может содержать от 5 до 8-ми цифр

def input_phone () : 
    max_attempts = 3
    print("Введите номер телефона. У вас {max_attempts} попытка(ки)(ок)). ")
    print("Номер телефона может содержать от 5-ти до 8-ми цифр. ")
    res = "" 
    for i in range(max_attempts) :   
        phone = input(f"{i+1} - ")
        if phone.isdigit() and int(phone) > 0 and len(phone) in range(5,9) : 
            res = phone
            return res
    return res    

print(input_phone())
def input_city_code () : 
    max_attempts = 3
    print("Введите код города(оператора). У вас {max_attempts} попытка(ки)(ок)). ")
    print("Код города (оператора) содержит от 2-х до 5-ти цифр. ")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1} - ")
        if code.isdigit() and int(code) > 0 and len(code) in range(2,6) : 
            res = code
            return res
    return res    

print(input_city_code())
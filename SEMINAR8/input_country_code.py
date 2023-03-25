def input_country_code () : 
    max_attempts = 3
    print("Введите код страны. У вас {max_attempts} попытка(ки)(ок)). ")
    print("Код страны содержит не более 3-х цифр. ")
    print("По умолчанию используется код России - +7")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1} - +")
        if code == "" : 
            res = "+007"
            return res
        elif code.isdigit() and int(code) > 0: 
            if len(code) == 1 : 
                res += "+00" + code
                return res 
            if len(code) == 2 : 
                res += "+0" + code
                return res
            if len(code) == 3 : 
                res += "+" + code
                return res
    return res    
    
print (input_country_code())
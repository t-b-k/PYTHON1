# Задача № 49. 
# Создать телефонный справочник с возможностью импорта и экспорта 
# данных в формате .txt. Фамилия, имя, отчество, номер телефона - 
# данные, которые должны храниться в файле. 
# 1. Программа должна выводить данные в терминал
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска
#    определенной записи (например, имя или фамилию человека)
# Использование функций. 
# Ваша программа не должна быть линейной. 

# Мы считываем информацию, куда-то складываем и потом взаимодействуем. 
# У нас будет список. 
# В чем проблема текстового файла? Можно только дописывать. 
# Внести изменения нельзя. Только заново все записать.
# Поисковую функцию можно разбить на другие функции 

from os import path
file_base = "base.txt"
# Чтение - режим по умолчанию!!! 

last_id = 0
all_data = []

if not path.exists(file_base) : 
    with open (file_base, "w", encoding="utf-8") as _: 
        pass
    
def read_records() : 
    global last_id, all_data
    if last_id :  
        with open(file_base, encoding="utf-8") as f : 
            all_data = [i.strip() for i in f]
            last_id = all_data[-1][0]
        return all_data
    return []

def show_all () : 
    if all_data: 
        print(*all_data, sep="\n")
    else: 
        print("Empty data!")

def add_new_contact() : 
    global last_id
    array = ["Surname", "Name", "Patronymic", "Phone_number"]
    string = "" 
    for i in array : 
        string += input(f"Enter {i} => ") + " "
    all_data.append(string)
# Добавить строку, проверяющую наличие такой записи
# При внесении изменений в базу тоже надо проверять на появление дубликатов
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f: 
        f.write(f"{last_id} {string}\n")

def main_menu () : 
    play = True
    while play : 
        read_records()
        answer = input("Phone book: \n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
# Надо добавить Change, Import, Export
# Export - это выгрузка текущей базы в другой файл: Введите название
# будущей базы, пришиваем .txt, проверяем на существование, отдаем в бета-функцию
# import - это изменение переменной file_base на новое имя, которое
# предоставит пользователь. 

        match answer : 
            case "1": 
                show_all()
            case "2": 
                add_new_contact()
            case "3": 
                pass
            case "4": 
                pass
            case "5": 
                pass
            case "6": 
                pass
            case "7": 
                play = False
            case _ : 
                print("Try again!\n")

main_menu()
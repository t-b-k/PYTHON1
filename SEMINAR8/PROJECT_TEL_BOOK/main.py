''' 
Main.py - это стартовый модуль, задача которого - вызвать метод модуля controller, 
который будет запускать бесконечный цикл, получающий входные "сигналы" 
(из определенного набора) из модуля view (user interface).  

В соответствии с полученной пользователем цифрой controller запускает 
тот или иной метод. 

Все данные телефонного справочника будут представлять собой список словарей. 
Каждый элемент этого списка представляет собой словарь. 

[{<Контакт 1>}, {<Контакт 2>}, {}, ... {Контакт N}]

last_id- глобальная переменная, в которой будет храниться номер последней 
занесенной записи

<Контакт i> = {"ID":<Номер записи>, "Name":<Имя_чел>, "Surname":<Отчество>, ... "Tel":<Телефон>} 

Модуль record. 
В данном модуле описываются функции, определяющие формат записи в базу данных
информации от пользователя (склеивает ключи из словаря и значения из view)

Модуль read (Камянецкий). 
    Например: 
        def view_data (data) : 
        print (data)
        def get_value() : 
        return int(input('value '))

Метод export() 
'''
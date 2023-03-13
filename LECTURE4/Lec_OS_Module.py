# Модуль OS предоставляет множество функций для работы с 
# операционной системой, причем их поведение, как правило, 
# не зависит от ОС, поэтому программы, написанные с использованием
# этих функций, остаются переносимыми. 
# Для того чтобы начать работать с данным модулем, необходимо 
# его импортировать: 

import os

# Базовые функции модуля OS: 

# смена текущего директория

# os.chdir ('C:\Users\Татьяна Калашникова\Desktop\PYTHON1')

# Узнать, в каком директории мы находимся: Get Current Working Directory

# print(os.getcwd ())

# Модуль os.path вложен в модуль path и реализует некоторые полезные 
# функции для работы с путями, такие как: 

# os.path.basename(path ) # - базовое имя пути ("последняя миля")

# os.path.abspath(path) # - возвращает нормализованный абсолютный путь

# print (os.path.abspath('main.ru'))
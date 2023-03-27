# В данной программе нам понадобится 5 модулей: 
# 1. Сбор информации с датчиков (data_provider)
#    В этом модуле будут описаны такие методы, как: 
#       get_temperature, get_pressure, get_wind_speed
# 2. Логирование (logger)
#       temperature_logger, pressure_logger, winf_speed_logger
# 3. Интерфейс пользователя (user_interface)
#       temperature_view, pressure_view, wind_speed_view
# 4. HTML-генератор (html_creator)
#       create
# 5. Главный модуль (main - этот)
#       Одна кнопка  - запустить систему

import html_creator as hc
import xml_generator as xg
import data_provider as dp

hc.new_create(xg.new_create(dp.data_collection()))

# print(hc.create())
# print(xg.create())

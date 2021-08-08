#!/usr/bin/env python3
while True:
    text = list(input('Введите текст:').split())  # считываем строку и кладём её в список text
    lower_text = [x.lower() for x in text]  # понижаем регистр и записываем в новый список
    my_dict = {val: lower_text.count(val) for val in set(lower_text)}  # создаём словарь, где ключи это элементы
    # списка,а значения - их количество в списке
    max_value = max(my_dict.values())  # находим максимальное значение в словаре
    final_dict = {k: v for k, v in my_dict.items() if v == max_value}  # создаём новый словарь, состоящий только
    # из элементов, чьи значения совпадают с максимальным
    for key, value in final_dict.items():
        print("{0} - {1}".format(value, key))  # форматированный вывод словаря на экран

#!/usr/bin/env python3
while True:
    text = list(input('Введите текст:').split())           #считываем строку и кладём её в список text
    text = [x.lower() for x in text]                       #понижаем регистр букв в списке
    my_dict = {val: text.count(val) for val in set(text)}  #создаём dict,где ключ это элемент списка,а значение-их количество в списке
    max_value = max(my_dict.values())                      #находим максимальное значение в словаре
    my_dict = {k: v for k, v in my_dict.items() if v == max_value}  #оставляем те элементы словаря, чьи значения совпадают с max
    for key, value in my_dict.items():
        print("{0} - {1}".format(value, key))              # форматированный вывод словаря на экран

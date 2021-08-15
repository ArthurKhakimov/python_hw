#!/usr/bin/env python3
def str_to_int(s):  # функция для преобразования строки в целое число
  if s:
    return (ord(s[-1]) - ord('0')) + 10 * str_to_int(s[:-1])
  else:
    return 0
def even_and_action(e):  # функция для проверки четности и выполнения вычисления
    if e % 2:
        return int(3 * e + 1)
    else:
        return int(e/2)
while True:
    text = list(input('Введите текст:'))
    if ''.join(text).isdigit():  # проверяем строку на содержание "нецифровых" символов
        a = str_to_int(text)
        print(even_and_action(a))
    else:
        if ''.join(text) == 'cancel':  # для выхода из программы
            break
        print("Не удалось преобразовать введенный текст в число.")

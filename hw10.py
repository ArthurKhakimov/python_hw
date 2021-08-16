#!/usr/bin/env python3
def even_and_action(e):  # функция для проверки четности и выполнения вычисления
    if e % 2:
        return int(3 * e + 1)
    else:
        return int(e / 2)


num = int(input('Введите натуральное число:'))
i = 0
while num != 1:
    num = even_and_action(num)
    i = i + 1
print("Число шагов:", i)

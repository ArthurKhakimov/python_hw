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


#  Примеры:
#  Введите натуральное число:70
#  35,106,53,160,80,40,20,10,5,16,8,4,2,1
#  Число шагов: 14
#-----------------------------------------
#  Введите натуральное число:300
#  150,75,226,113,340,170,85,256,128,64,32,16,8,4,2,1
#  Число шагов: 16

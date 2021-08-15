#!/usr/bin/env python3
with open("passwd", "r") as f:
    file = [line for line in f]
with open("group", "r") as f1:
    file1 = [line1 for line1 in f1]
shells = [f.split(":")[-1][:-1] for f in file] # вычленяем все shell в список
shells_dict = {val: shells.count(val) for val in set(shells)} # делаем из списка словарь с количеством каждого
pass_list = [[f.split(":")[0], f.split(":")[2], f.split(":")[3]] for f in file] # список вида [[uname,uid,gid],]
group_list = [[f.split(":")[0], f.split(":")[2], (f.split(":")[3][:-1]).split(",")] for f in file1] # список [[gname,gid,[users]]]
for i in range(len(group_list)):
    group_list[i][2][:] = [item for item in group_list[i][2] if item != ''] # удаляем все пустые элементы в group_list[][2], это нужно чтоб при выводе спика не залезала лишняя запятая
group_dict={}
for i in range(len(group_list)): # из 2 списков, подставляя данные из них, собираем новый словарь
    for j in range(len(pass_list)):
        if group_list[i][1] == pass_list[j][2]:
            group_list[i][2] = group_list[i][2] + [pass_list[j][0]] # дополняем список юзеров информацией из passwd
            for u in range(len(group_list[i][2])):
                if group_list[i][2][u] == pass_list[j][0]:
                    group_list[i][2][u] = pass_list[j][1]  # меняем имена юзеров на их uid
                    group_dict[group_list[i][0]] = group_list[i][2] # словарь с уже только нужными данными для записи в файл
with open("output.txt", "w") as f:
    for key, value in shells_dict.items():
        f.write("{0} - {1};".format(key, value)) # запись в файл с требуемым форматированием
    f.write("\n")
    for key, value in group_dict.items():
        f.write("{0}:{1},".format(key, ', '.join(value))) # запись в файл с требуемым форматированием.

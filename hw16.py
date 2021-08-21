#!/usr/bin/env python3
import re
from geopy.geocoders import Nominatim

with open("gps.txt", "r") as f:
    gps = [re.sub("[\n|'|'']", '',line) for line in f if line.strip()]  # читаем из файла в список,с удалением лишних символов
gps1 = [re.split(r'[,;]', s) for s in gps]  # разбиваем строку на градусы,минуты и секунды
gps_dd = [[float(s[0]) + float(s[1])/60 + float(s[2])/3600,float(s[3]) + float(s[4])/60 + float(s[5])/3600] for s in gps1]
geolocator = Nominatim(user_agent="test")  # высчитываем десятичные координаты
location = [[f'Location: {geolocator.reverse(s).address}', f"Goggle Maps URL:https://www.google.com/maps/search/?api=1&query={','.join(map(str,s))}"] for s in gps_dd]
[print("".join(i)) for s in location for i in s]  # Вывод с форматиррованием

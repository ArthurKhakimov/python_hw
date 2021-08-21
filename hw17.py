#!/usr/bin/env python3
from exif import Image
import glob

a = glob.glob('*.jpg')  # Получаем список всех jpg файлов
for n in a:
    with open(n, "rb") as photo:
        image = Image(photo)  # Получаем метаданные
    x = image.gps_latitude  # Извлекаем координаты
    y = image.gps_longitude  
    with open("gps.txt", "a") as f:
        f.write(f"{x[0]},{x[1]}',{x[2]}'';{y[0]},{y[1]}',{y[2]}''\n")  # Пишем в файл с форматированием
import hw16  # Вызываем hw16

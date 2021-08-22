#!/usr/bin/env python3
from PIL import Image
import glob

def resize_image(percent):  # Функция для получения миниатюр изображений, параметром надо передать размер в процентах от исходного
    a = glob.glob('photo_for_hw18/*.*')  # получаем список всех файлов
    for s in a:
        saved = "photo_for_hw18/" + "resized_" + str(percent) + "%_" +s[15:]  # шаблон нового имени файла
        img = Image.open(s)
        width, height = img.size
        size = (width * percent / 100, height * percent / 100)  # высчитываем новый размер файла
        img.thumbnail(size)  # меняем размер
        img.save(saved)  #  сохраняем в новый файл

if __name__ == '__main__':
    resize_image(10)

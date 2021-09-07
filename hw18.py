#!/usr/bin/env python3

# Переделал так, чтобы в функцию передавали путь до каталога с фотографиями.

from PIL import Image
import glob


def resize_image(photo_folder,percent):  # Функция для получения миниатюр изображений, параметрами надо передать имя каталога и размер в процентах от исходного размера
    a = glob.glob(photo_folder+'/*.*')  # получаем список всех файлов
    for s in a:
        saved = photo_folder + '/resized_' + str(percent) + '%_' +s[15:]  # шаблон нового имени файла
        img = Image.open(s)
        width, height = img.size
        size = (width * percent / 100, height * percent / 100)  # высчитываем новый размер файла
        img.thumbnail(size)  # меняем размер
        img.save(saved)  #  сохраняем в новый файл

if __name__ == '__main__':
    resize_image('photo_for_hw18',10)

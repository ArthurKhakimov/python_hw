#!/usr/bin/env python3
#  Переделал и начал принимать тип шкалы в параметрах к функции


def temperature_converter(t, scale):
    """Функция для конвертации температуры из Цельсия в Фаренгейт и наоборот.
    Передаваемые параметры: температура и тип шкалы('f' для Фаренгейта, 'с' для Цельсия)"""
    if scale == 'f':
        celcium = 5.0 * (t - 32) / 9
        result = f'{celcium} C'
    elif scale == 'c':
        fahrenheit = (9 / 5.0 * t) + 32
        result = f'{fahrenheit} F'
    else:
        result = "Некорректный ввод параметров"
    return result


if __name__ == "__main__":
    print(temperature_converter(100,'f'))
    print(temperature_converter(100, 'c'))
    print(temperature_converter(100, 'k'))

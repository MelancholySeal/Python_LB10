#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":

    # Определение множества гласных букв
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    # Ввод строки с клавиатуры
    input_string = input("Введите строку: ")

    # Подсчет количества гласных в строке
    count_vowels = sum(1 for char in input_string.lower() if char in vowels)

    # Вывод результата
    print(f"Количество гласных в введенной строке: {count_vowels}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    input_string = input("Введите строку: ")

    count_vowels = sum(1 for char in input_string.lower() if char in vowels)

    print(f"Количество гласных в введенной строке: {count_vowels}")

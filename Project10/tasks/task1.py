#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":

    A = {'b', 'e', 'f', 'k', 't'}
    B = {'f', 'i', 'j', 'p', 'y'}
    C = {'j', 'k', 'l', 'y'}
    D = {'i', 'j', 's', 't', 'u', 'y', 'z'}

    X = (A & C) | (B & C)
    Y = (A - B) | (D - C)

    print("Результат X:", X)
    print("Результат Y:", Y)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":

    A = {'b', 'e', 'f', 'k', 't'}
    B = {'f', 'i', 'j', 'p', 'y'}
    C = {'j', 'k', 'l', 'y'}
    D = {'i', 'j', 's', 't', 'u', 'y', 'z'}

    X = (A & B) | (B & C)
    Y = (A & (set() if not B else set()) | (D - C))

    print("Результат X:", X)
    print("Результат Y:", Y)

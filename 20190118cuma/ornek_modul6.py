#!/usr/bin/python
# -*- coding:UTF-8 -*-

def listeTopla(liste):
    toplam = 0
    for i in liste:
        if type(i) == int:
            toplam = toplam + i
    return toplam
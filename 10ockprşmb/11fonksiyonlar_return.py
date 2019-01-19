#!/usr/bin/python
# -*- coding: UTF-8 -*-

# fonksiyonların geriye değer döndürmesi return

# def topla(s1,s2):
#     print("toplama sonucu = ",(s1+s2))
#
# toplamaSonucu =topla(10,20)
# print(toplamaSonucu)

# yukarıdalki fonksiyon geriye değer döndürmez.

def topla(s1,s2):
    sonuc = (s1+s2)
    return sonuc

toplamaSonucu = topla(10,20)
print(toplamaSonucu)

degisken = topla(30,40)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# isim parametreli fonksiyonlar

def ornekFonksiyon(ad,soyad,telefon):
    print("ad=",ad)
    print("soyad=",soyad)
    print("telefon=",telefon)

ornekFonksiyon("esra","ünal","02121112233")
ornekFonksiyon("02123336655","mehmet","kurnaz")
ornekFonksiyon(telefon="02123336655",ad="mehmet",soyad="kurnaz")

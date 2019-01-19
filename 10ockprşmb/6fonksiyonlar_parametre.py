#!/usr/bin/python
# -*- coding: UTF-8 -*-

# parametreli fonksiyonlar

# def mesajYaz():
#     print("merhaba, dünya!")
# mesajYaz()

def mesajYaz( parametre ):
    print("merhaba,",parametre)

mesajYaz("php")
mesajYaz("sait")

# bir örnek
def topla( sayi1,sayi2 ):
    print("toplam=",(sayi1+sayi2))

topla(10,20)
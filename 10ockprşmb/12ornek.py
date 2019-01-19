#!/usr/bin/python
# -*- coding: UTF-8 -*-

def topla(x,y):
    return x+y

def carp(x,y):
    return x*y

s1=int(input("birinci sayı = "))
s2=int(input("ikinci sayı = "))

islem = input("bir işlem seçin (1-topla,2-çarp) =")

if islem=="1":
    sonuc=topla(s1,s2)
elif islem=="2":
    sonuc=carp(s1,s2)
else:
    sonuc="geçersiz işlem seçildi.."

print(sonuc)
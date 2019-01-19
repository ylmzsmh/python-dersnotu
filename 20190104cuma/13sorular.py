#!/usr/bin/python
# -*-  coding: UTF-8 -*-

# dışarıdan girilen 3 adet sayının en büyüğünü ekrana yazdıran python kodu?

s1 = int(input("sayi 1 = "))
s2 = int(input("sayi 2 = "))
s3 = int(input("sayi 3 = "))

if s1 > s2:
    enBuyuk = s1
else:
    enBuyuk = s2

if s3 > enBuyuk:
    enBuyuk = s3

print(s1,s2,s3," sayıları arasından en büyük olanı ", enBuyuk,sep=",")

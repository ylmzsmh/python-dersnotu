#!/usr/bin/python
# -*- coding: UTF-8 -*-

# çarpma operatörü kullanmadan dışarıdan girilen 2 sayının çarpımını bulan programı yazınız?


x= int(input("sayı1 = ")) # 2
y= int(input("sayı2 = ")) # 3

sonuc = 0 # 0
i = 1 # 1

while i <= y: #  True, True, True, False
    sonuc = sonuc + x # 2,4,6
    i += 1 # 2,3,4

print("sonuç =",sonuc)
print(i)
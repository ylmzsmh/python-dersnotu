#!/usr/bin/python
# -*- coding: UTF-8 -*-

# while ile True Kullanımı

# i=1
# while True:
#    print(i,"python")
#    if i==10:
#        break
#    i += 1

# bir örnek

while True:
    soru = input("Menü Seçin (Çıkmak İçin q Ya Bas..) = "),
    print(type(soru))
    if soru=="q":
        print("Çıkılıyor..")
        break
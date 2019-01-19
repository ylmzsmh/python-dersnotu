#!/usr/bin/python
# -*-  coding: UTF-8 -*-

# baslangıç ve bitiş arasındaki sayıların 3 ve 5 e tam bölünenlerin toplamını hesaplayan ve yazdıran kodu while döngüsü ile oluşturun?
# sayılar kullanıcıdan alınacak

ba = int(input("başlangıç : "))
bi = int(input("bitiş : "))
toplam = 0

while ba<=bi:
    if ba%3==0 and ba%5==0:
        toplam = toplam + ba
        # print(ba)
    ba +=1

print(toplam)
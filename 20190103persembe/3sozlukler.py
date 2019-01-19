#!/usr/bin/python
# -*- coding: UTF-8 -*-
# sözlükler
# örnek bir tanımlama
sozluk = {
    "marka":"fiat",
    "model":"fiorino",
    "yıl":2015
}
print("sözlük tipi =",type(sozluk))
print("sözlük değerleri =",sozluk)

# öğelere erişmek
print("sözlüğün herhangi bir öğesi =",sozluk["marka"])
# olmayan bir key yazılırsa hata oluşur

# öğelere erişmek
print("sözlüğün herhangi bir öğesi =", sozluk.get("marka","aradığınız bilgi bulunamadı"))

# değer değiştirme
sozluk["yıl"]=2019
print(sozluk)

# değer ekleme
sozluk["fiyat"]=120
print(sozluk)

# bir sözlükte bir key bir defa kullanılır

# iç içe sözlük oluşturma
icerik= {"model":"egea","yıl":2018}
sozluk={
    "marka":"fiat",
    "bilgiler":icerik
}
print(sozluk)

# sözlük uzunluk
print(len(sozluk))

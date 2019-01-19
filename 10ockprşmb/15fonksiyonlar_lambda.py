#!/usr/bin/python
# -*- coding: UTF-8 -*-

# lambda kullanımı

def elma(param):
    return param+10
print(elma(10))

# aynı işlemi lambda ile yapalım
armut= lambda param:param+10
print(armut(10))

# lambda  ile birden fazla argüman alma
kiraz = lambda a,b:a+b
print(kiraz(1,2))
'''
üstteki kodun açıklaması
tanımlanan fonksiyonuı kiraz  değişkenine ata
bu fonksiyona a ve b değişkenleri gelsin
fonksiyon bu a ve b değişkenlerini toplayıp geriye return etsin.
'''
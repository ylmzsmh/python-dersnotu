#!/usr/bin/python
# -*- coding: UTF-8 -*-
# DEMETLER
# demet tanımlama
demet = ("fındık","ceviz","kiraz")
print(type(demet))
print(demet)

# demetin herhangi bir öğesine erişmek
print(demet[0])
print(demet[0:2])

# demeti silmek
del demet
# print(demet)

# demetin değeri değişmez
# demet = ("fındık","ceviz","kiraz")
# demet[0]="fıstık"

# demetteki elemanın sıra numasını almak
print(demet.index("kiraz"))

# örnek
demet = ("fındık","ceviz","kiraz")
print("tipi =",type(demet)," içeriği =",demet)
liste=[demet]
print("tipi =",type(liste)," içeriği =",liste)
# elemanlarına erişelim
print("listenin eleman adedi = ",len(liste))
print(liste[0])
print(liste[0][0])
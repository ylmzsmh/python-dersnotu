#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
parametre olarak aldığı listedeki sayıları toplayan bir modul dosyası yazarak bo modül dosyasını kullanarak aşağıdaki listedeki sayıları toplayınız.

liste=["mustafa",79,"baskın",90,"mert",50,"ebru","45"]
'''
liste=["20","mustafa",70,"baskın",90,"mert",50,"ebru",40]
toplam=0
for i in liste:
    if type(i)==int:
        toplam = toplam + i
print(toplam)

# modül oluşturmak için

def listeTopla(liste):
    toplam = 0
    for i in liste:
        if type(i) == int:
            toplam = toplam + i
    return toplam

import ornek_modul6
print("modülümüzü kullandık=",ornek_modul6.listeTopla(liste))

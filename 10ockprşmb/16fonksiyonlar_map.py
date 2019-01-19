#!/usr/bin/python
# -*- coding: UTF-8 -*-

# map kullanımı

# sayıların karesini alalım ve listeye atalım
sayilar=[1,2,3,4,5]
'''kareAl fonksiyonu kendisine gönderilen sayının karesini alıp geri döndürür'''
def kareAl(sayi):
    return sayi*sayi
'''yeniSayilar isminde boş bir liste tanımladık'''
yeniSayilar=[]
'''sayilar listesini iterate ettik.
her bir değeri i değişkenine aktardık'''
for i in sayilar:
    # karesini aldığımız değeri karesi değişkenine atadık.
    karesi =kareAl(i)
    yeniSayilar.append(karesi)
print(sayilar)
print(yeniSayilar)

'''yeniSayilar listesini sildik.'''
del yeniSayilar

# yukarıdaki işlemi map ile yapalım

sayilarimiz=[1,2,3,4,5]
def karesiniAl(sayi):
    return sayi**2
yeniSayilar=list(map(karesiniAl,sayilarimiz))
print(sayilarimiz)
print(yeniSayilar)

del yeniSayilar

# yukarıdaki işlemi map ve lambda ile yapalım
sayilarimiz=[1,2,3,4,5]
yeniSayilar=list(map(lambda x:x**2,sayilarimiz))
print(sayilarimiz)
print(yeniSayilar)
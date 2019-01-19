#!/usr/bin/python
# -*- coding: UTF-8 -*-

# liste tanımlama ve listeyi görme
liste = ["mustafa","erkan",28,34]
print(liste)
print(type(liste))

# boş bir liste tanımlama
liste=[]
print(type(liste))

# listenin uzunluğu len
liste = ["mustafa","erkan",28,34]
adet =len(liste)
print(adet)

# aşağıdaki listenin eleman adedi
liste=["erkan","mustafa","muhammet","ahmet","muhammet","aliihsan","mustafa"]
adet =len(liste)
print(adet)

ad="mustafa"
soyad="yılmaz"
yas=35
boy=179

isimler=[ad,soyad,yas,boy]
print(isimler)

# listedeli elemanlara erişmek

# bilgi = listede bir key(anahtar,indis,sıra numarası) birde value (değer) kavramı vardır. ve listenin ilk öğesinin sıra numarası 0 'dır.
# listenin keylerine müdahale edilemez.

kisi=['mustafa', 'yılmaz', 35, 179]

# yukarıdaki listeyi baz alarak

# herhangi bir öğeye erişmek

ad = kisi[0]
print("adnız=",ad)
print("soyadınız=",kisi[1])
print("yaşınız=",kisi[2])
print("boyunuz=",kisi[3])

# son eğeye ulaşmak
kisi=['mustafa', 'yılmaz', 35, 179]
print("son öğe = ",kisi[3])
print("son öğe = ",kisi[len(kisi)-1])
print("son öğe = ",kisi[-1])

# ilk öğeye ulaşmak
kisi=['mustafa', 'yılmaz', 35, 179]
print("ilk öğe =",kisi[0])
print("ilk öğe =",kisi[-3])
print("ilk öğe =",kisi[-len(kisi)])

# listedeki belirli öğelere ulaşmak dilimleme
liste=["erkan",37,"mustafa",35,"muhammet",2,"ahmet",38,"muhammet",25,"aliihsan",29,"mustafa",38]
dilimler = liste[0:7]
print(dilimler)

dilimler = liste[2:4]
print(dilimler)

# öncekiler
liste=["erkan",37,"mustafa",35,"muhammet",2,"ahmet",38,"muhammet",25,"aliihsan",29,"mustafa",38]
print(liste)
oncekiler = liste[:5]
print(oncekiler)

# sonrakiler
liste=["erkan",37,"mustafa",35,"muhammet",2,"ahmet",38,"muhammet",25,"aliihsan",29,"mustafa",38]
print(liste)
sonrakiler = liste[8:]
print(sonrakiler)
print(type(sonrakiler))

# listeye eleman eklemek append
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi.append("ezgi")
print(kisi)

# listeye eleman eklemek insert
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi.insert(0,"emine")
print(kisi)

# listeye veri eklemek diğer bir yöntem silerek
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi[0]="burcu"
print(kisi)

# diğer ekleme yöntemleri
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi[1:1]=["ezgi","yasin","mert"]
print(kisi)

# diğer ekleme yöntemleri
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi[1:2]=["ezgi","yasin","mert"]
print(kisi)

# diğer ekleme yöntemleri
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi[1:]=["ezgi","yasin","mert"]
print(kisi)

# diğer ekleme yöntemleri
kisi=['mustafa', 'yılmaz', 35, 179]
print(kisi)
kisi[5:]=["ezgi","yasin","mert"]
print(kisi)






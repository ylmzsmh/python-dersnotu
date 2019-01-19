#!/usr/bin/python
# -*- coding: UTF-8 -*-

# aşağıdaki verileri içeren
# sabit bir sözlük oluşturun
# ad=mustafa
# soyad=yılmaz
# yas=35
#
# ad=can veysel
# soyad=şoroğlu
# yas=27
#
# ad=semih
# soyad=yılmaz
# yas=25

isimler = {
    1:{
        "ad":"mustafa",
        "soyad":"yılmaz",
        "yas":35
    },
    2:{
        "ad": "can veysel",
        "soyad": "şoroğlu",
        "yas": 27
    },
    3:{
        "ad": "semih",
        "soyad": "yılmaz",
        "yas": 25
    }
}

# print(isimler)

# diğer bir örnek
# kullanıcıdan alınan 3'er adet ad,soyad ve yas bilgisini tek bir sözlükte toplayınız?

sozluk={}

ad1= input("ad1 = ")
ad2= input("ad2 = ")
ad3= input("ad3 = ")
soyad1=input("soyad1 = ")
soyad2=input("soyad2 = ")
soyad3=input("soyad3 = ")
yas1=input("yas1 = ")
yas2=input("yas2 = ")
yas3=input("yas3 = ")

veri1={
    "ad":ad1,
    "soyad":soyad1,
    "yas":yas1
}
veri2={
    "ad":ad2,
    "soyad":soyad2,
    "yas":yas2
}
sozluk[0]=veri1
sozluk[1]=veri2
sozluk[2]={"ad":ad3,"soyad":soyad3,"yas":yas3}
print(sozluk)
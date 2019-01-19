#!/usr/bin/python
# -*- coding: UTF-8 -*-

# sözlükten değer silme (del)
sozluk={
    "marka":"fiat",
    "model":"fiorino",
    "yıl":2018
}

print(sozluk)

del sozluk["yıl"]

print(sozluk)

# sözlükten değer silme (pop)
sozluk={
    "marka":"fiat",
    "model":"fiorino",
    "yıl":2018
}
print(sozluk)
sozluk.pop("yıl")
print(sozluk)

# sözlüğü bütün olarak silmek
del sozluk
# print(sozluk)

# sözlükten son değeri silme
sozluk={
    "marka":"fiat",
    "model":"fiorino",
    "yıl":2018
}
print(sozluk)
sozluk.popitem()
sozluk.popitem()
print(sozluk)

# sözlüğü boşaltmak
sozluk={
    "marka": "fiat",
    "model": "fiorino",
    "yıl": 2018
}
print(sozluk)
sozluk.clear()
print(sozluk)

# diğer bir sözlük tanımlama şekli(dict)
sozluk=dict(ad="mustafa",soyad="yılmaz",yas=35)
print(type(sozluk))
print(sozluk)

# KEYS VE VALUES KAVRAMLARI
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
print(isimler.keys())
print(isimler[1].keys())

print(isimler.values())
print(isimler[1].values())

# araştırma konuları
# copy()
# fromkeys()
# setdefault()
# update()
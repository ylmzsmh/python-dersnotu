#!/usr/bin/python
# -*- coding: UTF-8 -*-

# kullanıcıdan bir belirli aralıkta sıra numarası alıp sözlükteki değerlerini,
# ekrana
# mustafa yılmaz 35 şeklinde
# yazdıran kodu oluşturunuz
# listeniz.
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

siraNo = int(input("Sıra No = "))
print(isimler[siraNo]["ad"],isimler[siraNo]["soyad"],isimler[siraNo]["yas"])
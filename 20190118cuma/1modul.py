#!/usr/bin/python
# -*- coding:UTF-8 -*-
# import random
# chars=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',0,1,2,3,4,5,6,7,8,9]
# # print(random.choices(chars))
# adet = int(input("adet= "))
# sifre =""
# for i in range(0,adet):
#     sifre += str(random.choice(chars))
# print("şifre= ",sifre)

# import string
# import random
# alfabeKucuk= string.ascii_lowercase
# print("küçük harfler=",alfabeKucuk)
# alfabeBuyuk= string.ascii_uppercase
# print("büyük harfler=",alfabeBuyuk)
# rakamlar = string.digits
# print("rakamlar=",rakamlar)
# buyukKucukHarfler=string.ascii_letters
# print("büyük küçük harfler=",buyukKucukHarfler)
# ozelKarakter=string.punctuation
# print("özel karakterler=",ozelKarakter)
#
# # örnek
# charsLetter = alfabeKucuk+alfabeBuyuk+rakamlar
# adet=20
# sifre = list(random.choice(charsLetter) for i in range(adet))
# print("şifremiz=",sifre)
#
# # üstteki liste olarak üretilen şifreyi tek bir değişkende toplamak için
# # birinci yöntem
# password=""
# for i in sifre:
#     password +=i
# print("password=",password)
# # ikinci yöntem
#
# password = "".join(sifre)
# print("password=",password)

# kendi modülümüzü yazmak
def carp(s1,s2):
    s=s1*s2
    return s

# üstteki ifadeyi bir dosyaya yazıp kaydettikten sonra bu artık bir modüldür.
# çağırmak istediğinizde dosya ismini yazmanız yeterli olacaktır.

import random
# print(dir(random))
for s in dir(random):
    print(s)
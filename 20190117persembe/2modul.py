#!/usr/bin/python
# -*- coding:UTF-8 -*-

# import random
# # print(dir(random))
# rastgeleSayi = random.randint(1,100)
# print(rastgeleSayi)

# modülleri import etme (içe aktarmak)

# # yöntem 1
# import random
# print(random.randint(1,100))

# # yöntem 2
# from random import *
# print(randint(1,100))

# # yöntem 3
# from random import randint
# print(randint(1,100))

# # yöntem 4
# from random import randint as r
# print(r(1,100))

# # soru
# # bir harf ve bir sayıdan bir sayıdan rastgele bir şifre üretin.
# harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# sayilar =[0,1,2,3,4,5,6,7,8,9]
# import random
# harfKey= random.randint(0,25)
# sayiKey = random.randint(0,9)
# rastgeleHarf=harfler[harfKey]
# rastgeleSayi=sayilar[sayiKey]
# sifre = rastgeleHarf+str(rastgeleSayi)
# print("şifre=",sifre)

# soru
# kullanıcıdan karakter istenecek örnek 5-10 arası girilen adet kadar karakterli şifre üretilecek
harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sayilar =[0,1,2,3,4,5,6,7,8,9]
import random
adet = int(input("adet giriniz= "))
yeniAdet=adet//2
sifre = ""
if adet%2==0:
    sayi="çift"
else:
    sayi="tek"
i=1
while i<=yeniAdet:
    sifre += harfler[random.randint(0,25)]
    sifre += str(sayilar[random.randint(0,9)])
    if i==yeniAdet:
        if sayi=="tek":
            sifre += harfler[random.randint(0, 25)]
    i +=1
print("şifre=",sifre)
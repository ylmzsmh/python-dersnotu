#!/usr/bin/python
# -*- coding:UTF-8 -*-
# hatalar

# # programcı (syntax) hataları
# print("merhaba, dünya!")
# # echo "merhaba, dünya!"
# # print "merhaba, dünya!"

# # program hataları( bug )
# s1 = input("sayi1")
# s2 = input("sayi2")
# toplam = int(s1)+int(s2)
# s3 = input("sayi3")
# sonuc = toplam+s3
# print(sonuc)

# # istisnalar
# s1=int(input("sayi1= "))
# s2=int(input("sayi2= "))
# # if s2==0:
# #     print("sıfıra bölüm hatası")
# #     exit()
# bolum=float(s1/s2)
# print("bölüm=",bolum)


# # istisnalar
# try:
#     s1=int(input("sayi1= "))
#     s2=int(input("sayi2= "))
#     bolum=float(s1/s2)
#     print("bölüm=",bolum)
# except:
#     print("bir hata oluştu")

# ValueError
# ZeroDivisionError

# # bir örnek
# # s1=input("sayı1 = ")
# # s2=input("sayı2 = ")
# # try:
# #     s1=int(s1)
# #     s2=int(s2)
# #     bolum= float(s1/s2)
# #     print("bölüm= ",bolum)
# # except ValueError:
# #     print("sayı girilmedi..")
# # except ZeroDivisionError:
# #     print("0'a bölünenemez..")
# # except:
# #     print("bir hata oluştu..")


# bir örnek
s1=input("sayı1 = ")
s2=input("sayı2 = ")
try:
    s1=int(s1)
    s2=int(s2)
    bolum= float(s1/s2)
    print("bölüm= ",bolum)
except(TypeError,ValueError,ZeroDivisionError) as hataMesaji:
    print("Kullanıcı kaynaklı bir hata oluşturdunuz >:( ")
    print("hata mesajı.: ",str(hataMesaji))

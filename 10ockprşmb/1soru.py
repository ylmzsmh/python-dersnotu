#!/usr/bin/python
# -*- coding: UTF-8 -*-

# bir değişkene tutulan bir sayı atanacak,
# kullanıcıdan 3 defada bu sayıyı bulması istenecek
# eğer bulursa doğru tahmin
# bulamaz ise
# 2.şansınız, tahmininiz= diye tekrardan soracak
# eğer 3 defada bilemez ise tahmin edemediniz
# eğer 3 defa da bulursa dorğu tahmin yazacak
# kodu oluşturunuz?

tutulanSayi =3
print("1-50 arası bir sayı tahmin ediniz, 3 hakkınız var,!")

hak=1
while hak<=3:
    print(str(hak)+". hakkınız, tahmininizi girin = ")
    tahmininiz = int(input())
    if tahmininiz==tutulanSayi:
        print("Doğru Tahmin Ettiniz..")
        break
    hak += 1
else:
    print("3 hakkınızda tahmin edemediniz..")





#!/usr/bin/python
# -*- coding: UTF-8 -*-

# aşağıdaki listeyi
isimler = ["python","php","html"]
# ekrana
# python = p-y-t-h-o-n
# php = p-h-p
# html = h-t-m-l
# şeklinde yazdırın?

'''isimler listesini iterasyona tabi tutup her bir değerini li adında bir değişkene aktarıyoruz'''
for li in isimler:
    '''li değişkenini yazdır ve sonrasında bir = bırak'''
    print(li,end="=")
    '''listedeki bir elemanın (şuan li içinde bulunuyor) uzunluğunu alıyoruz'''
    uzunluk = len(li)
    adet = 1
    '''li değişkeninin içinde bulunan kelimeyi iterate ediyoruz.'''
    for karakter in li:
        '''eğer son karakter yazdırılıyor ise'''
        if uzunluk==adet:
            print(karakter,end="")
            '''son karakter değil ise'''
        else:
            print(karakter,end="-")
        adet += 1
    print("")
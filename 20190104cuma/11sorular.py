#!/usr/bin/python
# -*-  coding: UTF-8 -*-
# başlangıç ve bitiş arasında ki sayılardan çift olanlarını ekrana yazdıran kopdu oluşturunuz.?
# bir sayının 2 ye bölümünden kalan (mod %) 0 ise çifttir.

baslangic = int(input("başlangıç : "))
bitis = int(input("bitiş : "))

while baslangic<=bitis:
    if baslangic%2==0:
        print(baslangic)
    baslangic +=1

# aynı örnek for ile

baslangic = int(input("başlangıç : "))
bitis = int(input("bitiş : "))

for i in range(baslangic,bitis+1):
    if i%2==0:
        print(i)

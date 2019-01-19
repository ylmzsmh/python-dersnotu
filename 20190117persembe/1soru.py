#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pprint
'''
bir kurumda personel bilgileri saklanmak istenmektedir. personelin adı +soyadı+T.C. kimlik numarası+oda numarası+dahili telefon numarası
bir sözlük veri yapısı ile tutulması planlanıyor.
programı kullanan kişi var olan verileri silebilmeli,yeni veri ekleyebilmeli ve varolan bilgiler üzerinde değişijklik yapabilmelidir.?
'''

isimler = {
    1:{
        "ad":"ömer",
        "soyad":"çelikten",
        "tc":"12345678910",
        "oda":1,
        "dahili":"07"
    },
    4:{
        "ad":"mustafa",
        "soyad":"durna",
        "tc":"12345678911",
        "oda":2,
        "dahili":"08"
    },
    3:{
        "ad":"muhammet bera",
        "soyad":"yılmaz",
        "tc":"12345678912",
        "oda":3,
        "dahili":"09"
    },
    2:{
        "ad":"mustafa",
        "soyad":"yılmaz",
        "tc":"12345678913",
        "oda":4,
        "dahili":10
    }
}
# print("isimler listesi")
# pprint.pprint(isimler)
# print()

while True:
    print("::::menü::::")
    print("ekleme (1) ")
    print("güncelleme (2) ")
    print("silme (3) ")
    print("tüm liste (4) ")
    secim=input("seçiminiz (q çıkış ) = ")

    if secim=="q":
        print("çıkılıyor...")
        break
    elif secim=="4":
        print("tüm kişiler")
        pprint.pprint(isimler)
    elif secim=="1":
        # isimlere yeni isim ekleyelim
        ad=input("ad= ")
        soyad=input("soyad= ")
        tc=input("tc= ")
        oda=input("oda= ")
        dahili=input("dahili= ")
        siraNo = max(isimler.keys()) + 1
        isimler[siraNo] = {"ad": ad, "soyad": soyad, "tc": tc, "oda": oda, "dahili": dahili}
        print("bilgiler eklendi..")
        # pprint.pprint(isimler)
    elif secim =="2":
        # kişi arama ve güncelleme
        aranaAd= input("Güncellenecek ad = ")
        listeAdet=len(isimler.items())
        adet=1
        for siraNo,degerler in isimler.items():
            # sozlukDegerlerListesi = list(degerler.values())
            # if aranaAd==sozlukDegerlerListesi[0]:
            if aranaAd==degerler["ad"]:
                print(degerler["ad"],"-",degerler["soyad"],"-",degerler["tc"],"-",degerler["oda"],"-",degerler["dahili"])
                sorAra = input("Güncellemek istediğiniz kişi Bumu? (e/h = )")
                if sorAra=="e":
                    ad = input("ad= ")
                    soyad = input("soyad= ")
                    tc = input("tc= ")
                    oda = input("oda= ")
                    dahili = input("dahili= ")
                    isimler[siraNo]["ad"]=ad
                    isimler[siraNo]["soyad"]=soyad
                    isimler[siraNo]["tc"]=tc
                    isimler[siraNo]["oda"]=oda
                    isimler[siraNo]["dahili"]=dahili
                    print("bilgiler Güncellendi..")
                    break
                else:
                    if adet==listeAdet:
                        print("aradığınız bulunadı..")
            else:
                if adet == listeAdet:
                    print("aradığınız bulunadı..")
            adet +=1

    elif secim=="3":
        # Kişi arama ve silme
        silinecekAd = input("Silinecek ad = ")
        for siraNo,degerler in isimler.items():
            sozlukDegerlerListesi=list(degerler.values())
            if silinecekAd==sozlukDegerlerListesi[0]:
                print(degerler["ad"], "-", degerler["soyad"], "-", degerler["tc"], "-", degerler["oda"], "-",
                      degerler["dahili"])
                sorAra = input("silmek istediğiniz kişi Bumu? (e/h = )")
                if sorAra=="e":
                    del isimler[siraNo]
                    print("bilgiler silindi..")
                    break
#!/usr/bin/python
# -*-  coding: UTF-8 -*-

# aşağıdaki notları yazı ile yazan kodu oluşturun?
# 0-44   = kaldı
# 45-54  = geçer
# 55-69  = orta
# 70-84  = iyi
# 85-100 = pekiyi
# aralık dışında ise geçersiz not yazdıran kodu if şartı oluşturunuz?


sinav = 44.5

# birinci yol

if sinav>=0 and sinav<=44:
    print("kaldı")
elif sinav>=45 and sinav<=54:
    print("geçer")
elif sinav>=55 and sinav<=69:
    print("orta")
elif sinav>=70 and sinav<=84:
    print("iyi")
elif sinav>=85 and sinav<=100:
    print("pekiyi")
else:
    print("geçersiz sinav")

# ikinci yol

if sinav<0:
    print("geçersiz sinav")
elif sinav<45:
    print("kaldı")
elif sinav<55:
    print("geçer")
elif sinav<70:
    print("orta")
elif sinav<85:
    print("iyi")
elif sinav<101:
    print("pekiyi")
else:
    print("geçersiz sinav")


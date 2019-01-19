#!/usr/bin/python
# -*- coding: UTF-8 -*-

# fonksiyonlarda global kavramı

x=2

def fonk():
    global sonuc
    global y
    print(x)
    print(y)
    sonuc = x+y
    y=102


y=5
fonk()
print(sonuc)
print(y)
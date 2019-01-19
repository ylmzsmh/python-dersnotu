#!/usr/bin/python
# -*-  coding: UTF-8 -*-

# aşağıdaki kod bloklarının çıktısı ne olur?

# birinci

sayi=7
if sayi>3:
    print("3")
    if sayi<5:
        print("5")
        if sayi==7:
            print("7")

# ikinci

if 1+1==2:
    if 2*2==8:
        print("if")
    else:
        print("else")

# üçüncü

if (1==1) and (2+2>3):
    print("true")
else:
    print("false")

# dördüncü

if not True:
    print("1")
elif not(1+1==3):
    print("2")
else:
    print("3")
    
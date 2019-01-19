#!/usr/bin/python
# -*-  coding: UTF-8 -*-

# soru

# aşağıdaki iki değişkeni (a,b)
# a büyüktür b
# b büyüktür a
# a eşittir b
# şeklinde ekrana yazdıran kodu oluşturunuz?

a=10
b=20

if a>b:
    print(a," büyüktür ",b)
elif b>a:
    print(b," büyüktür ",a)
else:
    print(a," eşittir ",b)
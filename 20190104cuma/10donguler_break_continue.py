#!/usr/bin/python
# -*-  coding: UTF-8 -*-
# break deyimi

i=1
while i<6:
    print(i)
    if i==3:
        break
    i += 1

print("##########")

# continue deyimi

i=0
while i<6:
    i += 1
    if i==3:
        continue
    print(i,end=" ")
    print("elma")

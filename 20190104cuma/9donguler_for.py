#!/usr/bin/python
# -*-  coding: UTF-8 -*-
# for döngüsü
# esasında iterasyon için kullanılır.

# i=1
# while i<=10:
#     print(i)
#     i+=1


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i,end=" ")

# range komutu ile liste üretmek için
sayiListesi = list(range(1,10))
print(sayiListesi)

# range komutunu for ile kullanmak
for i in list(range(10)):
    print(i)

# range komutu ile artırım adedi belirlenebilir.
print(list(range(0,11,2)))

# for ile else kullanımı

for x in range(10):
    print(x)
else:
    print("bitti")

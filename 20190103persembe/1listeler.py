#!/usr/bin/python
# -*- coding: UTF-8 -*-

# listeden eleman silme (remove)
liste=["elma","armut","kiraz"]
print(liste)
silinen = liste.remove("armut")
print(silinen)
print(liste)
# remove geriye değer döndürmez
# değere göre silme yapar

# listeden eleman silme (pop)
liste=["elma","armut","kiraz"]
print(liste)
silinen=liste.pop(1)
print(silinen)
print(liste)

# listeden eleman silme (del)
liste=["elma","armut","kiraz"]
print(liste)
del liste[0]
print(liste)
del liste
print(liste)

# listeyi temizleme(clear)
liste=["elma","armut","kiraz"]
print(liste)
liste.clear()
print(liste)

# araştırma
# aşağıdaki komutların görevlerini araştırınız?
# count()
# copy()
# extend()
# sort()
# reverse()





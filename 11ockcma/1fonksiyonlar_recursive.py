#!/usr/bin/python
# -*- coding:UTF-8 -*-

# recursive fonksiyonlar

# def yaz(sayi): # 3,2,1
#     if sayi==1:
#         print(sayi)
#     else:
#         print(sayi) #3,2,1
#         sayi = sayi - 1 #2,1,0
#         yaz(sayi) # 2,1
# yaz(10)

# recursive ile listeyi ekrana yazdıralım

# önceklikle döngü ile yazdıralım
liste=["meryem","hatice","muhammet bera","ismet","emine"]
# for str in liste:
#     print(str)

# şimdi recursive ile yazdıralım

'''
["meryem","hatice","muhammet bera","ismet","emine"]
["hatice","muhammet bera","ismet","emine"]
["muhammet bera","ismet","emine"]
["ismet","emine"]
["emine"]
[]
'''
def listeYaz(liste):
    if len(liste)==0:
        pass
    else:
        print(liste[0]) # meryem,hatice,muhammet bera,ismet
        '''
        ["hatice","muhammet bera","ismet","emine"]
        ["muhammet bera","ismet","emine"]
        ["ismet","emine"]
        ["emine"]
        []
        '''
        liste = liste[1:]
        '''
        ["hatice","muhammet bera","ismet","emine"]
        ["muhammet bera","ismet","emine"]
        ["ismet","emine"]
        ["emine"]
        []
        '''
        listeYaz(liste)
# listeYaz(liste)

isimler = ["ahmet","aliihsan","mustafa","muhammet","volkan"]

'''
["ahmet","aliihsan","mustafa","muhammet","volkan"]
["aliihsan","mustafa","muhammet","volkan"]
[ "mustafa", "muhammet", "volkan"]
["muhammet","volkan" ]
["volkan" ]
[]
'''
def isimleriYaz( liste ):
    if len(liste)==0:
        return ""
    else:
        '''
        [ "aliihsan","mustafa","muhammet","volkan"]
        [ "mustafa", "muhammet", "volkan"]
        [ "muhammet", "volkan"]
        ["volkan"]
        []
        '''
        yeniListe=liste[1:]
        '''
        ahmet + ["aliihsan","mustafa","muhammet","volkan"]
        ahmet + aliihsan + [ "mustafa", "muhammet", "volkan"]
        ahmet + aliihsan + mustafa + ["muhammet","volkan" ]
        ahmet + aliihsan + mustafa + muhammet + ["volkan]
        ahmet + aliihsan + mustafa + muhammet + volkan
        '''
        return liste[0] +"\n"+ isimleriYaz(yeniListe)
print(isimleriYaz(isimler))


# python ile faktöriyel

'''
5,4,3,2,1
'''
def faktoriyel(sayi):
    '''
    false,false,false,false,true
    '''
    if sayi==1:
        return 1
        '''
        -5*4*3*2*1-
        '''
    else:
        '''
        5*(5-1)
        5*4*(4-1)
        5*4*3*(3-1)
        5*4*3*2*(2-1)
        '''
        return sayi*faktoriyel(sayi-1)
print(faktoriyel(5))


#!/usr/bin/python
# -*- coding:UTF-8 -*-
# os modülü
# kullanılan işletim sistemi ile ilgili bilgiler verir.

# import os

# # işletim sistemini bize verir
# print(os.name)
# '''
# nt=windows
# posix=linüx
# mac=macintosh
# '''
# # neden kullanılır
# # örnek
# isletimSistemi = os.name
# if isletimSistemi== "nt":
#     print("windows işletim sistemi")
#     '''windows işletim sistemine ait kodlar'''
# elif isletimSistemi=="posix":
#     print("linüx işletim sistemi")
#     '''linüx işletim sistemine ait kodlar'''
# elif isletimSistemi=="mac":
#     print("mac işletim sistemi")
#     '''mac işletim sistemine ait kodlar'''

# diğer bir örnek
# if os.name=="posix":
#     olustur = os.system("mkdir 'ornekDizin'")
#     if olustur==True:
#         print("linüx de klasör oluşturuldu.")
#
# if os.name=="nt":
#     olustur = os.system("md 'ornekDizin'")
#     if olustur==0:
#         print("windows da klasör oluşturuldu.")

# kullandığımız işletim sistemini öğrenmek
# import platform
# print(platform.system()+" "+ platform.release())

# dizin içeriğini listelemek
# import os
# print(os.listdir())
#
# # bulunduğumuz dizini öğrenmek
# print(os.getcwd())
#
# # örnek
# print(os.listdir(os.getcwd()))
#
# # örnek
# # indirilenler dizinini listelemek
# dizinIcerigi = os.listdir("c:/Users/lab08/downloads")
# # print(dizinIcerigi)
# for di in dizinIcerigi:
#     print(di)


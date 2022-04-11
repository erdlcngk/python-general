# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 02:36:35 2022

@author: Erdal
"""

import pandas as pd

# sözlük oluştur
dictionary = {"isim": ["ali","veli","kenan","ayşe","murat","hilal"],
              "yas":[15,16,17,18,33,45],
              "maas": [100,200,300,400,500,600]}
veri = pd.DataFrame(dictionary)
print(veri)

# ilk 5 satır
print(veri.head())

# verinin sütunlarını yazdırma
print(veri.columns)

# veri bilgisi
print(veri.info())

# istatistiksel özellikler
print(veri.describe())

# yas sütunu
print(veri["yas"])

# sütun ekleme
veri["sehir"] = ["Ankara","İstanbul","Konya","Hatay","İzmir","Adıyaman"]
print(veri)

# yas sütunu
print(veri.loc[:,"yas"])

# yas sütunu ve 3 satır
print(veri.loc[:2,"yas"])

# yas sütunu ve 3 satır
print(veri.loc[:2,["yas","isim"]])

# satırları tersten yazdır
print(veri.loc[::-1,:])

# yas sütunun iloc ile yazdırma
print(veri.iloc[:,1])

# ilk 3 satır ve yas ve isim
print(veri.iloc[:3,[0,1]])

# filtreleme
dictionary = {"isim": ["ali","veli","kenan","ayşe","murat","hilal"],
              "yas":[15,16,17,18,33,45],
              "sehir": ["Ankara","Ankara","Konya","Hatay","Konya","Adıyaman"]}
veri = pd.DataFrame(dictionary)

# yaşa göre filtreleme yas > 22
filtreleme1 = veri.yas > 22
filtrelenmis_veri = veri[filtreleme1]
print(filtrelenmis_veri)

# ortalama yas 
ortalama_yas = veri.yas.mean()

veri["yas_grubu"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)

# birleştirme
dictionary1 = {"isim": ["ali","veli","kenan"],
              "yas":[15,16,17],
              "sehir": ["Ankara","Ankara","Konya"]}

dictionary2 = {"isim": ["ayşe","murat","hilal"],
              "yas":[18,33,45],
              "sehir": ["Hatay","Konya","Adıyaman"]}

veri1 = pd.DataFrame(dictionary1)
veri2 = pd.DataFrame(dictionary2)

# dikey
veri_dikey = pd.concat([veri1,veri2],axis = 0)

# yatay
veri_yatay = pd.concat([veri1,veri2],axis=1)
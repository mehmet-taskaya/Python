# TEMEL İŞLEMLER

import numpy as np

# array oluşturmak

x = np.array([12,3,4,50, 40])
y = np.array([15,5,6,51, 4])

# iki arrayi birleştirme

np.concatenate([x,y])

# array ayırma

a,b,c=np.split(x,[3,5])

# array sıralama

np.sort(x)

# eleman işlemleri

a[0] = 1 # 0. indise 1 değerini atar
a[:,0] #0. Sütuna erişir
a[0,:] #0. Satıra erişir

# koşullu eleman işlemleri

np.sum(a > 10) #array içinde 10 dan büyük olan tüm sayıları say
np.all(a > 5) # tüm elemanlar için bool tipinde sonuç döner

# matematiksel işlemler

np.add(a,3) # a'nın her elamnına 3 ekler
np.substract() # çıkarma
np.multiply() # çarpma
np.divide() # bölme

np.mean(a) # ortalaması
np.add.reduce(a) #elemanlarını topla
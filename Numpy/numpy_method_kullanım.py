import numpy as np


dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
print(dizi)

dizi=dizi.reshape(3,6) #dizi burada yeniden şekillendiriliyor.

print("matris: ",dizi)
print("şekil: ",dizi.shape)
print("boyut: ",dizi.ndim)
print("veri tipi: ",dizi.dtype)
print("boy: ",dizi.size)

# iki boyutlu array oluşturma
dizi2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(dizi2)

# sıfırlardan oluşan dizi
sifir_dizi = np.zeros((3,4))
print("sıfırlardan oluşan dizi: ",sifir_dizi)

# birlerden oluşan dizi
bir_dizi = np.ones((3,4))
print("birlerden oluşan dizi: ",bir_dizi)

# boş dizi
bos_dizi = np.empty((3,4))
print("boş bir dizi:", bos_dizi)

# arange(x,y,basamak)
dizi_aralik = np.arange(10,50,5)
print("range: ",dizi_aralik)

# linspace(x,y,basamak) iki aralığı verilen parçaya böler ilk ve son dâhil
dizi_bosluk = np.linspace(10, 20, 3)
print("linspace: ",dizi_bosluk)

# float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

# matematiksel işlemler
a = np.array([1,2,3])
b = np.array([3,4,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# dizi elemanları toplama
print(np.sum(a))

# dizi elemanları içerisinde max
print(np.max(a))

# dizi elemanları ortalama
print(np.mean(a))

# dizi elemanları medyan(ortadaki sayı)
print(np.median(a))

# rastgele sayı üretme [0,1] arasında sürekl uniform 3*3
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

# indeks
arr = np.array([1,2,3,4,5,6,7])
print(arr[0])

# dizinin ilk 4 elemanını alma
print(arr[0:4])

# dizinin tersini alma
print(arr[::-1])

# iki boyutlu diziler üzerine
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(dizi2D)

#dizinini birinci satır ve birinci sütunundan bulunan elemanı bulma
print(dizi2D[1,1])

# 1. sütunun tümünü alma
print(dizi2D[:,1])

# satır 1, sütun 1,2,3
print(dizi2D[1,1:4])

# dizinin son satır tüm sütunlarını alma
print(dizi2D[-1,:])

# dizinin son sütun tüm satırlarını alma
print(dizi2D[:,-1])

# diziyi vektör hâline getirme
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(dizi2D)

vektor = dizi2D.ravel()
print(vektor)

# maksimumu sayının indeksi
maksimum_sayinin_indeksi = vektor.argmax()
print("maksimum sayının indeksi: ",maksimum_sayinin_indeksi)

# diziyi tekrar 2 boyutlu hâle getirme
vektor_eski_hal = vektor.reshape(3,4)
print(vektor_eski_hal)
import numpy as np

# numpy dizi oluşturma
np_arr = np.array([10,15,30,45,60])
print(np_arr)


# 5-15 arasındaki sayılardan dizi oluşturma
np_arr = np.arange(5,15)
print("\n","5 - 15 aralığındaki sayılardan oluşan bir dizi: ", np_arr)

# 50-100 arasındaki sayılardan 5'er artarak dizi oluşturma
np_arr = np.arange(50,100,5)
print("\n","50 - 100 arasında sayılardan 5'er artarak oluşan dizi: ", np_arr)

# 10 elemanlı sıfırlardan oluşan dizi oluşturma (dizi float olarak oluşturulur)
np_arr = np.zeros(10)
print("\n","10 elemanlı 0'lardan oluşan dizi: ",np_arr)

# 10 elemanlı birlerden oluşan dizi oluşturma (dizi float olarak oluşturulur)
np_arr = np.ones(10)
print("\n","10 elemanlı 1'lerden oluşan dizi: ", np_arr)

# 0-100 arasında eşit aralıklarla dizi 5 üretme ve dizi oluşturma (100 dahil ediliyor)
np_arr = np.linspace(0,100,5)
print("\n","0 - 100 arasında eşit aralıklarla ", np_arr)


# 10-30 arasında rastgele 5 tane tamsayı üretme
np_arr = np.random.randint(10,30,5)
print("\n","10 - 30 arasında rastgele 5 tane tamsayı üretme: ",np_arr)

# -1 ve 1 arasında 10 adet sayı rastgele sayı üretme
np_arr = np.random.randn(10)
print("\n","-1 ve 1 arasında 10 adet rastgele sayı üretme", np_arr)


# 3x5 boyutunda 10-50 arasında rastgele sayılar tutan bir matris üretme
np_arr = np.random.randint(10,50,15).reshape(3,5)
print("\n","3x5 boyutlarında 10 - 50 sayıları arasındaki sayılardan oluşan bir matris:",np_arr)

# üretilen matrisin satır ve sütunlarının toplamı
np_arr = np.random.randint(10,50,15).reshape(3,5)
rowTotal = np_arr.sum(axis=1)
columnTotal = np_arr.sum(axis=0)
print("\n","matrisin satır ve sütun toplamları: ",np_arr, "\n", "satırlar: ",rowTotal, "\n", "sütunlar: " ,columnTotal)

# üretilen matris veya dizinin en büyük elemanını, en küçük elemanını ve ortalamasını bulma
np_arr = np.random.randint(10,50,15).reshape(3,5)
max_element = np_arr.max()
min_element = np_arr.min()
mean_element = np_arr.mean()
print("\n",np_arr, "\n", "en büyük eleman: ",max_element, "\n", "en küçük eleman: " ,min_element, "\n", "ortalama eleman: ", mean_element)

# üretilen matrisin en büyük değerinin indeksi
np_arr = np.random.randint(10,50,15).reshape(3,5)
max_element = np_arr.argmax()

# 10-20 arasındaki sayıları içeren dizinin ilk 3 elemanı
np_arr = np.arange(10,20)
first_three_element = np_arr[0:3]

# üretilen dizinin elemanlarını tersten yazdırma
np_arr = np.random.randint(1,100,20)
reversed_arr = np_arr[::-1]

# üretilen matrisin ilk satırını seçme
np_arr = np.random.randint(10,50,15).reshape(3,5)
first_line = np_arr[0:1,0:]

# üretilen matrisin 2. satır 3. sütundaki elemanını seçme
np_arr = np.random.randint(10,50,15).reshape(3,5)
selected_element = np_arr[1,2]

# üretilen matrisin tüm satırlardaki ilk elemanını seçme
np_arr = np.random.randint(10,50,15).reshape(3,5)
selected_elements = np_arr[:,0]

# üretilen matrisin herbir elemanının karesi
np_arr = np.random.randint(10,50,15).reshape(3,5)
squared_arr = np_arr **2 # Burada dizinin kendisiyle çarpımı (np_arr * np_arr) da yazılsa aynı sonucu verirdi. Dizideki
# herbir eleman kendi indisindeki elemanla çarpılıyor.

# üretilen matristeki pozitif ve çift sayıları bulma
np_arr = np.random.randint(-50,50,30)
print(np_arr)
positif_numbers = np_arr[np_arr > 0]
positif_and_even_numbers = positif_numbers[positif_numbers %2 == 0]
print(positif_and_even_numbers)
liste = ["1","2","5a","10b","abc","10","50"]

## Liste elemanları içindeki sayısal değerleri bulunuz
# for i in liste:
#     try:
#         sonuc = int(i)
#         print(sonuc)
#     except:
#         continue

## Kullanıcı "q" değerini girmekikçe aldınığız her inputun sayı olduğundan emin olunuz aksi hâlde hata mesajı yazınız.
# while True:
#     kullanici_degeri = input("Lütfen bir değer giriniz: ")
#     if(kullanici_degeri == "q"):
#         print("q ile çıkış yaptınız")
#         break
#     try:
#        kullanici_degeri = float(kullanici_degeri)
#        print(f"girilen sayi: {kullanici_degeri}")
#
#     except:
#         print("Lütfen bir sayı veya 'q' değerini giriniz")

## Dictionary ve key bilgilerini parametre olarak alan get(d, key) fonksiyonlarını hazırlayınız.
urun = {"urunAdi": "Poco"}
def get(d,key ):
    try:
        return d[key]
    except:
        return None

print(get(urun,"fiyat"))
print(get(urun, "urunAdi"))



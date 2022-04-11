import module_db
def urunEkle(product, fiyat):
    module_db.urunler.append({"id": len(module_db.urunler) + 1, "urunAdi":product, "fiyat":fiyat})

def urunGuncelle(id,product,price):
   module_db.urunler[id - 1].update({"id":id, "urunAdi":product, "fiyat":price})
   return module_db.urunler




def urunleriGetir():
    return module_db.urunler
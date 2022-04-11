import pandas as pd
df = pd.read_csv("C:/Users/Erdal/Desktop/Uygulamalar Ve Dosyalar/Kod/python/Basit Düzey/Pandas/Veri Setleri/citrus.csv")
result = df.sort_values(by="name")
print(result)
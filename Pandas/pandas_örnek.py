import pandas as pd

df = pd.read_csv("C:/Users/Erdal/Desktop/Uygulamalar Ve Dosyalar/Kod/python/Basit Düzey/Pandas/Veri Setleri/nba_all_seasons.csv")

result = df

# ilk 10 kayıt getirilir.
result = df.head(10)

# hangi kolonda kaç kayıt olduğunu sayar
result = df.index

# tüm oyuncuların kilo ortalaması
result = df["player_weight"].mean()

# en uzun boy
result = df["player_height"].max()

# en uzun boylu oyuncu
result = df[df["player_height"]==df["player_height"].max()]["player_name"].iloc[0]

# yaşı 20-25 arasında olan oyuncuların isim ve college bilgileri
result = df[(df["age"]>=20) & (df["age"]<=25)].sort_values(by="age",ascending=False)[["player_name","college","age"]]

# "Michael Cage" isimli oyuncunun college bilgisi
result = df[df["player_name"] == "Michael Cage"]["college"].iloc[0] # .eq() methodu da kullanılabilirdi

# Takımlara göre oyuncuların ortalama maaş ağırlık bilgisi
result = df.groupby("college").mean()["player_weight"]

# Kaç farklı college vardır
result = len(df.groupby("college"))

# Her college'den kaç oyuncu vardır
result = df.groupby("college").size()
# result = df["college"].value_counts() -> bu daha verimli ve incelenmesi daha rahat

# ismi içerisinde "and" geçen kayıtları getirme
result = df[df["player_name"].str.contains("and")].merge(df[df["player_name"].str.contains("And")],how="outer")

print(result)
import pandas as pd

# .cvs dosyasının açık şekilde konumu belirtilir. Örneğin:
df = pd.read_csv("C:/Users/Erdal/Desktop/Uygulamalar Ve Dosyalar/Kod/python/Basit Düzey/Pandas/Veri Setleri/ENvideos.csv")

# ilk 10 kaydı getirme
result = df.head(10)

# ikinci 5 kaydı getirme
result = df[5:10]

# Dataset'te bulunan kolon isimleri ve kolon sayısını bulma
result = df.columns
#print(result, "\n", result.size)

# Aşağıda bulunan bazı kolonalrı silin ve kalan kolonları listeleyin
#(thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed, description)
result = df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"], axis =1)

# Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz
result = df[["likes","dislikes"]].mean()

# İlk 50 videonun like ve dislike kolonlarını getirme
result = df[["likes","dislikes"]].head(50)

# En çok görüntülenen videoyu getirme
# result = df[["title","views"]].max()
result = df[df["views"].max() == df.loc[:,"views"]][["title","views"]]

# En düşük görüntülenen videoyu getirme
# result = df[["title","views"]].min()["title"]
result = df[df["views"].min() == df["views"]][["title","views"]]

# En fazla görüntülenen 10 videoyu getirme
result = df[["title","views"]].sort_values(by="views",ascending=False).head(10)["title"]

# Kategoriye göre beğeni ortalamalarını sıralı şekilde getirme
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# Kategoriye göre yorum sayılarını yukarıdan aşağıya göre sıralama
result = df.groupby("category_id").sum().sort_values("comment_count")["comment_count"]

# Her kategoride kaç video olduğunu gösterme
result = df["category_id"].value_counts()

# Her videonun title uzunluğu bilgisini yeni bir kolonda gösterme
df["title_lenght"] = df["title"].str.len()
result = df[["title","title_lenght"]]

# Her video için kullanılan tag sayısını yeni bir kolonda gösterme
df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
result = df[["title","tags","tag_count"]]

# En popüler videoları listeleme (like ve dislike oranına göre)

def likedislike(dataset):
    likeList = list(dataset["likes"])
    dislikelist = list(dataset["dislikes"])
    liste = list(zip(likeList,dislikelist))

    oranlistesi = []

    for like,dislike in liste:
        if(like+dislike)==0:
            oranlistesi.append(0)
        else:
            oranlistesi.append(like/(like+dislike))
    return oranlistesi
    


print(likedislike(df))


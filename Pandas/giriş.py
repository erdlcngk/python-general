import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(3,100,9).reshape(3,3), index=["a","b","c"], columns= ["sayi1","sayi2","sayi3"])
result = df[["sayi1","sayi2","sayi3"]].sum(axis=0)
result= df.loc[:,:"sayi3"]
df["sayi4"] = pd.Series(np.random.randint(3,10,3),["a","b","c"])
df.loc["d"]=pd.Series(np.random.randint(3,10,4))
df.loc["d","sayi4"]=4.32
# df.drop("d",axis=0)
result = df.copy
df.loc["f" and "d",["sayi1","sayi2","sayi3","sayi4"]] = np.random.randint(10,50,4,)
print(df[(df["sayi1"]>50)&(df["sayi2"]<90)][["sayi3"]]) #sağ tarafta iki parantez içerine yazmamızın sebebi parantezlerin
#birleştiği noktada sol taraftan dönen değer aslında bir Data Frame ve biz sağ taraftaki parantezlerle dönen Data Frame
#içerisinden filtreleme yapıyoruz
# print(result)

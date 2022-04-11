import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/photos")
response2 = json.loads(response.text)
print(response2)
holder = []
for searcher in response2:
   holder.append(searcher["title"])
print(holder)
with open("deneme1.txt","w") as file:
    json.dump(holder,file,ensure_ascii=False)

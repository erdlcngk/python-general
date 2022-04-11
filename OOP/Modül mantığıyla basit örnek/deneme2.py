class Comment:
    def __init__(self,username:str, text:str, likes:int, dislikes:int):
        self.username = username
        self. text = text
        self.likes = likes
        self.dislikes = dislikes
        print("Yorum bilgileri başarıyla kaydedildi.")

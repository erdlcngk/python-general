from deneme2 import Comment
comment1 = Comment("Erdal", "Merhabalar", 150, 12)
comment2 = Comment("Semih", "Nasılsınız", 70, 7)
comment3 = Comment("Tunahan", "Oyun oynayalım mı?", 50, 20)
allComments = [comment1, comment2, comment3]
for comm in allComments:
    print(comm.username , "\n" , comm.text , "\n" , comm.likes , "\n" , comm.dislikes , "\n\n" )
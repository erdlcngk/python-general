from Card import Card
from Deck import Deck

types = ["karo","sinek","maça","kupa"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deck = Deck.getInstance()

for type in types:
    for value in values:
        card = Card(type,value)
        deck.addDeck(card.kartiGetir())




# print(sinek5.kartiGetir(),karo6.kartiGetir())
# deck.insert(len(deck),sinek5.kartiGetir())
# deck.insert(len(deck),karo6.kartiGetir())
# print(deck)
# deck = Deck.getInstance()
#
# deck.getDeck()
deck.mixDeck()
# deck.getDeck()
deneme = [[],[],[]]
deneme = deck.dealCards(deneme,10)
print(f"***{deneme}***")
deck.getDeck()
deneme[0] = deck.throwCard(deneme[1],"karo 8")


# BAŞARDIN!
# Kendine inanırsan yapamacağın bir şey yok.
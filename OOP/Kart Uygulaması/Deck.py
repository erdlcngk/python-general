import random
class Deck:
    __deck = []
    __instance = None


    def __init__(self):
        if(Deck.__instance != None):
            raise Exception("Bu sınıf singleton bir sınıftır!")
        else:
            Deck.__instance = self
    @staticmethod
    def getInstance():
        if(Deck.__instance == None):
            return Deck()
        return Deck.__instance


    def addDeck(self, card):
        if (len(self.__deck) <= 52 and (not self.__deck.__contains__(card)) and (card.__contains__("kupa") or card.__contains__("maça") or card.__contains__("sinek") or card.__contains__("karo"))):
            self.__deck.append(card)


        else:
            print("Hatalı bir kart bilgisi veya destede zaten olan bir kart girdiniz!")

    def getDeck(self):
        number = 0
        for searcher in self.__deck:
            number+=1
            print(number, "-)",searcher)

    def mixDeck(self):
        return random.shuffle(self.__deck)

    def dealCards(self, allLists, cardAmount):


        for counter2 in range(0,len(allLists)):
            counter1 = 1
            while(counter1 <= cardAmount):
                holder = random.choice(self.__deck)
                self.__deck.remove(holder)
                allLists[counter2].append(holder)
                counter1 += 1

        return allLists

    def throwCard(self,deck,card):
        if(deck.__contains__(card)):
            print(f"{deck} destesinden *{card}* kartını yere attınız!")
            deck.remove(card)
            print(f"Kalan desteniz{deck}")
        else:
            print(f"Bu kart elinizde olmadığından atamazsınız! Şu anki desteniz {deck}")
        return deck


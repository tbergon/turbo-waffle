from random import randint

class Card:

    def __init__(self,v,c):
        self.value = v
        self.color = c

    def IsEqual(self,card):
        if self.value == card.value:
            return True
        return False


class Cards:

    def __init__(self):
        self.cards = list()

    def CreateCards(self):
        for i in range(1,5):
            for j in range(7,15):
                self.cards.append(Card(j,i))

    def Flush(self):
        flushCards = [0] * 32
        print(flushCards)
        for i in range(0,31):
            rand = randint(0,31)
            while flushCards[rand] != 0:
                rand = randint(0,31)
            flushCards[rand] = self.cards[i]
        return flushCards


        
        


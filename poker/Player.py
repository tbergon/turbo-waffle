class Player:

    def __init__(self,name,amount):
        self.name = name
        self.hand = list()
        self.money = amount
    
    def Bet(self,m):
        self.money -= m
        return m
    
    def NewHand(self,a,b):
        self.hand.append(a)
        self.hand.append(b)

    def ClearHand(self):
        self.hand.clear
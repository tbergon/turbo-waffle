from Player import *
from Card import *

class Poker:

    def __init__(self,nbJoueur,mise):
        self.PlayerNumber = nbJoueur
        self.mise = mise
        self.Players = list()

    def Distrib(self,cards):
        cmpt = 0
        for e in self.Players:
            e.hand.append(cards[cmpt])
            e.hand.append(cards[cmpt])
            cmpt += 2
        cmptB = cmpt
        cardOnTable = list()
        while cmpt <= cmptB+5:
            c = cards[cmpt]
            cardOnTable.append(c)
        return cardOnTable


    def Victory(self,player):
        notEnd=True
        for p in self.Players:
            if p.money <= 0:
                print(p," is out.")
                p="Out"
        if self.PlayerNumber <=1:
            notEnd=False
            return "End"
            
            
        
        

    def StartGame(self):
        bet = 0
        notfinished = True

        for _ in range(0,self.PlayerNumber):
            name = input("Enter player name : ")
            p = Player(name,self.mise)
            self.Players.append(p)
            print("Empty hand : ",p.hand)
            # print(p.hand[0].value," of ",p.hand[0].color)
            # print(p.hand[1].value," of ",p.hand[1].color)

        cards = Cards()
        cards.CreateCards()
        c = cards.Flush()

        d = self.Distrib(c)
        turn = 0
        while notfinished:
            for p in self.Players:
                b = int(input("bet : "))
                bet += b
                p.Bet(bet)
            print(d[turn])
            if turn == 4:
                notfinished = False
        '''methode de verif de victoire'''
        

            

nbJoueurs=int(input("Enter the number of players"))
mise=int(input("Enter bet (integer)"))
game=Poker(nbJoueurs,mise)
game.StartGame()

from DeckofCards import *
import random

class Player(object):
    def __init__ (self, stack, position, name):
        self.stack = stack
        self.position = position
        self.name = name
    def getName(self):
        return self.name
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def getStack(self):
        return self.stack
    def setStack(self, stack):
        self.stack = stack
    def addStack(self, win):
        self.stack = self.stack + win
    def bet(self, bet):
        self.stack = self.stack - bet
        return bet
    def fold(self, opp, pot):
        opp.addStack(pot)
    
    
class comPlayer(Player):
    def __init___ (self, stack, position, name, strength = 0):
        Player.__init__ (self, stack, position, name)
    def calcPercentage(self, hand, community):
        rank = Rank()
        tempHand = Hand()
        tempHand.cards = hand.cards
        tempCommunity = Hand()
        tempComm = Hand()
        tempCommunity = community
        wins = 0
        tempComm = Hand()
        for x in range(2000):
            deck = Deck()
            deck.shuffle()
            tempComm.cards = list(tempCommunity.cards)
            opp = Hand()
            deck.dealCard(opp, 2)
            deck.dealCard(tempComm, 5 - tempComm.getLength())
            wins = wins + rank.getWinner(hand, opp, tempComm)
            tempComm.cards = tempCommunity.cards
        self.strength = wins/2000
    def getStrength(self):
        return self.strength
    def getRateReturn(self, strength, pot, amountToCall):
        odds = amountToCall/(amountToCall+pot)
        RR = strength/odds
        return RR
    def betDecision(self,hand, community, pot, amountToCall):
        self.calcPercentage(hand, community)
        strength = self.getStrength()
        if amountToCall !=0:
            RR = self.getRateReturn(strength,pot, amountToCall)
        else:
            RR = 0
        randomCheck = random.randint(0,100)/100
        if RR == 0:
            if self.strength < .5:
                return 1
            else:
                return 2
        
        else:
            if RR < .8:
                if randomCheck < .95:
                    return 0
                else:
                    return 2
            elif RR < 1:
                if randomCheck < .8:
                    return 0
                elif randomCheck < .90:
                    return 1
                else:
                    return 2
            elif RR < 1.5:
                if randomCheck < .6:
                    return 1
                else:
                    return 2
            else:
                if randomCheck < .3:
                    return 1
                else:
                    return 2


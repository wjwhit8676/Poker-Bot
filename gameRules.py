from Player import *
from DeckofCards import *

class gameRules(object):
    def __init__(self, position = 0, pot = 0):
        self.data = []
        self.position = 0
        self.pot = 0
    def getPosition(self):
        return self.position
    def setPosition(self, pos):
        self.position = pos
    def getPot(self):
        return self.pot
    def setPot(self, pot):
        self.pot = pot
    def betCycle(self, player1, player2, hand1, hand2, community, amountToCall):
        pot = self.getPot()
        if self.position == 0:
            dec = player1.betDecision(hand1, community, pot, amountToCall)
            if dec == 0:
                player1.fold(player2, pot)
                print(player1.getName(), "folds.", player2.getName(), "wins,", self.getPot(), ".")
                self.setPot(0)
                return True
            elif dec == 1:
                playerBet = player1.bet(amountToCall)
                pot += playerBet
                amountToCall = 0
                self.setPot(pot)
                print(player1.getName(), "Calls. Current pot: ", self.getPot())
            else:
                playerBet = player1.bet(pot)
                pot +=playerBet
                amountToCall = playerBet - amountToCall
                self.setPot(pot)
                print(player1.getName(), "Raises. Amount to call:", amountToCall)

            dec = player2.betDecision(hand2, community, pot, amountToCall)
            if dec == 0:
                player2.fold(player1, pot)
                print(player2.getName(), "folds.", player1.getName(), "wins,", self.getPot(), ".")
                self.setPot(0)
                return True
            elif dec == 1:
                playerBet = player2.bet(amountToCall)
                pot += playerBet
                amountToCall = 0
                self.setPot(pot)
                print(player2.getName(), "Calls. Current pot: ", self.getPot())
                return False
            else:
                playerBet = player2.bet(pot)
                pot +=playerBet
                amountToCall = playerBet - amountToCall
                self.setPot(pot)
                print(player2.getName(), "Raises. Amount to call:", amountToCall)
                fold = self.indBet(player1, player2, hand1, hand2, community, pot, amountToCall)
                return fold
        if self.position == 1:
            dec = player2.betDecision(hand2, community, pot, amountToCall)
            if dec == 0:
                player2.fold(player1, pot)
                print(player2.getName(), "folds.", player1.getName(), "wins,", self.getPot(), ".")
                self.setPot(0)
                return True
            elif dec == 1:
                playerBet = player2.bet(amountToCall)
                pot += playerBet
                amountToCall = 0
                self.setPot(pot)
                print(player2.getName(), "Calls. Current pot: ", self.getPot())
            else:
                playerBet = player2.bet(pot)
                pot +=playerBet
                amountToCall = playerBet - amountToCall
                self.setPot(pot)
                print(player2.getName(), "Raises. Amount to call:", amountToCall)

            dec = player1.betDecision(hand1, community, pot, amountToCall)
            if dec == 0:
                player1.fold(player2, pot)
                print(player1.getName(), "folds.", player2.getName(), "wins,", self.getPot(), ".")
                self.setPot(0)
                return True
            elif dec == 1:
                playerBet = player1.bet(amountToCall)
                pot += playerBet
                self.setPot(pot)
                print(player1.getName(), "Calls. Current pot: ", self.getPot())
                return False
            else:
                playerBet = player1.bet(pot)
                pot +=playerBet
                amountToCall = playerBet - amountToCall
                self.setPot(pot)
                print(player1.getName(), "Raises. Amount to call:", amountToCall)
                fold = self.indBet(player2, player1, hand2, hand1, community, pot, amountToCall)
                return fold
    def indBet(self, player, opp, hand, oppHand, community, pot, amountToCall):
        dec = player.betDecision(hand, community, pot, amountToCall)
        if dec == 0:
            player.fold(opp, pot)
            print(player.getName(), "folds.", opp.getName(),"wins,",self.getPot(),".")
            self.setPot(0)
            return True
        elif dec == 1:
            playerBet = player.bet(amountToCall)
            pot += playerBet
            self.setPot(pot)
            print(player.getName(), "Calls. Current pot: ", self.getPot())
            return False
        else:
            playerBet = player.bet(pot)
            pot +=playerBet
            amountToCall = playerBet - amountToCall
            print(player.getName(), "Raises. Amount to call:", amountToCall)
            fold = self.indBet(opp, player, oppHand, hand, community, pot, amountToCall)
            return fold
    def payBlinds(self, player1, player2, hand1, hand2, community):
        self.setPot(15)
        pot = 15
        amountToCall = 5
        print("Blinds are being paid")
        if self.position == 0:
            player1.bet(5)
            player2.bet(10)
        else:
            player1.bet(10)
            player2.bet(5)
        fold = self.betCycle(player1, player2, hand1, hand2, community, amountToCall)
        return fold
    
        

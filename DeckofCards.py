import random
import sys

class Card(object):
    suit_names = [None, "Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for rank in range(1,14):
                card = Card(rank, suit)
                self.cards.append(card)

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        self.cards.remove(card)

    def popCard(self, i = -1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def getCards():
        return self.cards

    def dealCard(self, hand, num):
        for i in range(num):
            hand.addCard(self.popCard())



class Hand(Deck):

    def __init__(self, label = ' '):
        self.cards = []
        self.label = label
    def getLength(self):
        return len(self.cards)

class Rank(object):
    def __init__(self, flushSuit = 0,firstCard = '00',secondCard = '00', thirdCard ='00', fourthCard = '00', fifthCard = '00'):
        self.data = []
    def setFlushSuit(self, x):
        self.flushSuit = x
    def getFlushSuit(self):
        return self.flushSuit
    def getRankHist(self, hand):
        rankHist = [0] * 14
        for x in hand.cards:
            rankHist[x.getRank()] += 1
        return rankHist
    def getSuitHist(self, hand):
        suitHist = [0] *5
        for x in hand.cards:
            suitHist[x.getSuit()] += 1
        return suitHist
    def isStraightFlush(self, suitHist, rankHist, hand):
        if self.isFlush(suitHist):
            rankss = rankHist
            flushRanks = [0]*14
            for x in hand.cards:
                rankss[x.getRank()] = x.getSuit()
            for x in range(14):
                if rankss[x] == self.getFlushSuit():
                    flushRanks[x] += 1
            if self.isStraight(flushRanks):
                return '8'+self.firstCard+self.secondCard+self.thirdCard+self.fourthCard+self.fifthCard
            
        
    def isFlush(self, suitHist):
        for x in range(5):
            if suitHist[x] >= 5:
                self.setFlushSuit(x)
                return True
        return False
    def checkFlush(self, suitHist, rankHist, hand):
        if self.isFlush(suitHist):
            ranks = [0]*14
            flushRanks = [0]*14
            count = 0
            for x in hand.cards:
                if x.getSuit() == self.getFlushSuit():
                    flushRanks[x.getRank()] += 1
            flushRanks.reverse()
            for z in range(14):
                if flushRanks[z] > 0:
                    if count == 0:
                        self.firstCard = str(14-z).zfill(2)
                    if count == 1:
                        self.secondCard = str(14-z).zfill(2)
                    if count == 2:
                        self.thirdCard = str(14-z).zfill(2)
                    if count == 3:
                        self.fourthCard = str(14-z).zfill(2)
                    if count == 4:
                        self.fifthCard = str(14-z).zfill(2)
                        return '5'+self.firstCard+self.secondCard+self.thirdCard+self.fourthCard+self.fifthCard
                    count+=1        
            
    
    def isStraight(self, rankHist):
        rankss = rankHist.copy()
        rankss[0] = rankss[13]
        return self.inRow(rankss, 5)
    def checkStraight(self, rankHist):
        ranks = rankHist.copy()
        ranks[0] = ranks[13]
        if self.inRow(ranks, 5):
            return '4'+self.firstCard+'00000000'

    def inRow(self, rankss, n):
        count = 0
        rankss.reverse()
        for i in range(14):
            if rankss[i] > 0:
                count += 1
                if count == n:
                    rankss.reverse()
                    self.firstCard = str(17-i).zfill(2)
                    self.secondCard = str(16-i).zfill(2)
                    self.thirdCard = str(15-i).zfill(2)
                    self.fourthCard = str(14-i).zfill(2)
                    self.fifthCard = str(13-i).zfill(2)
                    return True
            else:
                count = 0
        return False
    def fourKind(self,rankHist):
        for x in range(14):
            if rankHist[x] == 4:
                self.firstCard = str(x).zfill(2)
                rankHist.reverse()
                for y in range(14):
                    if rankHist[y] > 0 and rankHist[y] < 4:
                        self.secondCard = str(14-y).zfill(2)
                        rankHist.reverse()
                        return '7'+self.firstCard+self.secondCard+'000000'
    def checkFull(self, rankHist):
        rankHist.reverse()
        count = 0
        for x in range(14):
            if rankHist[x] == 3:
                self.firstCard = str(14- x).zfill(2)
                for y in range(0,x):
                    if rankHist[y] == 2:
                        self.secondCard = str(14-y).zfill(2)
                        rankHist.reverse()
                        return '6'+self.firstCard+self.secondCard+'000000'
                for y in range(x+1, 14):
                    if rankHist[y] > 1:
                        self.secondCard = str(14-y).zfill(2)
                        rankHist.reverse()
                        return '6'+self.firstCard+self.secondCard+'000000'
    def checkSet(self, rankHist):
        rankHist.reverse()
        count = 0
        for x in range(14):
            if rankHist[x] == 3:
                self.firstCard = str(14- x).zfill(2)
                for z in range(14):
                    if rankHist[z] == 1:
                        if count == 0:
                            self.secondCard = str(14-z).zfill(2)
                        if count == 1:
                            self.thirdCard = str(14-z).zfill(2)
                            rankHist.reverse()
                            return '3'+self.firstCard+self.secondCard+self.thirdCard+'0000'
                        count +=1
        rankHist.reverse()
        
    def pairs(self, rankHist):
        rankHist.reverse()
        count = 0
        for x in range(14):
            if rankHist[x] == 2:
                self.firstCard = str(14-x).zfill(2)
                for y in range(x+1,14):
                    if rankHist[y] == 2:
                        self.secondCard = str(14-y).zfill(2)
                        for z in range(14):
                            if rankHist[z] ==1:
                                self.thirdCard = str(14-z).zfill(2)
                                rankHist.reverse()
                                return '2'+self.firstCard+self.secondCard+self.thirdCard+'0000'
                for z in range(14):
                    if rankHist[z] == 1:
                        if count == 0:
                            self.secondCard = str(14-z).zfill(2)
                        if count == 1:
                            self.thirdCard = str(14-z).zfill(2)
                            rankHist.reverse()
                        if count == 2:
                            self.fourthCard = str(14-z).zfill(2)
                            rankHist.reverse()
                            return '1'+self.firstCard+self.secondCard+self.thirdCard+self.fourthCard+'00'
                        count +=1

    def highCard(self, rankHist):
        rankCopy = rankHist
        rankCopy.reverse()
        count = 0
        for z in range(14):
            if rankCopy[z] == 1:
                if count == 0:
                    self.firstCard = str(14-z).zfill(2)
                if count == 1:
                    self.secondCard = str(14-z).zfill(2)
                if count == 2:
                    self.thirdCard = str(14-z).zfill(2)
                if count == 3:
                    self.fourthCard = str(14-z).zfill(2)
                if count == 4:
                    self.fifthCard = str(14-z).zfill(2)
                    rankCopy.reverse()
                    return '0'+self.firstCard+self.secondCard+self.thirdCard+self.fourthCard+self.fifthCard
                count +=1    
                    
    def getRank(self, hand):
        suitHist = self.getSuitHist(hand)
        rankHist = self.getRankHist(hand)
        rankStr = None
        rankNum = None

        rankStr = self.isStraightFlush(suitHist,rankHist, hand)
        if rankStr != None:
            rankNum = int(rankStr)
            return rankNum

        rankHist = self.getRankHist(hand)

        rankStr = self.fourKind(rankHist)
        if rankStr!= None:
            rankNum = int(rankStr)
            return rankNum

        rankStr = self.checkFull(rankHist)
        if rankStr !=None:
            return int(rankStr)
        rankStr = self.checkFlush(suitHist, rankHist, hand)
        if rankStr !=None:
            return int(rankStr)

        rankHist = self.getRankHist(hand)
        
        rankStr = self.checkStraight(rankHist)
        if rankStr !=None:
            return int(rankStr)

        rankHist = self. getRankHist(hand)
        rankStr = self.checkSet(rankHist)
        if rankStr != None:
            return int(rankStr)
        rankHist = self.getRankHist(hand)
        rankStr = self.pairs(rankHist)
        if rankStr != None:
            return int(rankStr)
        rankStr = self.highCard(rankHist)
        if rankStr != None:
            return int(rankStr)

    def getWinner(self, user, opp, comm):
        userHand = Hand()
        userHand.cards = user.cards + comm.cards
        oppHand = Hand()
        oppHand.cards = opp.cards + comm.cards
        userRank = self.getRank(userHand)
        oppRank = self.getRank(oppHand)
        if userRank == None:
            userRank = 0
        if oppRank == None:
            oppRank = 0
        if userRank > oppRank:
            return 1
        elif userRank < oppRank:
            return 0
        else:
            return 0.5
        
    
if __name__ == '__main__':

    for y in range(2000):
        deck = Deck()
        deck.shuffle()
        user = Hand()
        opp = Hand()
        comm = Hand()
        rank = Rank()

        deck.dealCard(user, 2)
        deck.dealCard(opp, 2)
        deck.dealCard(comm,5)
        print(rank.getWinner(user, opp, comm))
        

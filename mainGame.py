from DeckofCards import *
from Player import *
from gameRules import *

player1 = comPlayer(0, 0, "Player 1")
player2 = comPlayer(0, 1, "Player 2")
rules = gameRules()
cont = 1
while cont == 1:
    deck = Deck()
    deck.shuffle()
    hand1 = Hand()
    hand2 = Hand()
    rank = Rank()
    community = Hand()
    comm = Hand()
    deck.dealCard(hand1, 2)
    deck.dealCard(hand2, 2)

    fold = rules.payBlinds(player1, player2, hand1, hand2, comm)
    if fold == False:
        print(" ")
        print("Dealing flop!")
        deck.dealCard(community, 3)
        for x in community.cards:
            print(x)
        comm.cards = community.cards
        fold = rules.betCycle(player1, player2, hand1, hand2, comm, 0)
    if fold == False:
        print(" ")
        print("Dealing turn!")
        deck. dealCard(community, 1)
        for x in community.cards:
            print(x)
        comm.cards = community.cards
        fold = rules.betCycle(player1, player2, hand1, hand2, comm, 0)
    if fold == False:
        print(" ")
        print("Dealing river!")
        deck. dealCard(community, 1)
        for x in community.cards:
            print(x)
        comm.cards = community.cards
        fold = rules.betCycle(player1, player2, hand1, hand2, comm, 0)
    if fold == False:
        winner = rank.getWinner(hand1,hand2, community)
        print(" ")
        print("Community Cards:")
        for x in community.cards:
            print(x)
        print(" ")
        print("Player 1 Cards:")
        for x in hand1.cards:
            print(x)
        print(" ")
        print("Player 2 Cards")
        for x in hand2.cards:
            print(x)
        print(" ")
        if winner == 1:
            print(player1.getName(), "Wins pot:", rules.getPot())
            player1.addStack(rules.getPot())
            rules.setPot(0)
        elif winner == 0:
            print(player2.getName(), "Wins pot:", rules.getPot())
            player2.addStack(rules.getPot())
            rules.setPot(0)
        else:
            print("The hand was a tie!")
            player1.addStack(rules.getPot()/2)
            player2.addStack(rules.getPot()/2)
            rules.setPot(0)
    print(player1.getName(), "Stack:", player1.getStack())
    print(player2.getName(), "Stack:", player2.getStack())
    if rules.getPosition() == 0:
        rules.setPosition(1)
    else:
        rules.setPosition(0)
    print(" ")
    cont =int(input("Would you like to play another hand? (input 1)"))

# Poker-Bot
My submission for my university senior project. It is a poker bot created in python that will determine strength of the poker hand it is holding and decide on an action to be made.

DeckofCards.py containes the methods responsible for creating poker cards, decks, and hands. It is also able to deal these objects into poker hands. DeckofCards.py also contains the class responsible for determining the types of hand and the winning hand between the two poker hands.
Player.py creates a class for the poker players in the game. It creates separate classes for human players and ai players. The comPlayer class is where the poker bot decides the strength of its hand and decides which move to make.
gameRules.py containes a class responsible for setting up the rules of a typical hand of poker. This class sets up the rules for Heads Up Texas Holdem, which contains only two players. The rules, as of now, only allow for a player to bet or raise the size of the current pot.
mainGame.py is runs through a hand of poker between two ai players. It is a text based representation that allows the user to see the behavior of the ai players.

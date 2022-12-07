from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        
        #Fill the deck
        for cardValue in range(2, 15):
            for suitValue in range(4):
                self.cards.append(Card(cardValue, suitValue))
        
        # Shuffle the deck
        shuffle(self.cards)
        
    def removeCard(self):
        '''This function removes a card from the deck'''
        #Making sure it isn't popping an empty deck
        if len(self.cards) == 0:
            return
        return self.cards.pop()
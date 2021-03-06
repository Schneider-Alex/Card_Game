from . import card
import random
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack", "Queen", "King", "Ace")
values = {"Two": 2,"Three" :3 ,"Four" :4,"Five" :5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10, "Queen":10, "King":10, "Ace":11}


class deck:

    def __init__( self ):
        self.deck =[]
        for suit  in suits:
            for rank in ranks:
                self.deck.append(card.Card(suit,rank))

    def __str__(self):
        deck_contains = ''
        for  card in self.deck:
            deck_contains += "\n" + card.__str__()
        return "The Deck has" + deck_contains
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card






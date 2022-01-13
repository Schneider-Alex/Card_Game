from classes.deck import deck
from classes.hand import Hand
import random







bicycle = deck()
bicycle.shuffle()
player=Hand()
player.add_card(bicycle.deal())
player.add_card(bicycle.deal())
print(player.value)
player.hit_or_stand(bicycle)




for card in player.cards:
    print(card)


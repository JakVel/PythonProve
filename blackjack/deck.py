from collections import deque
import random

from blackjack.suit import Suit
from blackjack.card import Card
from blackjack.rank import Rank

class Deck:
    def __init__(self):
        self.cards = deque()

        #Adds a every card in a card deck once into the deck.
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank=rank, suit=suit))

        #Shuffles the deck
        random.shuffle(self.cards)

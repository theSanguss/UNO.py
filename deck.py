from random import shuffle, randint
from card import Card

class Deck:
    def __init__(self):
            self.cards = self.build_deck()
            self.discard_pile = []
            self.shuffle(randint(1, 3))

    def build_deck(self):
        COLOURS = ("red", "green", "yellow", "blue")
        NUM_CARD_VALUES = ("1", "2", "3", "4", "5", "̲6", "7", "8", "̲9") * 2 + ("0",)    # Operands are used to account for duplicates
        ACT_CARD_VALUES = ("🛇", "⇄", "+ 2") * 2
        WIL_CARD_VALUES = ("⨁", "+ 4") * 4

        full_deck = [Card("NUM", c, v) for c in COLOURS for v in NUM_CARD_VALUES] + \
            [Card("ACT", c, v) for c in COLOURS for v in ACT_CARD_VALUES] + \
            [Card("WIL", "white", v) for v in WIL_CARD_VALUES]    # WILD cards are white, hence built separately

        return full_deck

    def shuffle(self, number_of_shuffles = 1):
        # Veery thorough shuffle
        for _ in range(number_of_shuffles):
            shuffle(self.cards)
            shuffle(self.cards[:len(self.cards)//2])
            shuffle(self.cards[len(self.cards)//2:])

    def draw(self, count = 1):
        drawn_cards = []
        for _ in range(count):
            if not self.cards:
                self.reshuffle_discard_pile()
            drawn_cards.append(self.cards.pop())
        return drawn_cards
    
    def reshuffle_discard_pile(self):
        # Keeps the top card as the only remaining card in discard pile
        self.cards = self.discard_pile[:-1].copy()
        self.shuffle(2)
        top_card = self.discard_pile[-1]
        self.discard_pile.clear()
        self.discard_pile.append(top_card)

'''
@author: rozieblo

Black Jack cards class
'''

import random

class BJCards:
    '''
    Black Jack cards in deck class
    '''
    suits = ('s', 'h', 'd', 'c')
    figures = ('J', 'Q', 'K', 'A')
    cards = 13

    def __init__(self):
        self.__suit__ = [x + 2 for x in \
                         range(0, (BJCards.cards - len(BJCards.figures)))]
        self.__suit__.extend(BJCards.figures)
        self.__cards_in_deck__ = 0
        self.__deck__ = None
        self.reset()

    def reset(self):
        '''
        Reset the deck
        '''
        self.__deck__ = [[x for x in self.__suit__] \
                                       for _ in BJCards.suits]
        self.__cards_in_deck__ = len(BJCards.suits) * BJCards.cards
        random.seed()

    @property
    def cards_in_deck(self):
        '''
        How many cards left on deck
        '''
        return self.__cards_in_deck__

    @staticmethod
    def is_card(card):
        '''
        Check whether it is correct card
        '''
        if len(card) > 3 or len(card) < 2:
            return False
        if len(card) == 3:
            if card[0:2] == '10' \
                and card[2] in BJCards.suits:
                return True
        else:
            if card[0].isdigit():
                if int(card[0]) < 2:
                    return False
                if card[1] in BJCards.suits:
                    return True
            if card[0] in BJCards.figures:
                if card[1] in BJCards.suits:
                    return True
        return False

    def get(self):
        '''
        Get one random card from deck
        '''
        if self.__cards_in_deck__ == 0:
            return None
        card_idx = random.randint(1, self.__cards_in_deck__)
        suit_idx = 0
        for suit in self.__deck__:
            if len(suit) >= card_idx:
                self.__cards_in_deck__ -= 1
                card = suit.pop(card_idx - 1)
                return '{}{}'.format(card, BJCards.suits[suit_idx])
            else:
                card_idx -= len(suit)
                suit_idx += 1

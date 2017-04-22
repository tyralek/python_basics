'''
@author: rozieblo

Black Jack cards class
'''

import random

class BJCards:
    '''
    Black Jack cards in deck class
    '''
    def __init__(self):
        self.__suits__ = ['s', 'h', 'd', 'c']
        self.__cards__ = 13
        self.__figures__ = ['J', 'Q', 'K', 'A']
        self.__suit__ = [x + 2 for x in \
                         range(0, (self.__cards__ - len(self.__figures__)))]
        self.__suit__.extend(self.__figures__)
        self.__cards_in_deck__ = 0
        self.__deck__ = None
        self.reset()

    def reset(self):
        '''
        Reset the deck
        '''
        self.__deck__ = [[x for x in self.__suit__] \
                                       for _ in self.__suits__]
        self.__cards_in_deck__ = len(self.__suits__) * self.__cards__
        random.seed()

    @property
    def cards_in_deck(self):
        '''
        How many cards left on deck
        '''
        return self.__cards_in_deck__

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
                return '{}{}'.format(card, self.__suits__[suit_idx])
            else:
                card_idx -= len(suit)
                suit_idx += 1

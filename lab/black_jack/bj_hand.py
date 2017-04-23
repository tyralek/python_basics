'''
@author: rafalo

Black Jack Hand class
'''
from enum import Enum
from bj_cards import BJCards

class As(Enum):
    '''
    As states
    '''
    WAS_NOT = 0
    WAS_AND_IS_11 = 1
    WAS_AND_IS_1 = 2

class BJHand(object):
    '''
    Black Jack Hand class
    '''
    def __init__(self):
        self.__sum__ = 0
        self.__as__ = 0

    def __handle_as__(self):
        '''
        As is quite complicated
        '''
        if self.__as__ == As.WAS_NOT:
            if self.__sum__ < 11:
                self.__sum__ += 11
                self.__as__ = As.WAS_AND_IS_11
            else:
                self.__sum__ += 1
                # Pylint false-positive R0204
                self.__as__ = As.WAS_AND_IS_1
        elif self.__as__ == As.WAS_AND_IS_11:
            self.__sum__ -= 10  # As is now 1
            self.__sum__ += 1   # add second As
            self.__as__ = As.WAS_AND_IS_1
        else:
            self.__sum__ += 1

    def reset(self):
        '''
        Reset hand
        '''
        self.__sum__ = 0
        self.__as__ = As.WAS_NOT

    @property
    def sum(self):
        '''
        Sum getter
        '''
        return self.__sum__

    def add_card(self, card):
        '''
        Add card to hand
        '''
        if self.sum > 21:
            return False
        if not BJCards.is_card(card):
            return False
        if card[0] == 'A':
            self.__handle_as__()
        elif card[0] in BJCards.figures:
            self.__sum__ += 10
        elif card[0:2] == '10':
            self.__sum__ += 10
        else:
            self.__sum__ += int(card[0])
        return True

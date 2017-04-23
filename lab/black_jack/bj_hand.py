'''
@author: rafalo

Black Jack Hand class
'''

from bj_cards import BJCards

class BJHand(object):
    '''
    Black Jack Hand class
    '''
    def __init__(self):
        self.__sum__ = 0
        self.__as__ = 0

    def reset(self):
        '''
        Reset hand
        '''
        self.__sum__ = 0
        self.__as__ = 0

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
            pass
        elif card[0] in BJCards.figures:
            self.__sum__ += 10
        elif card[0:2] == '10':
            self.__sum__ += 10
        else:
            self.__sum__ += int(card[0])
        return True

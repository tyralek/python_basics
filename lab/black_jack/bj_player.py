'''
@author: rafalo

Player class
'''

class BJPlayer(object):
    '''
    Black Jack Player class
    '''
    def __init__(self, capital):
        self.__capial__ = capital
        self.__bet__ = 0
#        self.__hand__ = BJHand()

    def bet(self, amount):
        '''
        Player bets a certain amount of money
        :param amount: amount of bet
        :type amount: Integer
        '''
        if amount > self.__capial__:
            return False
        self.__bet__ = amount
        self.__capial__ -= amount
        return True

    def win(self, amount):
        '''
        Player win the bet
        :param amount: amount which was won
        :type amount: Integer
        '''
        self.__capial__ += amount

    @property
    def capital(self):
        '''
        capital getter
        '''
        return self.__capial__

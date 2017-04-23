'''
@author: rozieblo

Black Jack cards class test
'''
import unittest
import random
from bj_cards import BJCards

class Test(unittest.TestCase):

    def setUp(self):
        random.seed()
        self.__suit__ = \
            ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', \
            'Jc', 'Qc', 'Kc', 'Ac', \
            '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', \
            'Js', 'Qs', 'Ks', 'As', \
            '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', \
            'Jh', 'Qh', 'Kh', 'Ah', \
            '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', \
            'Jd', 'Qd', 'Kd', 'Ad']

    def tearDown(self):
        pass

    def test_init(self):
        uut_cards = BJCards()
        self.assertEqual(uut_cards.cards_in_deck, 52)

    def test_reset(self):
        uut_cards = BJCards()
        take = random.randint(1, uut_cards.cards_in_deck)
        for _ in range(take):
            uut_cards.get()
        uut_cards.reset()
        self.assertEqual(uut_cards.cards_in_deck, 52)

    def test_get_all(self):
        uut_cards = BJCards()
        for i in range(uut_cards.cards_in_deck):
            uut_cards.get()
            self.assertEqual(uut_cards.cards_in_deck, 52 - i - 1)
        self.assertEqual(uut_cards.cards_in_deck, 0)
        self.assertEqual(uut_cards.get(), None)

    def test_get(self):
        uut_cards = BJCards()
        for _ in range(uut_cards.cards_in_deck):
            card = uut_cards.get()
            self.assertTrue(card in self.__suit__)
            self.__suit__.pop(self.__suit__.index(card))
        self.assertEqual(len(self.__suit__), 0)

    def test_is_card(self):
        BJCards.is_card('card')
        for card in self.__suit__:
            self.assertTrue(BJCards.is_card(card))
        self.assertFalse(BJCards.is_card('1s'))
        self.assertFalse(BJCards.is_card('0d'))
        self.assertFalse(BJCards.is_card('2v'))
        self.assertFalse(BJCards.is_card('Kv'))
        self.assertFalse(BJCards.is_card('Aw'))
        self.assertFalse(BJCards.is_card('As1'))
        self.assertFalse(BJCards.is_card('10'))
        self.assertFalse(BJCards.is_card('10p'))
        self.assertFalse(BJCards.is_card('Jss'))
        self.assertFalse(BJCards.is_card('K'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

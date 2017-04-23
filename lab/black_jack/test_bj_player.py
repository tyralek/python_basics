'''
@author: rozieblo

Black Jack player class test
'''
import unittest
from bj_player import BJPlayer

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        uut_player = BJPlayer(100)
        self.assertEqual(uut_player.capital, 100)

    def test_win(self):
        uut_player = BJPlayer(100)
        uut_player.win(25)
        self.assertEqual(uut_player.capital, 125)

    def test_bet(self):
        uut_player = BJPlayer(100)
        self.assertFalse(uut_player.bet(101))
        self.assertTrue(uut_player.bet(100))
        self.assertEqual(uut_player.capital, 0)
        self.assertFalse(uut_player.bet(1))
        self.assertEqual(uut_player.capital, 0)
        uut_player = BJPlayer(100)
        self.assertTrue(uut_player.bet(48))
        self.assertEqual(uut_player.capital, 52)
        self.assertFalse(uut_player.bet(100))
        self.assertTrue(uut_player.bet(48))
        self.assertEqual(uut_player.capital, 4)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

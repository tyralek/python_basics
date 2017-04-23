'''
@author: rozieblo

Black Jack hand class test
'''
import unittest
from bj_hand import BJHand

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        uut_hand = BJHand()
        self.assertEqual(uut_hand.sum, 0)

    def test_reset(self):
        uut_hand = BJHand()
        uut_hand.add_card('5c')
        self.assertNotEqual(uut_hand.sum, 0)
        uut_hand.reset()
        self.assertEqual(uut_hand.sum, 0)

    def test_add_card(self):
        uut_hand = BJHand()
        self.assertTrue(uut_hand.add_card('2s'))
        self.assertEqual(uut_hand.sum, 2)
        self.assertTrue(uut_hand.add_card('3s'))
        self.assertEqual(uut_hand.sum, 5)
        self.assertTrue(uut_hand.add_card('5h'))
        self.assertEqual(uut_hand.sum, 10)
        self.assertTrue(uut_hand.add_card('9d'))
        self.assertEqual(uut_hand.sum, 19)
        self.assertFalse(uut_hand.add_card('wd'))
        self.assertEqual(uut_hand.sum, 19)
        self.assertFalse(uut_hand.add_card('1d'))
        self.assertEqual(uut_hand.sum, 19)
        self.assertTrue(uut_hand.add_card('7d'))
        self.assertEqual(uut_hand.sum, 26)
        self.assertFalse(uut_hand.add_card('3c'))
        self.assertEqual(uut_hand.sum, 26)
        uut_hand.reset()
        self.assertTrue(uut_hand.add_card('10s'))
        self.assertEqual(uut_hand.sum, 10)
        self.assertTrue(uut_hand.add_card('Ks'))
        self.assertEqual(uut_hand.sum, 20)
        self.assertTrue(uut_hand.add_card('10s'))
        self.assertEqual(uut_hand.sum, 30)
        uut_hand.reset()
        self.assertTrue(uut_hand.add_card('As'))
        self.assertEqual(uut_hand.sum, 10)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

'''
@author: rozieblo

Tic tac toe test
'''
import unittest
from tic_tac_toe import tic_tac_toe

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ttt_put(self):
        ttt = tic_tac_toe()
        self.assertEqual(ttt.board, [[0,0,0],[0,0,0],[0,0,0]])
        ttt.put('b2')
        self.assertEqual(ttt.board, [[0,0,0],[0,'x',0],[0,0,0]])
        ttt.put('a1')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],[0,0,0]])
        ttt.put('c3')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],[0,0,'x']])
        ttt.put('a3')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        ttt.put('d1')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        ttt.put('a1')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        ttt.put('a1')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        ttt.put('b2')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        ttt.put('a0')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        ttt.put('3')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],['o',0,'x']])
        pass

    def test_ttt_clear(self):
        ttt = tic_tac_toe()
        self.assertEqual(ttt.board, [[0,0,0],[0,0,0],[0,0,0]])
        ttt.put('b2')
        self.assertEqual(ttt.board, [[0,0,0],[0,'x',0],[0,0,0]])
        ttt.put('a1')
        self.assertEqual(ttt.board, [['o',0,0],[0,'x',0],[0,0,0]])
        ttt.clear()
        self.assertEqual(ttt.board, [[0,0,0],[0,0,0],[0,0,0]])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

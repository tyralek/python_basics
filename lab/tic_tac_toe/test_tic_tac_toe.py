'''
@author: rozieblo

Tic tac toe test
'''
import unittest
from tic_tac_toe import TicTacToe


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ttt_put(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(ttt.now_move(), 'x')
        self.assertTrue(ttt.put('b2'))
        self.assertEqual(ttt.now_move(), 'o')
        self.assertEqual(ttt.board, [[0, 0, 0], [0, 'x', 0], [0, 0, 0]])
        self.assertTrue(ttt.put('a1'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], [0, 0, 0]])
        self.assertTrue(ttt.put('c3'))
        self.assertEqual(ttt.now_move(), 'o')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], [0, 0, 'x']])
        self.assertTrue(ttt.put('a3'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])
        self.assertFalse(ttt.put('d1'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])
        self.assertFalse(ttt.put('a1'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])
        self.assertFalse(ttt.put('a1'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])
        self.assertFalse(ttt.put('b2'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])
        self.assertFalse(ttt.put('a0'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])
        self.assertFalse(ttt.put('3'))
        self.assertEqual(ttt.now_move(), 'x')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], ['o', 0, 'x']])

    def test_ttt_clear(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        ttt.put('b2')
        self.assertEqual(ttt.board, [[0, 0, 0], [0, 'x', 0], [0, 0, 0]])
        ttt.put('a1')
        self.assertEqual(ttt.board, [['o', 0, 0], [0, 'x', 0], [0, 0, 0]])
        ttt.clear()
        self.assertEqual(ttt.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_ttt_winner_x_column(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c3')
        self.assertEqual(ttt.winner_is(), 'x')
        self.assertFalse(ttt.put('b3'))
        self.assertEqual(ttt.winner_is(), 'x')
        self.assertEqual(ttt.board, [[0, 'o', 'x'], \
                         [0, 'o', 'x'], [0, 0, 'x']])

    def test_ttt_winner_x_row(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b2')
        self.assertEqual(ttt.winner_is(), 'x')
        self.assertFalse(ttt.put('a1'))
        self.assertEqual(ttt.winner_is(), 'x')
        self.assertEqual(ttt.board, [[0, 'o', 'o'], \
                         ['x', 'x', 'x'], [0, 0, 0]])

    def test_ttt_winner_x_diagonal(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c3')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a1')
        self.assertEqual(ttt.winner_is(), 'x')
        self.assertFalse(ttt.put('a1'))
        self.assertEqual(ttt.winner_is(), 'x')
        self.assertEqual(
            ttt.board, [['x', 'o', 'o'], [0, 'x', 0], [0, 0, 'x']])

    def test_ttt_winner_o_column(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a3')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b3')
        self.assertEqual(ttt.winner_is(), 'o')
        self.assertFalse(ttt.put('a2'))
        self.assertEqual(ttt.winner_is(), 'o')
        self.assertEqual(ttt.board, [['x', 'o', 'x'], \
                         [0, 'o', 0], ['x', 'o', 0]])

    def test_ttt_winner_o_row(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c3')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a2')
        self.assertEqual(ttt.winner_is(), 'o')
        self.assertFalse(ttt.put('b1'))
        self.assertEqual(ttt.winner_is(), 'o')
        self.assertEqual(ttt.board, [['x', 0, 'x'], \
                         ['o', 'o', 'o'], [0, 0, 'x']])

    def test_ttt_winner_o_diagonal(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a3')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('a1')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('b2')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c3')
        self.assertEqual(ttt.winner_is(), 0)
        ttt.put('c1')
        self.assertEqual(ttt.winner_is(), 'o')
        self.assertFalse(ttt.put('a1'))
        self.assertEqual(ttt.winner_is(), 'o')
        self.assertEqual(ttt.board, [['x', 0, 'o'], \
                         ['x', 'o', 0], ['o', 0, 'x']])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

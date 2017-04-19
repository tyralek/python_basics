'''
@author: rozieblo

Tic tac toe class
'''


class TicTacToe:
    '''
    Tic tac toe class
    '''
    def __init__(self):
        self.__x = 0
        self.__winner = 0
        self.clear()

    @property
    def board(self):
        '''
        Get board.
        '''
        return self.__board

    @staticmethod
    def __letter_to_column(letter):
        return ord(letter) - ord('a')

    @staticmethod
    def __number_to_row(number):
        return ord(number) - ord('1')

    def put(self, field):
        '''
        put 'x' or 'o' to the board
        '''
        if field[0] not in 'abc':
            return False
        if field[1] not in '123':
            return False
        if self.__winner != 0:
            return False

        column = self.__letter_to_column(field[0])
        row = self.__number_to_row(field[1])
        if self.__board[row][column] != 0:
            return False
        if self.__x == 1:
            put = 'x'
            self.__x = 0
        else:
            put = 'o'
            self.__x = 1
        self.__board[row][column] = put

        # check winner
        self.__winner = self.__check_column(column)
        if self.__winner == 0:
            self.__winner = self.__check_row(row)
        if self.__winner == 0:
            self.__winner = self.__check_diagonal()
        return True

    def __check_column(self, column):
        col = list(set([row[column] for row in self.__board]))
        if len(col) == 1 and col[0] != 0:
            return col[0]
        return 0

    def __check_row(self, row):
        set_row = list(set(self.__board[row]))
        if len(set_row) == 1 and set_row[0] != 0:
            return set_row[0]
        return 0

    def __check_diagonal(self):
        diag1 = list(set([self.__board[i][i] for i in range(3)]))
        diag2 = list(set([self.__board[i][2 - i] for i in range(3)]))

        if len(diag1) == 1 and diag1[0] != 0:
            return diag1[0]
        if len(diag2) == 1 and diag2[0] != 0:
            return diag2[0]
        return 0

    def clear(self):
        '''
        Clear board and all markers. Reset game.
        '''
        self.__board = [[0 for _ in range(3)] for _ in range(3)]
        self.__winner = 0
        self.__x = 1

    def winner_is(self):
        '''
        Who is the winner.
        '''
        return self.__winner

    def now_move(self):
        '''
        Whos move is now.
        '''
        if self.__x == 0:
            return 'o'
        return 'x'


class Display:
    '''
    Display class, it shows current game status.
    '''
    def __init__(self):
        self.__display = \
            "  a   b   c\n" \
            "1   |   |  \n" \
            " -----------\n" \
            "2   |   |  \n" \
            " -----------\n" \
            "3   |   |  \n"

    def __show_ttt(self, ttt):
        disp = list(self.__display)
        for row in range(3):
            for col in range(3):
                if ttt.board[col][row] != 0:
                    disp[col * 25 + row * 4 + 14] = ttt.board[col][row]
        print(''.join(disp))

    def show(self, tic_tac_toe = None):
        '''
        Show current game status.
        :param tic_tac_toe: TicTacToe object to show or 0 for empty board
        :type tic_tac_toe: TicTacToe or None
        '''
        if tic_tac_toe:
            self.__show_ttt(tic_tac_toe)
        else:
            print(self.__display)

def main():
    '''
    main function for game.
    '''
    my_ttt = TicTacToe()
    my_display = Display()
    my_display.show()
    move_cnt = 0
    while my_ttt.winner_is() == 0 and move_cnt < 9:
        move = input(
            "Choose move for {} (a1 - c3): ".format(my_ttt.now_move()))
        print("\n")
        if my_ttt.put(move):
            my_display.show(my_ttt)
            move_cnt += 1
        else:
            print("You can't put {} in {}\n".format(move, my_ttt.now_move()))
    if my_ttt.winner_is():
        print("The winner is: {}\n".format(my_ttt.winner_is()))
    else:
        print("No one is the winner.\n")

if __name__ == "__main__":
    main()

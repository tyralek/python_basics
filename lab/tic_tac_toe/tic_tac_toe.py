'''
@author: rozieblo

Tic tac toe class
'''

class tic_tac_toe:
    def __init__(self):
        self.__board = [[0 for x in range(3)] for y in range(3)]
        self.__x = 1

    @property
    def board(self):
        return self.__board

    def put(self, field):
        if field[0] not in 'abc':
            return False
        if field[1] not in '123':
            return False
        column = ord(field[0]) - 97
        row = ord(field[1]) - 49
        if self.__x == 1:
            put = 'x'
            self.__x = 0
        else:
            put = 'o'
            self.__x = 1
        if self.__board[row][column] == 0:
            self.__board[row][column] = put

    def clear(self):
        self.__board = [[0 for x in range(3)] for y in range(3)]
        pass

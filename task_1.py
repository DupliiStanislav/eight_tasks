import argparse
import sys


class Chessboard:

    """Create a class to init our Chessboard"""

    def __init__(self, rows=None, cols=None):
        self.rows = rows
        self.cols = cols

    # create our board by rows and cols
    def create_board(self):

        chessboard = []
        for row in range(self.rows):
            inner = []
            for col in range(self.cols):
                inner.append('*')
            chessboard.append(inner)
        return chessboard

    # Show our board
    def show_board(self):

        for e, row in enumerate(self.create_board()):
            if e % 2 == 0:
                print(' ' + ''.join([f'{el:^3}' for el in row]))
            else:
                print(''.join([f'{el:^3}' for el in row]))


def is_valid(value):
    """Validation functions to check if args exist, positive and integers"""
    val = int(value)
    if val < 0:
        print('In this program we can create a chess board '
              'to do this u should use positive numbers as integers')
        raise argparse.ArgumentError
    return val


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Create chess board with two arguments rows and cols', exit_on_error=False)
        parser.add_argument('rows', type=is_valid, help='Rows number')
        parser.add_argument('cols', type=is_valid, help='Cols number')
        args = parser.parse_args()
        chessboard = Chessboard(args.rows, args.cols)
        chessboard.show_board()
    except argparse.ArgumentError:
        exc = sys.exc_info()[1]
        print(f'Use positive integer numbers, instead of: {exc}')


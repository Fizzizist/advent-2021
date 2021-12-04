import sys
from typing import List


class Board:

    def __init__(self, values: List[List[int]]):
        self.marked = [[False for _ in range(5)] for _ in range(5)]
        self.values = values

    def mark(self, num):
        for i in range(5):
            for j in range(5):
                if self.values[i][j] == num:
                    self.marked[i][j] = True
    
    def check_winner(self):
        # Check all horizontal rows
        if any([all(_list) for _list in self.marked]):
            return True

        # Check vertical rows
        for i in range(5):
            if all([self.marked[j][i] for j in range(5)]):
                return True

        # Check diagonal
        #if all([self.marked[i][i] for i in range(5)]):
         #   return True
        #if all([self.marked[i][j] for i, j in zip((i for i in range(5)), (j for j in reversed(range(5))))]):
         #   return True

    def get_total_unmarked(self):
        total = 0
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    total += self.values[i][j]
        return total

    def print_marked(self):
        print('\n')
        for i in self.marked:
            print(i)
        print('\n')

    def print_values(self):
        print('\n')
        for i in self.values:
            print(i)
        print('\n')


def _get_board(lines) -> Board:
    values = []
    for line in lines:
        vals = line.split(' ')
        while len(vals) != 5:
            vals.remove('')
        values.append([int(val) for val in vals])
    return Board(values)

def main():
    with open(sys.argv[1]) as f:
        nums = [int(num) for num in f.readline().strip().split(',')]
        f.readline()  # get rid of \n between nums and first board
        new_board = []
        boards = []
        for line in f.readlines():
            if line == '\n':
                boards.append(_get_board(new_board))
                new_board = []
            else:
                new_board.append(line.strip())

    for num in nums:
        for board in boards:
            board.print_marked()
            board.print_values()
            print(num)
            board.mark(num)
            if board.check_winner():
                print(board.get_total_unmarked() * num)
                return

main()

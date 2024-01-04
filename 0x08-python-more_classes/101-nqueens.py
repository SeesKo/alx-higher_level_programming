#!/usr/bin/python3
import sys


class ChessboardSolver:
    def __init__(self, board_size):
        self.board_size = board_size
        self.solutions = []

    def can_place_queen(self, row, col, placement):
        for prev_row in range(row):
            if placement[prev_row] == col or \
                    abs(placement[prev_row] - col) == (row - prev_row):
                return False
        return True

    def find_solutions(self, current_row, placement):
        if current_row == self.board_size:
            self.solutions.append(placement.copy())
            return

        for current_col in range(self.board_size):
            if self.can_place_queen(current_row, current_col, placement):
                placement[current_row] = current_col
                self.find_solutions(current_row + 1, placement)


def print_solution(solution):
    for col in solution:
        print("[{}, {}]".format(solution.index(col), col), end="")
        if col != solution[-1]:
            print(", ", end="")
    print()


if __name__ == "__main__":
    argument_count = len(sys.argv)

    if argument_count != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        try:
            board_size = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver_instance = ChessboardSolver(board_size)
    solver_instance.find_solutions(0, [None for _ in range(board_size)])

    for solution in solver_instance.solutions:
        print_solution(solution)

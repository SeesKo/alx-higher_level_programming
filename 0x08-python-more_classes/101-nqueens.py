#!/usr/bin/python3

"""Solves the N queens problem."""

import sys


class Queen:
    """
    Queen class represents the N-Queens problem solver.
    """

    def __init__(self, n):
        """
        Initializes a Queen object.

        Raises:
            ValueError: If N is not a positive integer or is less than 4.
        """
        if not isinstance(n, int) or n < 4:
            raise ValueError("N must be a positive integer and at least 4")
        self.n = n

    def is_safe(self, board, row, col):
        """
        Check if placing a queen at a specific position
        (row, col) on the board is safe.

        Returns:
            bool: True if the placement is safe, False otherwise.
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve_nqueens_util(self, board, row, solutions):
        """
        Recursively solve the N-Queens problem for each row.
        """
        if row == self.n:
            solutions.append([(i, board[i]) for i in range(self.n)])
            return

        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve_nqueens_util(board, row + 1, solutions)

    def solve_nqueens(self):
        """
        Solve the N-Queens problem and return the solutions.
        """
        board = [-1] * self.n
        solutions = []
        self.solve_nqueens_util(board, 0, solutions)
        return solutions


if __name__ == "__main__":
    """
    Parse command-line arguments and create a Queen object.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        queen = Queen(int(sys.argv[1]))
        solutions = queen.solve_nqueens()
        for solution in solutions:
            print(solution)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

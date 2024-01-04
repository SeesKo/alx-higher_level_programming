#!/usr/bin/python3

"""Solves the N queens problem."""

import sys


def is_safe(board, row, col, n):
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


def solve_nqueens_util(board, row, n):
    """
    Recursively solve the N-Queens problem for each row.
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)


def solve_nqueens(n):
    """
    Solve the N-Queens problem and print the solutions.

    Raises:
        ValueError: If N is not a positive integer.
    """
    if not n.isdigit():
        raise ValueError("N must be a positive integer")

    n = int(n)
    if n < 4:
        raise ValueError("N must be at least 4")

    board = [-1] * n
    solve_nqueens_util(board, 0, n)


if __name__ == "__main__":
    """
    Parsing command-line arguments and call the solve_nqueens function.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        solve_nqueens(sys.argv[1])
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

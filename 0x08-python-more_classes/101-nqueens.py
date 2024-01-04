#!/usr/bin/python3
"""Solves the N queens problem"""


import sys


def is_valid(board, row, col):
    """
    Checks if a queen can be placed at (row, col)
    without attacking other queens.
    """
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
    return True


def solve_n_queens(n, board, row):
    """Recursively solves the N-queens problem."""
    if row == n:
        print(" ".join(map(str, board)))  # Print the solution
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_n_queens(n, board, row + 1)


def main():
    """Main function to handle input and call the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n  # Initialize the board with -1s
    solve_n_queens(n, board, 0)


if __name__ == "__main__":
    main()

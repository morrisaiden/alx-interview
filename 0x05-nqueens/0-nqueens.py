#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed on the board at position (row, col).
    A queen cannot be placed if it attacks another queen diagonally
    or vertically.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N, solutions):
    """
    Solve the N Queens problem using backtracking.
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_nqueens(board, col + 1, N, solutions)

            board[i][col] = 0


def nqueens(N):
    """
    Solve the N Queens problem and print all solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    solutions.sort()

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)

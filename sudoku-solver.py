# Sudoku Solver using Backtracking
def print_board(board):
    """Utility function to print the board."""
    for row in board:
        print(" ".join(str(num) for num in row))


def is_valid(board, row, col, num):
    """Check if placing num at board[row][col] is valid."""
    # Check if num is not in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if num is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if num is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty(board):
    """Find an empty space on the board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Empty cells are represented by 0
                return i, j
    return None


def solve_sudoku(board):
    """Solve the Sudoku board using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Solved if no empty spaces are found
    row, col = empty

    for num in range(1, 10):  # Try numbers 1 through 9
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If placing num doesn't lead to a solution, reset the cell (backtrack)
            board[row][col] = 0

    return False


# Example Sudoku puzzle (0s represent empty spaces)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists.")
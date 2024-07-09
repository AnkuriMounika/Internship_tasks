def is_valid(board, row, col, num):
    # Check if placing 'num' in board[row][col] is valid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    # Solve the Sudoku using backtracking
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    # Print the Sudoku board in a readable format
    for row in board:
        print(" ".join(str(num) for num in row))

if __name__ == "__main__":
    # Initialize an empty 9x9 Sudoku board
    sudoku_board = [[0] * 9 for _ in range(9)]

    print("Enter the Sudoku board row by row:")
    for i in range(9):
        while True:
            row = input(f"Enter numbers for row {i+1} separated by spaces: ").strip()
            try:
                sudoku_board[i] = list(map(int, row.split()))
                if len(sudoku_board[i]) != 9:
                    raise ValueError("Please enter exactly 9 numbers.")
                break
            except ValueError as e:
                print(e)

    print("\nOriginal Sudoku Board:")
    print_board(sudoku_board)
    
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")

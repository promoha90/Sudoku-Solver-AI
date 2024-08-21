class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        def format_number(num):
            if num == 0:
                return ' * '
            else:
                return f' {num} '

        board_str, ASCII_art = '', ('+'+('-'*11))
        for row in self.board:
            # Add top border
            
            board_str += ASCII_art * 3 + '+\n'
            # Add the row of numbers
            row_str = '|' + '|'.join(format_number(num) for num in row) + '|\n'
            board_str += row_str
        # Add bottom border
        board_str += ASCII_art * 3 + '+\n'
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

def main():
    # Prompt the user for input
    board = parse_board()
    solve_sudoku(board)

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'\nSudoku to solve:\n{gameboard}')
    
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

def parse_board():
    # Prompts the user to input the Sudoku board row by row and converts it into a list of lists.
    board = []
    print("Enter each row of the Sudoku puzzle, using spaces to separate numbers. Use '0' for empty cells.")
    for i in range(9):
        while True:
            try:
                line = input(f"Row {i + 1}: ")
                row = list(map(int, line.split()))

                for num in row:
                    if num < 0 or num > 9:
                        raise ValueError("Each number must contain exactly 1 positive integer value")
                    
                if len(row) != 9:
                    raise ValueError("Each row must contain exactly 9 numbers")
                
                board.append(row)
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter the row again.")
                
    return board

if __name__ == "__main__":
    main()
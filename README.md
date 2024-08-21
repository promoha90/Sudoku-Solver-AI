# Sudoku Solver

This project is a simple yet powerful Sudoku solver implemented in Python. The program can take an incomplete Sudoku puzzle as input, solve it using a backtracking algorithm, and display the completed board.

## How Does the Backtracking Algorithm Work?

The backtracking algorithm is a problem-solving technique used to find solutions by incrementally building a solution, step by step. If at any point it is determined that a partial solution cannot lead to a complete solution, the algorithm "backs up" and tries a different solution.

For Sudoku, the backtracking algorithm attempts to fill the empty cells as follows:

1. **Searching for Empty Cells:**
   - The algorithm scans the board for the first empty cell (i.e., a cell containing a 0).

2. **Trying a Valid Number:**
   - Once an empty cell is found, the algorithm tries placing a number between 1 and 9 in that cell.
   - For each number, it checks if the number adheres to Sudoku rules:
     - It should not repeat in the same row.
     - It should not repeat in the same column.
     - It should not repeat in the same 3x3 subgrid.

3. **Recursion:**
   - If the number is valid, the algorithm places that number in the cell and then moves to the next empty cell.
   - This process is repeated recursively until the entire board is filled or it is determined that no valid solution can be found with the current number.

4. **Backtracking:**
   - If at any point the algorithm finds that it is not possible to place any number in a cell without violating Sudoku rules, it backtracks to the previous step.
   - This backtracking involves removing the previous number placed in a cell and trying the next possible number.
   - This trial-and-error process continues until a complete solution is found or it is determined that no solution is possible with the given initial configuration.

### Advantages of the Backtracking Algorithm
- **Simplicity:** Easy to understand and implement.
- **Flexibility:** Works for a variety of decision and optimization problems.
- **Completeness:** Guarantees finding a solution if one exists, as it explores all possibilities.

### Disadvantages
- **Efficiency:** Can be inefficient for very large or complex problems, as it may require exploring many possibilities.

In summary, the backtracking algorithm is a powerful tool for solving Sudoku puzzles, as it systematically tries different combinations of numbers to find the correct solution. This project implements this algorithm to automatically solve any valid Sudoku board.

## Project Files

### `sudoku_solver.py`
This file contains the primary logic of the Sudoku solver, divided into several components:

- **Board Class:**
  - `__init__` method: Initializes the board with a 2D list representing the Sudoku grid.
  - `__str__` method: Converts the board into a string format for easy display, where empty cells are represented by asterisks (*).
  - `find_empty_cell` method: Scans the board to find the first empty cell (represented by a 0).
  - `valid_in_row`, `valid_in_col`, `valid_in_square` methods: Check whether a given number can be placed in a specified row, column, or 3x3 square without violating Sudoku rules.
  - `is_valid` method: Combines the row, column, and square checks to validate a possible number placement.
  - `solver` method: Implements the backtracking algorithm to solve the Sudoku puzzle. It recursively tries different numbers in empty cells, backtracking if a conflict is found.

- **`main()` Function:**
  - The `main()` function is the entry point of the program. It prompts the user to input a Sudoku puzzle row by row, creates a Board object, and then calls the solver to solve the puzzle. The solved puzzle (or a message indicating that the puzzle is unsolvable) is then displayed to the user.

- **`parse_board()` Function:**
  - This function handles user input, ensuring that the Sudoku puzzle is correctly formatted before passing it to the solver. It prompts users to input each row of the puzzle, checks for valid input, and handles errors appropriately.

### `test_sudoku_solver.py`
This file includes unit tests for the Board class. These tests are designed to ensure the correctness and robustness of the implemented methods:

- `test_board_str()`: Verifies the string representation of the Board object, ensuring that it formats the Sudoku board correctly for display.
- `test_find_empty_cell()`: Tests the `find_empty_cell` method to ensure it accurately identifies the first empty cell in the board.
- `test_valid_in_row()`: Ensures that the `valid_in_row` method correctly identifies whether a number can be placed in a given row.
- `test_valid_in_col()`: Tests the `valid_in_col` method for checking valid placements in a specific column.
- `test_valid_in_square()`: Verifies the `valid_in_square` method's accuracy in checking the validity of a number within a 3x3 subgrid.
- `test_is_valid()`: Combines the individual checks for rows, columns, and squares to ensure the overall validity check (`is_valid`) functions as expected.
- `test_solver()`: This test checks whether the backtracking solver correctly solves a sample Sudoku puzzle, comparing the output with the expected solution.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Clone this repository.
3. Navigate to the project directory in your terminal.
4. Run `python sudoku_solver.py` to start the Sudoku solver.
5. Use `pytest` to run tests in `test_sudoku_solver.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
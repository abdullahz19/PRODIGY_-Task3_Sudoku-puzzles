"""
Sudoku Solver using Backtracking Algorithm
Solves Sudoku puzzles automatically by exploring possible solutions
and finding the correct arrangement of numbers.
"""


class SudokuSolver:
    """
    A class to solve Sudoku puzzles using the backtracking algorithm.
    
    The board is represented as a 9x9 2D list where 0 represents empty cells.
    """
    
    def __init__(self, board):
        """
        Initialize the solver with a Sudoku board.
        
        Args:
            board: 9x9 2D list where 0 represents empty cells
        """
        self.board = [row[:] for row in board]  # Create a copy of the board
        self.original_board = [row[:] for row in board]  # Keep original for reference
    
    def is_valid(self, row, col, num):
        """
        Check if placing a number at (row, col) is valid.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)
            
        Returns:
            True if the placement is valid, False otherwise
        """
        # Check row constraint
        if num in self.board[row]:
            return False
        
        # Check column constraint
        if num in [self.board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box constraint
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        
        return True
    
    def find_empty(self):
        """
        Find the next empty cell in the board.
        
        Returns:
            Tuple (row, col) of the first empty cell, or None if no empty cells
        """
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None
    
    def solve(self):
        """
        Solve the Sudoku puzzle using backtracking.
        
        Returns:
            True if the puzzle is solved, False if no solution exists
        """
        empty = self.find_empty()
        
        # Base case: no empty cells left, puzzle is solved
        if empty is None:
            return True
        
        row, col = empty
        
        # Try each number from 1 to 9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                # Place the number
                self.board[row][col] = num
                
                # Recursively try to solve the rest of the puzzle
                if self.solve():
                    return True
                
                # Backtrack: remove the number and try the next one
                self.board[row][col] = 0
        
        # No valid number found, backtrack further
        return False
    
    def get_solution(self):
        """
        Get the solved board.
        
        Returns:
            9x9 2D list representing the solved Sudoku puzzle
        """
        return self.board
    
    def is_solved(self):
        """
        Check if the puzzle is completely solved.
        
        Returns:
            True if all cells are filled, False otherwise
        """
        for row in self.board:
            if 0 in row:
                return False
        return True
    
    def display(self, board=None):
        """
        Display the Sudoku board in a readable format.
        
        Args:
            board: Optional board to display. If None, displays current board.
        """
        if board is None:
            board = self.board
        
        print("\n" + "=" * 25)
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 25)
            
            row_str = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                
                if board[i][j] == 0:
                    row_str += ". "
                else:
                    row_str += str(board[i][j]) + " "
            
            print(row_str)
        print("=" * 25 + "\n")
    
    def reset(self):
        """Reset the board to its original state."""
        self.board = [row[:] for row in self.original_board]


def print_comparison(original, solved):
    """
    Display original and solved puzzles side by side.
    
    Args:
        original: Original unsolved board
        solved: Solved board
    """
    print("\n" + "ORIGINAL PUZZLE".center(54) + "\n")
    print_board(original)
    print("\n" + "SOLVED PUZZLE".center(54) + "\n")
    print_board(solved)


def print_board(board):
    """
    Print a Sudoku board in a readable format.
    
    Args:
        board: 9x9 2D list representing the Sudoku board
    """
    print("=" * 25)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            
            if board[i][j] == 0:
                row_str += ". "
            else:
                row_str += str(board[i][j]) + " "
        
        print(row_str)
    print("=" * 25)

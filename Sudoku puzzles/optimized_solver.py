"""
Optimized Sudoku Solver using Backtracking with advanced techniques.
Includes constraint propagation and intelligent cell selection.
"""

from collections import defaultdict


class OptimizedSudokuSolver:
    """
    Advanced Sudoku solver with optimizations:
    - Constraint propagation
    - Minimum Remaining Values (MRV) heuristic
    - Naked singles elimination
    """
    
    def __init__(self, board):
        """Initialize the optimized solver with a Sudoku board."""
        self.board = [row[:] for row in board]
        self.original_board = [row[:] for row in board]
        
        # Initialize possible values for each cell
        self.candidates = [[set() for _ in range(9)] for _ in range(9)]
        self._initialize_candidates()
    
    def _initialize_candidates(self):
        """Initialize possible values for empty cells."""
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    self.candidates[row][col] = set(range(1, 10))
                    # Remove values already in row, column, and box
                    for num in range(1, 10):
                        if not self.is_valid(row, col, num):
                            self.candidates[row][col].discard(num)
                else:
                    self.candidates[row][col] = set()
    
    def is_valid(self, row, col, num):
        """Check if placing a number at (row, col) is valid."""
        # Check row
        if num in self.board[row]:
            return False
        
        # Check column
        if num in [self.board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        
        return True
    
    def find_best_cell(self):
        """
        Find the cell with minimum remaining values (MRV heuristic).
        Returns the cell with the fewest possibilities, which is most constrained.
        
        Returns:
            Tuple (row, col) or None if no empty cells
        """
        min_candidates = 10
        best_cell = None
        
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    num_candidates = len(self.candidates[row][col])
                    
                    if num_candidates == 0:
                        # No valid candidates for this cell - contradiction
                        return (row, col)
                    
                    if num_candidates < min_candidates:
                        min_candidates = num_candidates
                        best_cell = (row, col)
        
        return best_cell
    
    def propagate_constraints(self, row, col, num):
        """
        When a number is placed, remove it from candidates of related cells.
        
        Args:
            row, col: Position of the placed number
            num: The number placed
            
        Returns:
            List of (row, col) cells that had candidates removed
        """
        removed = []
        
        # Remove from row
        for j in range(9):
            if j != col and num in self.candidates[row][j]:
                self.candidates[row][j].remove(num)
                removed.append((row, j))
        
        # Remove from column
        for i in range(9):
            if i != row and num in self.candidates[i][col]:
                self.candidates[i][col].remove(num)
                removed.append((i, col))
        
        # Remove from 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i, j) != (row, col) and num in self.candidates[i][j]:
                    self.candidates[i][j].remove(num)
                    removed.append((i, j))
        
        return removed
    
    def restore_constraints(self, row, col, num, removed):
        """Restore candidates when backtracking."""
        for r, c in removed:
            if r != row or c != col:
                self.candidates[r][c].add(num)
    
    def solve(self):
        """
        Solve using optimized backtracking with constraint propagation.
        
        Returns:
            True if solved, False otherwise
        """
        # Find the best cell (most constrained)
        cell = self.find_best_cell()
        
        if cell is None:
            # No empty cells - puzzle is solved
            return True
        
        row, col = cell
        
        # If a cell has no candidates, there's a contradiction
        if len(self.candidates[row][col]) == 0:
            return False
        
        # Try each candidate value
        for num in list(self.candidates[row][col]):
            # Place the number
            self.board[row][col] = num
            candidates_backup = [row_cands[:] for row_cands in self.candidates]
            candidates_backup = [set() for _ in range(9)]
            for r in range(9):
                candidates_backup[r] = [s.copy() for s in self.candidates[r]]
            
            # Propagate constraints
            removed = self.propagate_constraints(row, col, num)
            self.candidates[row][col] = set()
            
            # Recursively solve
            if self.solve():
                return True
            
            # Backtrack: restore state
            self.board[row][col] = 0
            for r in range(9):
                self.candidates[r] = [s.copy() for s in candidates_backup[r]]
        
        return False
    
    def get_solution(self):
        """Get the solved board."""
        return self.board
    
    def reset(self):
        """Reset to original state."""
        self.board = [row[:] for row in self.original_board]
        self._initialize_candidates()


def compare_solvers():
    """Compare performance of basic vs optimized solver."""
    import time
    from sudoku_solver import SudokuSolver
    
    puzzle = [
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
    
    print("\n" + "=" * 70)
    print("SOLVER PERFORMANCE COMPARISON".center(70))
    print("=" * 70)
    
    # Test basic solver
    print("\n1. BASIC SOLVER (Simple Backtracking)")
    basic_solver = SudokuSolver(puzzle)
    start = time.time()
    basic_solver.solve()
    basic_time = time.time() - start
    print(f"   Time: {basic_time:.4f} seconds")
    
    # Test optimized solver
    print("\n2. OPTIMIZED SOLVER (With Constraint Propagation & MRV)")
    opt_solver = OptimizedSudokuSolver(puzzle)
    start = time.time()
    opt_solver.solve()
    opt_time = time.time() - start
    print(f"   Time: {opt_time:.4f} seconds")
    
    # Summary
    print("\n" + "-" * 70)
    if opt_time > 0:
        speedup = basic_time / opt_time
        print(f"Speedup: {speedup:.2f}x faster with optimizations")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    compare_solvers()

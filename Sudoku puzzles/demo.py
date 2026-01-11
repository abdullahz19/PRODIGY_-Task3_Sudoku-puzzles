"""
Simple demonstration script that directly solves a Sudoku puzzle.
No user interaction required - just run it!
"""

import time
from sudoku_solver import SudokuSolver, print_board
from puzzle_utils import count_empty_cells


def demo():
    """Demonstrate the Sudoku solver with an example puzzle."""
    
    # Example puzzle - Easy level
    # 0 represents empty cells
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
    print("SUDOKU SOLVER DEMONSTRATION".center(70))
    print("=" * 70)
    
    # Display original puzzle
    print(f"\nOriginal puzzle with {count_empty_cells(puzzle)} empty cells:")
    print_board(puzzle)
    
    # Create solver instance
    solver = SudokuSolver(puzzle)
    
    # Solve the puzzle
    print("Solving...")
    start_time = time.time()
    is_solved = solver.solve()
    end_time = time.time()
    
    if is_solved:
        print(f"✓ Puzzle solved in {end_time - start_time:.4f} seconds!\n")
        print("Solved puzzle:")
        print_board(solver.get_solution())
        print("Solution is valid and complete!")
    else:
        print("✗ Could not solve this puzzle!")


if __name__ == "__main__":
    demo()

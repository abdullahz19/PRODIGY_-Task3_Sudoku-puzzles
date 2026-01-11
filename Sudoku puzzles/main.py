"""
Main script to demonstrate the Sudoku Solver.
Run this file to solve example Sudoku puzzles.
"""

import json
import time
from sudoku_solver import SudokuSolver, print_board
from puzzle_utils import (
    validate_puzzle, count_empty_cells, puzzle_to_readable_string
)


def solve_from_examples():
    """Load and solve puzzles from the example puzzles.json file."""
    
    try:
        with open('puzzles.json', 'r') as f:
            puzzles_data = json.load(f)
    except FileNotFoundError:
        print("Error: puzzles.json not found!")
        return
    
    for puzzle_key, puzzle_info in puzzles_data.items():
        if not isinstance(puzzle_info, dict) or 'puzzle' not in puzzle_info:
            continue
        
        puzzle = puzzle_info['puzzle']
        name = puzzle_info.get('name', puzzle_key)
        difficulty = puzzle_info.get('difficulty', 'Unknown')
        
        print("\n" + "=" * 70)
        print(f"Solving: {name} ({difficulty})")
        print("=" * 70)
        
        # Validate the puzzle
        is_valid, msg = validate_puzzle(puzzle)
        if not is_valid:
            print(f"Invalid puzzle: {msg}")
            continue
        
        # Count empty cells
        empty_count = count_empty_cells(puzzle)
        print(f"\nEmpty cells: {empty_count}")
        
        # Display original puzzle
        print("\nORIGINAL PUZZLE:")
        print(puzzle_to_readable_string(puzzle))
        
        # Create solver and solve
        solver = SudokuSolver(puzzle)
        
        start_time = time.time()
        is_solved = solver.solve()
        end_time = time.time()
        
        if is_solved:
            print("✓ PUZZLE SOLVED!")
            print(f"Time taken: {end_time - start_time:.4f} seconds\n")
            print("SOLVED PUZZLE:")
            print(puzzle_to_readable_string(solver.get_solution()))
        else:
            print("✗ No solution found for this puzzle!")


def solve_custom_puzzle():
    """Solve a custom puzzle entered by the user."""
    
    print("\n" + "=" * 70)
    print("CUSTOM PUZZLE SOLVER")
    print("=" * 70)
    print("\nEnter your Sudoku puzzle as an 81-digit string.")
    print("Use 0 for empty cells.")
    print("Example: 530070000600195000098000060800060003400803001700020006060000280000419005900005001\n")
    
    puzzle_str = input("Enter puzzle string: ").strip()
    
    if len(puzzle_str) != 81:
        print("Error: Puzzle string must contain exactly 81 characters!")
        return
    
    # Convert string to board
    try:
        board = []
        for i in range(9):
            row = [int(puzzle_str[i*9 + j]) for j in range(9)]
            board.append(row)
    except ValueError:
        print("Error: Puzzle string must contain only digits!")
        return
    
    # Validate the puzzle
    is_valid, msg = validate_puzzle(board)
    if not is_valid:
        print(f"Invalid puzzle: {msg}")
        return
    
    # Count empty cells
    empty_count = count_empty_cells(board)
    print(f"\nEmpty cells: {empty_count}")
    
    # Display original puzzle
    print("\nORIGINAL PUZZLE:")
    print(puzzle_to_readable_string(board))
    
    # Create solver and solve
    solver = SudokuSolver(board)
    
    start_time = time.time()
    is_solved = solver.solve()
    end_time = time.time()
    
    if is_solved:
        print("✓ PUZZLE SOLVED!")
        print(f"Time taken: {end_time - start_time:.4f} seconds\n")
        print("SOLVED PUZZLE:")
        print(puzzle_to_readable_string(solver.get_solution()))
    else:
        print("✗ No solution found for this puzzle!")


def main():
    """Main menu for the Sudoku Solver."""
    
    print("\n" + "=" * 70)
    print("SUDOKU SOLVER - Backtracking Algorithm".center(70))
    print("=" * 70)
    
    while True:
        print("\nOptions:")
        print("1. Solve example puzzles from puzzles.json")
        print("2. Solve a custom puzzle (enter as string)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            solve_from_examples()
        elif choice == '2':
            solve_custom_puzzle()
        elif choice == '3':
            print("\nThank you for using Sudoku Solver!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

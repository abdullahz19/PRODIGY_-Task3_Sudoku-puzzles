"""
Test suite for Sudoku Solver
Verifies all components work correctly.
"""

import time
from sudoku_solver import SudokuSolver
from puzzle_utils import (
    validate_puzzle, count_empty_cells, 
    load_puzzle_from_string, puzzle_to_string,
    puzzle_to_readable_string
)


def test_basic_puzzle():
    """Test solving a basic puzzle."""
    print("\n" + "=" * 70)
    print("TEST 1: Basic Puzzle Solving".ljust(70))
    print("=" * 70)
    
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
    
    solver = SudokuSolver(puzzle)
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    
    start = time.time()
    is_solved = solver.solve()
    elapsed = time.time() - start
    
    if is_solved and solver.is_solved():
        print(f"✓ PASSED - Solved in {elapsed:.4f} seconds")
        return True
    else:
        print("✗ FAILED - Could not solve puzzle")
        return False


def test_validation():
    """Test puzzle validation."""
    print("\n" + "=" * 70)
    print("TEST 2: Puzzle Validation".ljust(70))
    print("=" * 70)
    
    # Valid puzzle
    valid_puzzle = [[0] * 9 for _ in range(9)]
    valid_puzzle[0][0] = 5
    is_valid, msg = validate_puzzle(valid_puzzle)
    
    if is_valid:
        print("✓ PASSED - Valid puzzle recognized")
    else:
        print(f"✗ FAILED - {msg}")
        return False
    
    # Invalid puzzle (wrong dimensions)
    invalid_puzzle = [[0] * 8 for _ in range(9)]
    is_valid, msg = validate_puzzle(invalid_puzzle)
    
    if not is_valid:
        print("✓ PASSED - Invalid puzzle rejected")
        return True
    else:
        print("✗ FAILED - Invalid puzzle not caught")
        return False


def test_string_conversion():
    """Test puzzle string conversion."""
    print("\n" + "=" * 70)
    print("TEST 3: String Conversion".ljust(70))
    print("=" * 70)
    
    puzzle_str = "530070000600195000098000060800060003400803001700020006060000280000419005900005001"
    
    # Convert to board
    board = load_puzzle_from_string(puzzle_str)
    
    # Convert back to string
    converted_str = puzzle_to_string(board)
    
    if converted_str == puzzle_str:
        print("✓ PASSED - String conversion successful")
        return True
    else:
        print("✗ FAILED - String conversion mismatch")
        print(f"Original:  {puzzle_str}")
        print(f"Converted: {converted_str}")
        return False


def test_puzzle_reset():
    """Test puzzle reset functionality."""
    print("\n" + "=" * 70)
    print("TEST 4: Puzzle Reset".ljust(70))
    print("=" * 70)
    
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
    
    solver = SudokuSolver(puzzle)
    original = [row[:] for row in solver.board]
    
    # Solve it
    solver.solve()
    solved = [row[:] for row in solver.board]
    
    # Reset
    solver.reset()
    reset = [row[:] for row in solver.board]
    
    if reset == original and solved != original:
        print("✓ PASSED - Reset works correctly")
        return True
    else:
        print("✗ FAILED - Reset did not work properly")
        return False


def test_validity_check():
    """Test validity checking function."""
    print("\n" + "=" * 70)
    print("TEST 5: Move Validity Check".ljust(70))
    print("=" * 70)
    
    puzzle = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    solver = SudokuSolver(puzzle)
    
    # 5 is already in first row
    if not solver.is_valid(0, 1, 5):
        print("✓ PASSED - Detects duplicate in row")
    else:
        print("✗ FAILED - Should reject duplicate in row")
        return False
    
    # 5 is already in first column
    if not solver.is_valid(1, 0, 5):
        print("✓ PASSED - Detects duplicate in column")
        return True
    else:
        print("✗ FAILED - Should reject duplicate in column")
        return False


def test_multiple_puzzles():
    """Test solving multiple puzzles."""
    print("\n" + "=" * 70)
    print("TEST 6: Multiple Puzzles".ljust(70))
    print("=" * 70)
    
    puzzles = [
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 3, 5, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 7, 0],
            [7, 0, 0, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 4, 0, 0, 8, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0, 0],
            [0, 8, 4, 0, 0, 0, 0, 0, 0],
            [6, 0, 2, 0, 0, 0, 0, 4, 7]
        ]
    ]
    
    solved_count = 0
    for i, puzzle in enumerate(puzzles):
        solver = SudokuSolver(puzzle)
        if solver.solve():
            solved_count += 1
    
    if solved_count == len(puzzles):
        print(f"✓ PASSED - All {len(puzzles)} puzzles solved")
        return True
    else:
        print(f"✗ FAILED - Only {solved_count}/{len(puzzles)} puzzles solved")
        return False


def run_all_tests():
    """Run all tests and print summary."""
    print("\n" + "=" * 70)
    print("SUDOKU SOLVER - TEST SUITE".center(70))
    print("=" * 70)
    
    tests = [
        ("Basic Puzzle Solving", test_basic_puzzle),
        ("Puzzle Validation", test_validation),
        ("String Conversion", test_string_conversion),
        ("Puzzle Reset", test_puzzle_reset),
        ("Move Validity Check", test_validity_check),
        ("Multiple Puzzles", test_multiple_puzzles),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ EXCEPTION in {test_name}: {str(e)}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY".center(70))
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name.ljust(40)} {status}")
    
    print("=" * 70)
    print(f"Results: {passed}/{total} tests passed".center(70))
    print("=" * 70 + "\n")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)

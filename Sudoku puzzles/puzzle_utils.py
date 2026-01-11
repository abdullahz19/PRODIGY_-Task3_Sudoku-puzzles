"""
Utility functions for Sudoku puzzle input and output handling.
"""

import json
from pathlib import Path


def load_puzzle_from_file(filepath):
    """
    Load a Sudoku puzzle from a JSON file.
    
    Args:
        filepath: Path to the JSON file containing the puzzle
        
    Returns:
        9x9 2D list representing the puzzle
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data['puzzle'] if isinstance(data, dict) else data


def save_puzzle_to_file(puzzle, filepath):
    """
    Save a Sudoku puzzle to a JSON file.
    
    Args:
        puzzle: 9x9 2D list representing the puzzle
        filepath: Path where the puzzle will be saved
    """
    with open(filepath, 'w') as f:
        json.dump({'puzzle': puzzle}, f, indent=2)


def load_puzzle_from_string(puzzle_str):
    """
    Load a Sudoku puzzle from a string representation.
    
    Args:
        puzzle_str: String with 81 digits (0 for empty cells)
        
    Returns:
        9x9 2D list representing the puzzle
    """
    if len(puzzle_str) != 81:
        raise ValueError("Puzzle string must contain exactly 81 characters")
    
    board = []
    for i in range(9):
        row = [int(puzzle_str[i*9 + j]) for j in range(9)]
        board.append(row)
    return board


def puzzle_to_string(puzzle):
    """
    Convert a Sudoku puzzle to a string representation.
    
    Args:
        puzzle: 9x9 2D list representing the puzzle
        
    Returns:
        String with 81 digits
    """
    result = ""
    for row in puzzle:
        result += "".join(str(cell) for cell in row)
    return result


def validate_puzzle(puzzle):
    """
    Validate a Sudoku puzzle format.
    
    Args:
        puzzle: 9x9 2D list to validate
        
    Returns:
        Tuple (is_valid, message)
    """
    if not isinstance(puzzle, list) or len(puzzle) != 9:
        return False, "Puzzle must be a 9x9 grid"
    
    for i, row in enumerate(puzzle):
        if not isinstance(row, list) or len(row) != 9:
            return False, f"Row {i} must have 9 columns"
        
        for j, cell in enumerate(row):
            if not isinstance(cell, int) or cell < 0 or cell > 9:
                return False, f"Cell ({i}, {j}) must be an integer between 0 and 9"
    
    return True, "Valid puzzle format"


def count_empty_cells(puzzle):
    """
    Count the number of empty cells in a puzzle.
    
    Args:
        puzzle: 9x9 2D list
        
    Returns:
        Number of empty cells (0s)
    """
    count = 0
    for row in puzzle:
        count += row.count(0)
    return count


def puzzle_to_readable_string(puzzle):
    """
    Convert puzzle to a readable multi-line string format.
    
    Args:
        puzzle: 9x9 2D list
        
    Returns:
        Readable string representation
    """
    result = "\n" + "=" * 25 + "\n"
    for i in range(9):
        if i % 3 == 0 and i != 0:
            result += "-" * 25 + "\n"
        
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            
            if puzzle[i][j] == 0:
                row_str += ". "
            else:
                row_str += str(puzzle[i][j]) + " "
        
        result += row_str + "\n"
    
    result += "=" * 25 + "\n"
    return result

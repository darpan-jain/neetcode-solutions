"""
Question: https://leetcode.com/problems/valid-sudoku/
"""

import collections
from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    """
    Approach: Check for duplicates in every row, column and 3x3 grid (sub_squares)
    by maintaining a hashset for each row, col and sub-square.

    Time Complexity: O(9^2) = O(81) i.e. the size of the 9x9 board
    """

    # Hashset to record all values in each row, col and 3x3 sub-square
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)

    # For squares, the key will be the location of the sub-square on the 9x9 board
    # represented by (r//3, c//3) -> using the board's (r, c) and int division by 3,
    # we can find the location of the 3x3 sub-square
    squares = collections.defaultdict(set)

    # Iterate through the board and look for duplicates
    for r in range(9):
        for c in range(9):
            # First check if the current position has a number. If not, skip iteration.
            if board[r][c] == ".":
                continue

            # Now, check if the current element already exists in the hashsets
            # Note the key being used for `squares` -> integer division by 3 to get the sub-square's location
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                return False

            # If current element not a duplicate, add it to the hashsets
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            # Use (r//3, c//3) to find the location of current sub-square
            squares[(r//3, c//3)].add(board[r][c])

    # If not duplicates found in the entire board, it's a Valid Sudoku board!
    return True
    
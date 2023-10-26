"""
Problem Description:
The task is to validate a partially filled 9x9 Sudoku board. The validation needs to ensure:

Each row has unique numbers from 1 to 9.
Each column has unique numbers from 1 to 9.
Each of the nine 3x3 sub-grids (squares) has unique numbers from 1 to 9.

You are only validating the existing numbers and not solving the Sudoku. A valid input Sudoku board may still not have a valid solution.

Potential Approaches:

Brute Force: For every cell, check its row, column, and 3x3 grid for duplicates.
Time Complexity: O(n^3) per cell (n being 9 in this case).
Space Complexity: O(1).

Hashing (as shown in the current code):
Maintain separate hash sets for each row, each column, and each 3x3 grid.
Traverse the board once and fill up these hash sets.
If at any point a number is already present in the corresponding hash set, return false.
Time Complexity: O(n^2) (n being 9 in this case).
Space Complexity: O(n^2) for storing the sets.

Using Bit Manipulation:
Use bits to represent numbers in each row, column, and 3x3 grid.
Set the bit corresponding to a number when it is encountered.
If the bit is already set, there's a duplicate.
Time Complexity: O(n^2).
Space Complexity: O(n^2) for storing the bit-representations.

Explanation of Current Code:
The current code uses the hashing approach with three hash sets for rows, columns, and 3x3 grids.

This approach uses a defaultdict from the collections module to handle rows, columns, and squares separately. 
It checks each number to see if it's already present in its respective row, column, or square. 
If it is, then the Sudoku is not valid. 
Otherwise, it adds the number to the set for that row, column, or square.
"""
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Using defaultdict to initialize sets for each row, column and 3x3 square.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        # Traversing through the entire board.
        for r in range(9):
            for c in range(9):
                # Skip empty cells.
                if board[r][c] == ".":
                    continue

                # If the current number is already in the set for its row, column, or 3x3 square, return False.
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                # Otherwise, add the current number to its row, column, and 3x3 square sets.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If we've traversed the entire board without finding any duplicates, the Sudoku is valid.
        return True

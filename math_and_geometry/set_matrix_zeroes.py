'''
Question: https://leetcode.com/problems/set-matrix-zeroes/
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Approach:
            Use the first row and column to store the information about which rows and columns need to be made zero.

            1. Iterate over the matrix. If the value of the current element is 0, set the first row and column of that element to 0
            2. For the first row, we store a boolean flag to indicate if the first row needs to be made zero. 
                Why? Because the first row and column are used to store the information about which rows and columns need to be made zero, so can't be made zero as we are iterating.
            3. Once the information is stored, we can iterate over the matrix again -  this time to set the decided rows and columns to zero.
            4. Check if value at the origin (0, 0) is 0 and rowZero flag, and set the first column and row to zero respectively. 
    
        Time Complexity: O(3 * (M * N)) = O(M * N) -> since we are iterating over the matrix thrice
        Space Complexity: O(1) -> since we don't use any extra space to store the information about which rows and columns need to be made zero
        """
        
        # Save the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Boolean flag to indicate if the first row needs to be made zero
        rowZero = False
        
        # 1. Iterate over the matrix and if the value of the current element is 0, set the first row and column of that element to 0.
        for r in range(ROWS):
            for c in range(COLS):
                
                # If value of current element is 0, set the first row and column of that element to 0
                if matrix[r][c] == 0:

                    # First column can be set to zero directly
                    matrix[0][c] = 0
                    
                    # 2. Check condition for setting the first value of the row to 0
                    # If not first row, set the first value of that row to 0
                    if r > 0:
                        matrix[r][0] = 0
                    # If first row, set the `rowZero` flag to True
                    else:
                        rowZero = True

        # 3. Now that information is stored, iterate matrix again to actually set the decided rows and columns to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # 4. Also perform checks for the origin value and rowZero flag
        
        # Checking if the origin value is 0
        if matrix[0][0] == 0:
            # If yes, set the entire first column to zero
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # If rowZero flag is True, set the entire first row to zero
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        
        # No return statement, since the question asks to modify the matrix in-place

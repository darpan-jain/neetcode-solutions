'''
Question: https://leetcode.com/problems/spiral-matrix/
'''

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: 
            Maintain 4 pointers to go in a spiral over the matrix:
                - Top, Bottom, Left, Right
                -> Iteration order (clockwise direction):
                    - 1. Get elements from top row (LEFT -> RIGHT)
                    - 2. Get elements from rightmost column (TOP -> BOTTOM)
                    - 3. Get elements from bottom row (RIGHT -> LEFT)
                    - 4. Get elements from leftmost column (BOTTOM -> TOP)
                
                - Move the pointers inwards in a spiral order
                - When the pointers cross each other, stop iterating

        Time complexity: O(M * N),
            where, M = number of rows, N = number of columns -> size of the board / matrix
        Space complexity: O(M * N) -> to store the result of the spiral traversal
        """
        
        res = []
        
        # Top and bottom pointers represent first and last rows of the matrix
        top, bottom = 0, len(matrix)
        # Left and right pointers represent first and last columns of the matrix
        left, right = 0, len(matrix[0])

        # Note: `bottom` and `right` are offset by 1, so we use a `-1` when using them in the loops
        
        # Iterate until the pointers don't cross, i.e., until we reach the middle of the spiral
        while left < right and top < bottom:

            # 1. Get elements from top row (LEFT -> RIGHT)
            for i in range(left, right):
                res.append(matrix[top][i])
            
            # `top` pointer used up, so move down by 1 (increment by 1) for next iteration
            top += 1
            
            # 2. Get elements from rightmost column (TOP -> BOTTOM)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
                
            # `right` pointer used up, so move down by 1 (decrement by 1)
            right -= 1
            
            # Extra Breaking condition for when we input `matrix` as a row or column vector (single row or column)
            if not (left < right and top < bottom):
                break
            
            # 3. Get elements from bottom row (RIGHT -> LEFT, i.e., reverse iteration. Which is why `-1` for both ends of the range)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            
            # `bottom` pointer also used up, so move up by 1 (decrement by 1)
            bottom -= 1
            
            # 4. Finally, get elements from leftmost column (BOTTOM -> TOP i.e. reverse iteration, so also using `-1` in range)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
                
            # Finally, `left` pointer used up, so move right by 1 (increment by 1)
            left += 1
            

        # Final results from spiral traversal of the matrix
        return res

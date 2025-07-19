'''
Question: https://leetcode.com/problems/rotate-image/
'''


from typing import List
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Approach: Move values in counter-clockwise order to rotate matrix by 90 degrees

        Four pointers to parse through the `matrix` -> left, right, top, bottom
            1. Start from top-left, i.e., position (0, 0)
            2. Save the value of top-left in a temp variable
            3. Move value in bottom-left to top-left
            4. Move value in bottom-right to bottom-left
            5. Move value in top-right to bottom-left
            6. Finally, move value in top-left (stored in temp variable) to top-right
        
        Once the edges of the matrix are completed, the four corners are moved inwards 
        to rotate the other values inside. This is done by using a `for loop` that iterates until `r-l`
            - Top-left moves one to the right -> (top, l + i)
            - Bottom-left moves one up -> (bottom - i, l)
            - Bottom-right moves one left -> (bottom, r - i)
            - Top-right moves one down -> (top + i, r)
        
            Tip: To remember where the `i` index is to be applied:
                - If moving up or down -> the `top` or `bottom` pointer changes 
                - If moving left or right -> the `left` or `right` pointer changes

        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """

        # Left and right pointers 
        l, r = 0, len(matrix) - 1

        # Iterate until both pointers don't cross each other
        while l < r:
            
            # Perform rotation for a single layer of values in the matrix
            for i in range(r - l):

                # Top and bottom pointers will be the same as left and right pointers since it's a square matrix
                top, bottom = l, r

                '''
                Start rotating the values in counter-clockwise order.
                Note how we are using index `i` to move inwards in every iteration of the for loop
                '''

                # 1. & 2. Save the topleft so that the value is preserved when rotating values
                topLeft = matrix[top][l + i]

                # 3. Move value in bottom-left to top-left (top-left will move one to the right so (top, l + i))
                matrix[top][l + i] = matrix[bottom - i][l]

                # 4. Move value in bottom-right to bottom-left (bottom-left will move one up so (bottom - i, l))
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # 5. Move value in top-right to bottom-right (bottom-right will move one left so (bottom, r - i))
                matrix[bottom][r - i] = matrix[top + i][r]

                # 6. Move value in top-left (saved in temp variable) to top-right (top-right will move one down so (top + i, r))
                matrix[top + i][r] = topLeft
            
            # Now, since we have completed rotation of outer values, we can move to rotating the inner values
            # by moving the left and right pointers inwards
            r -= 1
            l += 1

    # No return statement, since the question asks to modify the matrix in-place


        """
        Numpy Approaches
        """

        # Single line using in-built numpy function
        matrix[:] = np.rot90(matrix, k=1)

        # Since a matrix transpose is equivalent to a 90 degree rotation, we can:
        matrix[:] = np.transpose(matrix)

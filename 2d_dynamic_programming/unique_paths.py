'''
Question: Unique Paths to reach Finish in a 2D Grid
Link: https://leetcode.com/problems/unique-paths/
'''



class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        """
        Apprach: Traverse bottom-up (DP) towards the starting position, 
                 collecting all possible unique paths at every grid position.
        
        Start at the Finish position, and traverse towards the Start position. 
        At every position `i`, 
            - Can go either Right or Down to get to the finish.
            - The total unique paths at `i` will be the sum of unique paths from Right and Down direction (saved in DP)
            - Traverse till the start position where you have the final result.
        
        Remember that from positions in the last row and last column of the grid, 
        there is only direction to reach finish which is Right in the last row and Down in the last column. 
        These are the boundary conditions / base cases when traversing.
        
        Time-Complexity: O(M * N), since we traverse M rows and N cols (visiting each node once in the grid)
        Space Complexity: O(N) saving the DP for each row
        """

        # The board is a grid of size `m`` rows x `n` cols
        
        # Maintain a 1D DP containing the unique paths of a single row
        # Initialize to all 1s since we start from the last row, where there is 
        # only one direction to get to the Finish i.e., moving Right
        row = [1] * COLS

        # Now we iterate through other rows and update the unique paths to reach Finish for each position
        for i in range(ROWS - 1):

            # The `curr_row` tracks the unique paths in the current row, also init to all 1s
            curr_row = [1] * COLS
            
            '''
            Loop to iterate all elements (in reverse since bottom-up) in `curr_row` and update unique paths values
            Starts with n-2 since the last (rightmost) column of every row has only 
            one path to reach Finish, i.e. Down, so not be considered (similar to the last row where can only move Right to reach Finish)
            '''
            for j in range(COLS - 2, -1, -1):
                # `curr_row` value for unique paths from `j` will be the sum of the values on the right and bottom
                # i.e. new value = right value `(j + 1)` + bottom value `(j)`

                # Now, number of unique paths for each element is the sum of unique paths in the Right `curr_row[j+1]` and Down direction `row[j]`
                # Remember that `row` still contains values of unique paths from the last row (which is below the current row)
                curr_row[j] = curr_row[j+1] + row[j]
            
            # Once all elements in `curr_row` update, update the `row` list for the next iteration
            row = curr_row
            
        # At the end, when traversal through all elements in the grid is completed, 
        # `row` will have unique paths at each element in the topmost row
        # The result will be saved at index 0, i.e. the Start position
        return row[0]

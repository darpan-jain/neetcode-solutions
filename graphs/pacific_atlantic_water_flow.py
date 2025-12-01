'''
Question: https://leetcode.com/problems/pacific-atlantic-water-flow/
'''

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        """
        Approach:

            Iterate from water to inside and check which nodes can do that for
            the two oceans separately. 
            Note that here it means that the previous height should be greater than
            the current height since we are going in reverse (water to land).
        
            Finally, the result will contain nodes that can do it for both oceans,
            i.e. water flow from one ocean to the other!
        
        Time Complexity : O(M * N), where M and N are the number of rows and cols on the grid
        Space Complexity: O(M * N)
        """
        
        ROWS, COLS = len(heights), len(heights[0])
        # Maintain sets for nodes that can reach the Pacific and Atlantic ocean
        pac, atl = set(), set()
        
        # Run DFS on all nodes on the ocean boundaries and check their neighbors using DFS
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or \
                r < 0 or c < 0 or \
                r == ROWS or c == COLS or \
                heights[r][c] < prevHeight):
                return
            
            # Add to visited
            visited.add((r, c))
            
            # Run DFS recursively in all four directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        '''
        Main loop - Run DFS for the boundaries of the two oceans (starting once from all directions)
        Order of searching is important. Start from Right -> Left and then Top -> Bottom (clockwise)
        '''
        
        # Iterate nodes from RIGHT and LEFT (move through columns, in both directions)
        # So, note that ROWS CONSTANT and COLUMNS UPDATE in the for loop (since moving left and right)
        for c in range(COLS):

            # All nodes in the first row (left -> right) - starting from pacific to atlantic
            dfs(0, c, pac, heights[0][c])

            # All nodes in the last row (right -> left) - starting from atlantic to pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        # Iterate node from TOP and BOTTOM (in both directions)
        # So, note that columns stays constant and UPDATE ROWS (moving up and down)
        for r in range(ROWS):
            
            # All nodes in first column (on the top) - starting from pacific to atlantic
            dfs(r, 0, pac, heights[r][0])

            # All nodes in the last column (on the bottom) - starting from atlantic to pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            
        # Finally, check for nodes that are a part of both sets
        # These are the nodes where water can flow from one ocean to the other!
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

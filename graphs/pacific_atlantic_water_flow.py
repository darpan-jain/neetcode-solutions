class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ''' 
        We iterate from water to inside and check which nodes can do that for
        the two oceans separately. Note that here it means that the previous Height should be 
        greater than the current height since we are going in reverse (water to land).
        
        Finally, the result will contain nodes that can do it for both oceans, i.e. water flow
        from one ocean to the other!
        '''
        
        ROWS, COLS = len(heights), len(heights[0])
        # Maintain sets for nodes that can reach the Pacific and Atlantic ocean
        pac, atl = set(), set()
        
        # Run DFS on all nodes on the ocean boundaries and check their neighbors using DFS
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or
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
        '''
        
        # Iterate nodes from RIGHT and LEFT (in both directions)
        # So, note that rows stays constant and UPDATE COLUMNS (moving left and right)
        for c in range(COLS):
            # All nodes in the first row (left -> right) - starting from pacific to atlantic
            dfs(0, c, pac, heights[0][c])
            # All nodes in the last row (right to left ->) - starting from atlantic to pacific
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # Iterate node from TOP and BOTTOM (in both directions)
        # So, note that columns stays constant and UPDATE ROWS (moving up and down)
        for r in range(ROWS):
            # All nodes in first column (on the top) - starting from pacific to atlantic
            dfs(r, 0, pac, heights[r][0])
            # All nodes in the last column (on the bottom) - starting from atlantic to pacific
            dfs(r, COLS-1, atl, heights[r][COLS-1])
            
        # Finally, check for nodes that are a part of both sets.
        # These are the nodes where water can flow from one ocean to the other!
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
        
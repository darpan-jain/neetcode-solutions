class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ''' Approach 1: Using Recursive DFS '''
        
        # Empty case
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        # Since we are doing a DFS, we go down the search diagonally, 
        # so we do not go back up at all!
        visit = set()
        
        # Use Recursive DFS to find the number of islands
        def dfs(r, c):
            
            # Base case & main condition
            # Return if we encounter water i.e. "0", since island is over!
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == "0" or (r, c) in visit:
                return
            
            # Remember to add current element to `visit`
            visit.add((r, c))

            # Recursively iterate in all four directions for DFS
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                # Recursively call DFS in all four directions
                dfs(r + dr, c + dc)
                
            
        ## Main loop while running DFS - used to update the `islands` result
        for r in range(ROWS):
            for c in range(COLS):
                # Perform DFS ONLY IF you encounter land i.e. "1"
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Increment `islands` count and iterate until its edges (or until we reach water) using DFS
                    islands += 1
                    dfs(r, c)
        
        # Finally return result
        return islands

        '''
        ## Approach 2: Using Iterative BFS
        
        # Edge case for empty grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        # Create a set for all the visited nodes in the grid
        visited = set()
        islands = 0
        
        # Iterative BFS - done using queue
        def bfs(r, c):
            q = collections.deque()
            
            # Add current node to visited and also to the queue
            visited.add((r, c))
            q.append((r, c))
            
            # Iterate until all the nodes in queue are visited
            while q:
                # NOTE: Change to `q.pop()` to make this iterative DFS. Rest of the code is the same.
                # Since it'll now pop from the end of the queue instead of the start!
                curr_row, curr_col = q.popleft()
                
                # All the directions of current (r, c) to perform search in 
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = curr_row + dr, curr_col + dc

                    # Check if (r, c) position not out of grid, is land and is not visited
                    if r in range(rows) and \
                       c in range(cols) and \
                       grid[r][c] == "1" and \
                       (r, c) not in visited:

                        # If not, then we can add the node to the queue and the visited set
                        q.append((r, c))
                        visited.add((r, c))
    
        ## Main loop for counting the number of islands
        # Go through every row and column
        for r in range(rows):
            for c in range(cols):
                # Do BFS only when the node is land i.e. "1" and has not been visited already
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                    
        return islands
    '''
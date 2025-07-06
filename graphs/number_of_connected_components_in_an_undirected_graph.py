"""
Question (Leetcode Premium): https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
Free Version: https://neetcode.io/problems/count-connected-components
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list for tracking neighbors of each edge/node
        adj = [[] for _ in range(n)]

        # Populate `adj`
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # visit set to avoid revisiting edges or getting stuck in loops
        visit = [False] * n

        # Recursive DFS to visit all neighbors of a given `node`
        def dfs_neighbors(node):
            # Iterate through all neighbors of `node`
            for nei in adj[node]:
                # Only call DFS function if neighbor is not already visited
                if not visit[nei]:
                    # Set current `nei` as visited
                    visit[nei] = True
                    dfs_neighbors(nei)
        
        # Driver code to calculate num of connected components
        res = 0
        # Visit all nodes in the Graph
        for node in range(n):
            # Only run recursive DFS if node not visited previously
            if not visit[node]:
                # Set the current `node` as visited
                visit[node] = True
                # Recursive DFS on all neighbors
                dfs_neighbors(node)
                # At the end of the call, we have visited connected nodes in a component
                # So, we increment the `res`
                res += 1
        
        return res

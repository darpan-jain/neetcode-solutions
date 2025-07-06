"""
Question (Leetcode Premium): https://leetcode.com/problems/graph-valid-tree/
OR Free(Neetcode): https://neetcode.io/problems/valid-tree

"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # In-valid or Empty Case
        if not n:
            return True
        
        # Create adjacency list for tracking each edge and all it's connections
        adj = {i:[] for i in range(n)}

        # Populate the adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Visit set to track if all the nodes have been visited during DFS
        visit = set()

        # Recursive DFS
        def dfs(i, prev):
            
            # If revisiting a node, most likely a Cycle in the Tree, i.e., Invalid
            if i in visit:
                return False
            
            # Add current valid edge to Visit Set
            visit.add(i)

            # Now recursively visit all the neighbors of the current edge
            for nei in adj[i]:
                # If the previous edge and current neighbor are same, just skip the loop
                if nei == prev:
                    continue
                # Recursive DFS call with `nei` being the new edge and `i` being the previous edge
                if not dfs(nei, i):
                    # If False returned (i.e., if cycle), Invalid Tree
                    return False
            
            # If all neighbors validated, valid Recursive DFS for the current edge `i`
            return True
        
        # Return True if DFS on Full Tree is valid AND
        # also if all edges in the Tree have been visited (and validated)
        return dfs(0, -1) and len(visit) == n

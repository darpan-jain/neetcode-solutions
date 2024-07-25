"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Use Hashmap and DFS to create a deepcopy of the input graph.
        Hashmap is created to ensure that we are not cloning nodes repeatedly.

        Time complexity: O(n) where n = number of edges(E) + number of vertices(V)
        '''

        # Hashmap to keep track of the all clones being made of the original node    
        oldToNew = {}

        # Clone input `curr_node` using Recursive DFS
        def clone(curr_node):

            # Return the already created copy in the `node` is present in `oldToNew`
            if curr_node in oldToNew:
                return oldToNew[curr_node]

            # Create a deepcopy of the node and add it to the hashmap
            copy = Node(curr_node.val)
            # Add `copy` to the cloned node
            oldToNew[curr_node] = copy

            # Now recursively populate the neighbors of the cloned node
            for nei in curr_node.neighbors:
                copy.neighbors.append(clone(nei))
            
            # Finally, return the completed deepcopy of the current `node`
            return copy

        ## Clone the `root node` if its not empty
        return clone(node) if node else None

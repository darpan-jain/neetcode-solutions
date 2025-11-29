"""
Question: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


from typing import List, Optional
from collections import deque


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Approach: Use Iterative BFS, since it is 'level' order (BFS -> breadth == level)
    Remember DFS is for Depth-First traversal/search!
    
    Time Complexity: O(N), since we do a BFS on the tree
    Space Complexity: O(N), since the queue stores upto N/2 nodes in it. This makes O(N/2) -> O(N)
    """
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty case, return empty result
        if not root: 
            return []
        
        # Create a new deque for BFS with only the root and a result array
        queue  = deque([root])
        result = []
        
        # Iterate until the queue is empty
        while queue:
            # Create a new array for saving the nodes in the current level
            level = []
            
            # Iterate through the nodes in current level
            for i in range(len(queue)):     
                '''
                Remember the order of steps for Iterative BFS (done using a Queue) ->
                    - Pop the root from queue (leftmost element since FIFO)
                    - Add the left and right children to the queue (order is important, left first then right)
                    - Increment the level by 1 (since we are going level by level i.e. breadth-wise)
                    - Continue until queue is empty (which the for loop handles)
                '''
                
                # Pop the root node from the left of the queue i.e. from start of the queue
                node = queue.popleft()
                # Append this value to the current level of traversal (appends to the end of the queue)
                level.append(node.val)
                
                # Add the left and right children to the right of the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            # Finally append ALL the nodes in the `level` array to the result
            # Added as a list, to the `result` list
            result.append(level)
        
        return result

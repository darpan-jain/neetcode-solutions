'''
Question: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach: 
            - Perform In-Order Traversal (L -> N -> R) of the Tree using a stack
            - Stop when you have visited `k` elements
        
        Why In-Order Traversal? 
        We need to visit the smallest elements first and L < N < R in BST

        Time Complexity : O(N), where N is the number of nodes in the BST
        Space Complexity: O(N), to store the stack
        """

        # `n` indicates the number of nodes visited. We stop at `n == k`
        n = 0
        # Stack to store the values of visited nodes
        stack = []
        
        # Iterate until we go through the entire BST
        while root or stack:
            
            # Keep going to left nodes (smaller values) until we reach a leaf node
            while root:
                # Store the current value in the stack
                stack.append(root)
                # Iterate to the left child of the current node
                root = root.left

            # At the end of the while loop, we have reached a leaf node. So we traverse back up again (L -> N)
            # Pop the latest node to process it (here we are TRAVELLING BACK UP in the tree)
            root = stack.pop()
            n += 1
            
            # Check if we are the the k-th smallest node
            if n == k:
                # If we are, this is where we stop and return the result
                return root.val
            
            # Here, we have visited all left children of the current node, so we visit the right chilren
            # This also completes the L -> N -> R In-Order Traversal
            root = root.right

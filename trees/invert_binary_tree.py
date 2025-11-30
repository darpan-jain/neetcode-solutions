"""
Question: https://leetcode.com/problems/invert-binary-tree/
"""

from typing import Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Use Recursive DFS to swap the children of the root

        Time Complexity: O(N)
        Space Complexity: O(N), for the recursion stack
        """
        
        # Base case for recursion
        if not root:
            return None
        
        # Swap the Children of the current `root`
        root.left, root.right = root.right, root.left
        
        # Run invertion on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # At the end of all recursions, the final `root` will be the inverted tree.
        return root
    
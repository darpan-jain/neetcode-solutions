"""
Question: https://leetcode.com/problems/validate-binary-search-tree/
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
    """
    Approach: Recusrive DFS using helper function

    Time complexity = O(N), since visiting all nodes at least once
    Space complexity = O(N), to store all the node values in stack during recursion
    """
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initial values for boundaries of root node are +infinity and -infinity
        return self.isValid(root, float('-inf'), float('inf'))

    # Helper function
    def isValid(self, root: Optional[TreeNode], left: int, right: int) -> bool:
        """
        left -> int boundary that means that all nodes in the the current subtree must be smaller than this value
        right -> int boundary that means all values in the current subtree are greater than this value
        """
        
        # Base case
        if not root:
            return True
        
        # Check if current root follows the BST rule
        if not left < root.val < right:
            return False
        
        # Traverse to new BST with left and right nodes as new roots,
        # i.e. recursively check the left and right subtrees of the current root

        # For left subtree (LEFT node is now ROOT), every value should be less than root val, i.e. right == node.val
        # For right subtree (RIGHT node is now ROOT), every node should be greater than root val, i.e. left == node.val
        return (self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right))        

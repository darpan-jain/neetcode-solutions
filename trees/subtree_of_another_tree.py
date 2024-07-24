"""
Question: https://leetcode.com/problems/subtree-of-another-tree/
"""


from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    """
    Approach: Recursive DFS with helper function to check if two given trees are the same.
    Time Complexity: O(root * subRoot)
    """
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If `subRoot` is empty, then always a subtree of `root`
        # Since an empty tree is a subtree of any tree.
        if not subRoot: 
            return True
        
        # If `root` is empty (and `subRoot` is non-empty cause it skipped the previous IF statment),
        # then `subRoot` CAN'T be a subtree of `root`
        if not root: 
            return False
        
        # Here we check if `root` and `subRoot` are the same Tree -> Base case for recursion
        if self.isSameTree(root, subRoot): 
            return True
        
        # Finally we check if the left or the right subtrees of the `root` are equal to the `subRoot`.
        # Note the `OR` condition, since the subRoot can be on the left OR the right of the `root`
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

    # Helper function to check if `p` and `q` are the same trees.
    # Refer to https://leetcode.com/problems/same-tree/ and `trees/same_tree.py` for explanation.
    def isSameTree(self, p, q):

        if not p and not q:
            return True
        
        if (not p or not q) and (p.val != q.val):
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
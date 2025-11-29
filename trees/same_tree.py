"""
Question: https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: Use Recursive DFS, with stopping conditions for when the nodes are null or their values are unequal.

        Time Complexity: O(P+Q), where P and Q are the number of nodes in the two trees
        Space Complexity: O(H), where H is the height of the tree (due to recursion stack)
        """

        # Base case: if both are null, then equal
        if not p and not q:
            return True

        # If only one of them null (both being null is covered in previous condition), then not equal
        # OR both not null BUT have unequal values
        if (not p or not q) or (p.val != q.val):
            return False

        # Recursive DFS call
        # Here, both `p` and `q` are not null and their values match,
        # so recursively check the left and right subtrees of each for equality
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

'''
Question: https://leetcode.com/problems/same-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Use recursive DFS: Time Complexity = O(p + q)
        '''
        
        ## Base cases
        
        # If both are null, then equal
        if not p and not q:
            return True
        
        # If only one of them null, then not equal OR both not null but have unequal values
        if (not p or not q) or (p.val != q.val):
            return False
        
        ## Recursive call
        # Here, both p and q are not null and their values match,
        # so recursively check the left and right subtrees of each for equality
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
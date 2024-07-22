'''
Question: https://leetcode.com/problems/invert-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Use Recursion to swap the children of the root. Done using DFS.
        '''
        
        # Base case for recursion
        if not root:
            return None
        
        # Swap the Children
        root.left, root.right = root.right, root.left
        
        # Run invertion on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the inverted root
        return root
    
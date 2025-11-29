'''
Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        -> Order name depends on when 'Root Node' is traversed!
        Traversal Definitions:
            - Preorder :  Visit Node ➝ Left ➝ Right  (NLR)
            - Inorder  :  Visit Left ➝ Node ➝ Right  (LNR)
            - Postorder:  Visit Left ➝ Right ➝ Node  (LRN)
    
        Approach: Order traversal done recursively
            - Notice that first value in Preorder array is always the Root. And the values on the left of the root in Inorder array are the left children
            - The first element in the `preorder` list is always the root of the current (sub)tree
            - In the `inorder` list, elements to the left of the root belong to the left subtree and elements to the right belong to the right subtree
            - Use these two intuitions to recursively construct the Binary Tree

        Time Complexity : O(N^2) in the worst case due to index() call inside recursion
        Space Complexity: O(N) for the recursion stack
        """
        
        # Base case: If either traversal list is empty, return None (no subtree)
        if not preorder or not inorder:
            return None
        
        # First value in `preorder` is ALWAYS the root of the current Tree (since N->L->R)
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of `root_val` (from `preorder`) in the `inorder` list
        # `mid` is used to split the inorder list into left and right subtrees
        mid = inorder.index(root_val)
        
        ''' 
        Now recursively construct the left and right subtrees of the current root
        Pass the left and right nodes as new roots from the input lists to construct the respective subtrees
        '''

        # For left subtree, isolate Left child of current root:
            # - For Preorder - next `mid` elements after root (since left subtree has `mid` nodes and is NLR) 
            # - For Inorder - The nodes on the left of `mid` (root)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        
        # For right subtree, Right Child is always in the end of the Traversal list,
        # So, pass everything on the right of `mid` from both preorder and inorder arrays
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root
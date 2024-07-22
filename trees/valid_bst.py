'''
Question: https://leetcode.com/problems/validate-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Done using recursion from a helper function!
    Time complexity = O(n) since visiting all nodes at least once
    Space complexity = O(n) since storing all the node values in stack during recursion
    '''
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initial values for boundaries of root node are + and - infinity!
        return self.isValid(root, float('-inf'), float('inf'))

    # Helper function
    def isValid(self, root, left, right):
        '''
        left = boundary that means that all nodes in the the current subtree must be smaller than this value
        right = boundary that means all values in the current subtree are greater than this value
        '''
        
        # Base case
        if not root:
            return True
        
        # Check if current root follows the BST rule
        if not left < root.val < right:
            return False
        
        # Traverse to new BST with left and right nodes as new roots
        # i.e. recursively check the left and right subtrees of the current root.

        # For left subtree (left node is now root), every value should be less than root val -> right == node.val
        # For right subtree (right node is now root), every node should be greater than root val -> left == node.val
        return (self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right))        

'''
Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        The LCA is the node where the split occurs for p and q nodes in the BST
        Time complexity: O(log n) since we search the BST instead of entirely iterating it.
        '''
        
        # Iterate until we find the LCA
        while root:
            
            # If p and q are both greater than current value, 
            # continue searching on the right of the current node of the BST
            if root.val < p.val and root.val < q.val:
                root = root.right
                
            # Vice-versa of previous condition. i.e. p and q are both less than current value
            elif root.val > p.val and root.val > q.val:
                root = root.left

            # If not previous cases, then we have found our split, i.e. the LCA
            else:
                return root
        
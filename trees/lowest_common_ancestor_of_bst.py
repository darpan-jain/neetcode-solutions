"""
Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Approach: The Lowerst Common Ancestor (LCA) is the node in the tree where the split 
        occurs for `p` and `q` nodes in a Binary Search Tree (BST).
        
        Time complexity: O(log N), since we search the BST with DFS instead of 
        entirely iterating it (which would take O(N) time).
        """
        
        # Iterate the tree until we find the LCA (result is guaranteed to exist)
        while root:
            
            # If `p` and `q` are both greater than current value, 
            # continue searching on the right of the current node of the BST
            if root.val < p.val and root.val < q.val:
                root = root.right
                
            # Vice-versa of previous condition. i.e. p and q are both less than current value
            elif root.val > p.val and root.val > q.val:
                root = root.left

            # If not previous cases, then we have found our split, i.e. the LCA
            else:
                return root

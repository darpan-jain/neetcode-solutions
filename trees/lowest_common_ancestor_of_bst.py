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
        Approach: The Lowerst Common Ancestor (LCA) is the node in the tree where the split occurs for `p` and `q` nodes in a Binary Search Tree (BST)
        
        Time Complexity : O(log N), since we search the BST with DFS instead of entirely iterating it (which would take O(N) time)
        Space Complexity: O(1), since we are not using any additional data structures that grow with input size
        """
        
        # Iterate the tree until we find the LCA (result is guaranteed to exist)
        while root:
            
            # If `p` and `q` are both less than current value `root.val` 
            # continue searching on the right of the current node of the BST (since all values GREATER than `root.val` are on the RIGHT)
            if p.val < root.val and q.val < root.val:
                root = root.left
                
            # Vice-versa of previous condition, i.e. `p` and `q` are both greater than current value `root.val`
            # continue searching on the left of the current node of the BST (since all values LESS than `root.val` are on the LEFT)
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # If not previous cases, then we have found our split, i.e. the LCA
            else:
                return root

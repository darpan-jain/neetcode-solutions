'''
Question: https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Goal: Find the maximum path sum in a binary tree.
        Remember: A path can start and end at any node, but EACH NODE may be USED ONLY ONCE.
        
        Approach:
        - Use DFS (depth-first search) to recursively compute the max sum from each subtree.
        - DFS because it allows to explore all nodes bottom-up and calculate local path sums in log(N) time
        - For each node:
          - 1. Calculate the max path sum that can be extended UPWARD to its parent (without split) - used for `leftMax` and `rightMax`
          - 2. Calculate the max path sum that ENDS at current node and includes both subtrees (with split) - stored in `res`
        - 3. Keep track of the global maximum using the `res` list
        
        Time Complexity: O(N), where `N` is the number of nodes in the tree
        Space Complexity: O(H), where `H` is the height of the tree (due to recursion stack)
        """
        
        # To store the maximum path sum found so far
        res = [root.val]
        
        # Returns the max path sum without a split
        def dfs(root):
            
            # Base case
            if not root:
                return 0
            
            # Find the max sum of the left path and ignore non-negative sums (by taking max with 0)
            leftMax = max(dfs(root.left), 0)
            
            # Find the max sum of the left path and ignore it non-negative sums
            rightMax = max(dfs(root.right), 0)

            '''
            What if we don't make the leftMax and rightMax values non-negative?
                - Ensures that ONLY positive contributions from child paths are included in the path sum
                - If a subtree has a negative sum, including it would decrease the total value of any path passing through that node
            
            Eg:
                Tree:
                     -10
                     /  \
                   -20   5

                Without max(..., 0):
                    Path sum at root = -10 + (-20) + 5 = -25  ❌

                With max(..., 0):
                    leftMax = 0, rightMax = 5
                    Path sum at root = -10 + 0 + 5 = -5        ✅

                The correct max path is just the node 5 → sum = 5

            So, we use max(..., 0) to exclude harmful (negative) paths.
            '''
            
            # Compute and store the max path sum that ENDS at current node and includes both subtrees (WITH SPLIT)
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # BUT, we have to return the max value WITHOUT SPLIT 
            # This return value is is used by the recursive calls for `leftMax` and `rightMax`
            return root.val + max(leftMax, rightMax)
        

        ''' Driver code, run dfs starting from the root '''
        dfs(root)

        # Return the value stored in `res` at index 0, i.e. value of the MAX PATH SUM of the entire Tree
        return res[0]
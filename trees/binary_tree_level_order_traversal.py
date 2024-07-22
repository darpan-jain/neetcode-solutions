'''
Question: https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    '''
    Since it's 'level' order, we use BFS (breadth == level).
    Remember DFS is depth-first traversal!
    
    Time complexity = O(n) since we do a BFS on the tree
    Space complexity = O(n), since the queue stores upto n/2 nodes in it. 
    This makes O( n/2 ) -> O( n ) space complexity
    '''
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty case, return empty result
        if not root: 
            return []
        
        # Create a new deque for BFS with only the root and a result array
        queue  = deque([root])
        result = []
        
        # Iterate until the queue is empty
        while queue:
            # Create a new array for saving the nodes in the current level
            level = []
            
            # Iterate through the nodes in current level
            for i in range(len(queue)):
                
                # Remember the steps for BFS - pop current element, add its children to the queue
                
                # Pop the root node from the left of the queue i.e. from start of the queue
                node = queue.popleft()
                # Append this value to the current level of traversal (appends to the end of the queue)
                level.append(node.val)
                
                # Add the left and right children to the right of the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            # Finally append ALl the nodes in the `level` array to the result
            # Added as a list, to the `result` list
            result.append(level)
        
        return result
                              
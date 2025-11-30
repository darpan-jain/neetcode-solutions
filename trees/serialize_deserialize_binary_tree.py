'''
Question: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Approach: Use Recursive DFS to serialize the tree using Preorder traversal (root -> left -> right or N -> L -> R)
    (can also be done using BFS with a queue)

    Time complexity: O(N) for both serialize and deserialize
    Space complexity: O(N) for both serialize and deserialize
    """

    def serialize(self, root: TreeNode) -> str:
        """ Encodes a tree to a single string. """
        
        # Serialized result array
        res = []
        
        # Create DFS Helper for Preorder traversal
        def dfs(node):
            # Base case - at a leaf node, add "N" to represent null
            if not node:
                res.append("N")
                return
            
            # Add the first node as root (since it is Preorder traversal)
            res.append(str(node.val))

            # Now recursively build for left and right subtrees
            dfs(node.left)
            dfs(node.right)
        

        # Call the helper DFS function
        dfs(root)

        # Return the result as a string
        return ",".join(res)


    def deserialize(self, data: str) -> TreeNode:
        """ Decodes your encoded data to tree. """
        
        # Split the data into an array (joined using ',' during serialization)
        vals = data.split(",")

        # Pointer which is a member variable of the 'Codec' class
        self.i = 0
        
        # Helper DFS method to re-build the tree from the `data` string
        def dfs():

            # Base case -> if we encounter "N", return None
            if vals[self.i] == "N":
                # Increment `self.i` so that we can move to next value
                self.i += 1
                return None
            
            # Add the root node to the new BST
            node = TreeNode(int(vals[self.i]))

            # Increment `self.i` so that we can move to next value
            self.i += 1

            # Now re-build the left and right subtrees
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        # Return the resulting tree from the recursively dfs function
        return dfs()

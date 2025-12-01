"""
Question: https://leetcode.com/problems/word-search-ii/
"""

from typing import List


class TrieNode:
    """
    TrieNode class to store information about each node in the Trie.
    For detailed explanation, refer to solution in tries/implment_trie_prefix_tree.py
    """

    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0 # To keep track of how many words pass through this node

    def addWord(self, word):
        cur = self # Start from the root node, i.e., `self`
        cur.refs += 1 # Increment the refs count for the root node

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
            # Increment the refs count for each node in the path of the word
            cur.refs += 1

        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                # Decrement the refs count for each node in the path of the word (since removing)
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Init the root of the Trie
        root = TrieNode()

        # Add all given `words` to the Trie
        for w in words:
            root.addWord(w)

        # Define the number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])
        # Define the sets to store the visited cells and the result words
        res, visit = set(), set()

        # Define the DFS function to search for the words in the board
        def dfs(r, c, node, word):

            # Base case for stopping the DFS recursion
            if (
                    r not in range(ROWS) or # Out of bounds row
                    c not in range(COLS) or # Out of bounds column
                    board[r][c] not in node.children or # Current character not in Trie children
                    node.children[board[r][c]].refs < 1 or # No words pass through this node
                    (r, c) in visit # Current cell already visited
                ):
                return

            # Add the current cell to the visited set (to avoid revisiting the same elements on the board)
            visit.add((r, c))
            
            # Set `node` to the current node's children
            node = node.children[board[r][c]]

            # Add the current character to the word
            word += board[r][c]

            # If the current character is a word (if `isWord` == True), remove it from the Trie and add it to the result set
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            # Now recursively search for the next characters in the word in all 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # After searching all 4 directions, remove the current cell from the visited set (to allow other paths to use this cell)
            visit.remove((r, c))


        ## Driver code to start the DFS search for every cell in the board (from main function)
        for r in range(ROWS):
            for c in range(COLS):
                # Start params for DFS: current cell, root of the Trie, and the current word
                dfs(r, c, root, "")

        # Finally, return the result set as a list
        return list(res)

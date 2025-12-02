'''
Question: https://leetcode.com/problems/word-search/
'''

from typing import List


class Solution:
    """
    Approach: Backtracking + Depth First Search (DFS)

        - Iterate over each cell in the board as a potential starting point for the word search
            - For each cell, initiate a DFS to explore all possible paths to match the word
        
        - During DFS, check if the current cell matches the current character of the word
            - If it matches, mark the cell as visited (e.g., by changing its value temporarily)
            - Recursively explore all four possible directions (up, down, left, right)
            - If the entire word is matched, return True
            - If a path does not lead to a solution, backtrack by unmarking the cell
        
        - If no starting point leads to a successful match, return False
    
    Time Complexity: O(M * 4^N)
        - M is the number of cells in the board
        - N is the length of the word to be searched
        - Each cell can lead to 3 possible directions (excluding the direction we came from)

    Space Complexity: O(N)
        - The recursion stack can go as deep as the length of the word in the worst case
    """
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Checks for empty conditions
        if not board:
            return False
        
        if not word:
            return True
        
        # Iterate over each row and column on the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        # If DFS doesn't return a True, word not found!
        return False
    
    # Helper function to perform DFS on the board to search a given word
    def dfs(self, board, r, c, word):
        # Base case - Empty word i.e. all characters checked and matched
        if len(word) == 0:
            return True
        
        # Check if r and c, i.e. row and column pointers are not going out of the board
        # or if current character doesn't match the curr char from the board
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[0] != board[r][c]:
            return False
        
        # Assign current word in the ith row and jth column to a temporary variable
        tmp = board[r][c]
        # Make the current word on board non-alphabetic to avoid visits again
        board[r][c] = '#'
        
        # Continue to check for other letters of the word in every direction.
        # Remember to search for all the words AFTER the current word!
        res = self.dfs(board, r + 1, c, word[1:]) or \
              self.dfs(board, r - 1, c, word[1:]) or \
              self.dfs(board, r, c + 1, word[1:]) or \
              self.dfs(board, r, c - 1, word[1:])
        
        # Make the current word alphabetic again
        board[r][c] = tmp
        
        # Boolean value to denote if the word exists in the board (from searching in all four directions from current cell at [r][c])
        return res

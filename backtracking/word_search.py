'''
Question: https://leetcode.com/problems/word-search/
'''

class Solution:
    
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
        
        # Check if r and c i.e. row and column pointers are not going out of the board
        # or if current character doesn't match the curr char from the board
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[0] != board[r][c]:
            return False
        
        # Assign current word in the ith row and jth column to a temporary variable
        tmp = board[r][c]
        # Make the current word on board non-alphabetic to avoid visits again
        board[r][c] = '#'
        
        # Continue to check for other letters of the word in every direction.
        # Remember to search for all the words AFTER the current word!
        res = self.dfs(board, r+1, c, word[1:]) or \
              self.dfs(board, r-1, c, word[1:]) or \
              self.dfs(board, r, c+1, word[1:]) or \
              self.dfs(board, r, c-1, word[1:])
        
        # Make the current word alphabetic again
        board[r][c] = tmp
        
        return res
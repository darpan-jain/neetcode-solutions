'''

Question: Longest Common Subsquence
Link: https://neetcode.io/problems/longest-common-subsequence

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Approach: Bottom-up Dynamic Pgogramming

        Visualize a DP as a 2D grid of size -> `len(text1) * len(text2)`

        Start from bottom-right, and look for matching characters along the diagonal positions.
        
            - If they match, add 1 and update the current position with the value from the diagonal position
            - If the don't match, at the current diagonal position, check for matches in the bottom or the right positions.
              Here the value to update will be the max of values in right and bottom positions on the DP grid.
        
        Time Complexity: O(N * M)
            where,
                `M` = `len(text1)`
                `N` = `len(text2)`
        Space Complexity: O(M * N)
        """
        
        # Create DP as a 2D Grid, initialized with all 0s
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Iterate starting from the bottom-right corner of the DP grid and move towards the top-left (start of the grid)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                # Check if characters at current positions match
                if text1[i] == text2[j]:
                    # If chars match, update the current position with the value from the diagonal position
                    # Add 1 to the value from the diagonal position since we found a match in the current position
                    dp[i][j] = 1 + dp[i+1][j+1]
                    
                else:
                    # If they don't match, add the max between right [i][j+1] and bottom [i+1][j] positions of the current position
                    # Here we don't add 1, since no match was found
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        # Finally, as we were iterating bottom-up, from bottom-right to top-left,
        # the top-left position will have the final answer for the longest common subsequence
        return dp[0][0]

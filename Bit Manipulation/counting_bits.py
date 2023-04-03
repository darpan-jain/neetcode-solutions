'''
Question: https://leetcode.com/problems/counting-bits/
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Time Complexity = O(n)
        '''

        # Create a `dp` of length `n+1`
        dp = [0] * (n + 1)
        # Offset determines where the significant bit changes
        offset = 1

        for i in range(1, n+1):
            # Offset changes only if i reaches `offset*2`
            if offset * 2 == i:
                offset = i

            # Number of ones is 1 + the number of ones in the i-offset position
            dp[i] = 1 + dp[i - offset]
        
        return dp
         
        
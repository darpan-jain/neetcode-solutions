'''
Question: https://leetcode.com/problems/counting-bits/
'''


from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Approach: Use Dynamic Programming to store the number of 1s in the binary representation of the number
        
        Time Complexity: O(N) -> iterating number with `N` times
        Space Complexity: O(N) -> storing the result in `dp` array
        """

        # Create a `dp` of length `n+1` to store the number of 1s in the binary representation of the number
        dp = [0] * (n + 1)

        # Offset determines where the significant bit changes
        offset = 1

        # Iterate from 1 to `n`
        for i in range(1, n+1):
            # Offset changes only if `i` reaches `offset*2` (i.e., the next power of 2)
            if offset * 2 == i:
                offset = i

            # Number of ones is 1 + the number of ones in the `i-offset` position
            dp[i] = 1 + dp[i - offset]
        
        return dp

'''
Question: https://leetcode.com/problems/longest-increasing-subsequence/
'''

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ 
        Approach: Bottom-up DP (iterate in reverse)

        - Iterate `nums` in reverse. At each index `i`:
            1. Create an increasing subsequence between i and len(nums) 
            2. Store the len of the subsequence in dp[i], if it is more that the current value (default is 1)
        - Finally, return the max length stored in all values of `dp`
        
        Time Complexity: O(N^2), since we have an outer loop for `i` and then an inner loop to create increasing subsequence) 
        Space Complexity: O(N), extra space to store the values in `dp`
        
        Can be done in O(N log N) using Segment Trees or Binary Search + DP 
        Refer to https://neetcode.io/problems/longest-increasing-subsequence/solution
        """
        
        n = len(nums)
        
        # Create DP of len(nums) with default value of 1 (since each element in itself is a subsequence of length 1)
        # This DP maintains the length of increasing sequences at each index `i`
        dp = [1] * n
        
        # Iterate in bottom-up i.e., reverse, to populate the `dp`
        # Outer loop iterates over all elements in reverse order
        for i in range(n, -1, -1):

            # Inner loop iterates over all elements after the ith index until end of `nums`
            for j in range(i + 1, n):
                
                # Check for increasing subsequence, 
                # i.e., if nums[i] (previous element) is less than nums[j] (current element)
                if nums[i] < nums[j]:

                    # If yes, then update the max subsequence length at dp[i]
                    # Note: 1 is added because we add the current element `nums[j]` to the new subsequence
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # After processing all elements, `dp` will contain the length of the longest increasing subsequence at all indices
        # Return the max value from all the indices in `dp`
        return max(dp)

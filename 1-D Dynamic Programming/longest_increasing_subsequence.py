'''
Question: https://leetcode.com/problems/longest-increasing-subsequence/
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ''' DP Approach -> Time Complexity = O(n^2) '''
        
        n = len(nums)
        
        # Create array of 1 with length = len(nums)
        # This DP maintains the length of increasing sequences at each index
        dp = [1 for _ in range(n)]
        
        # Since this is a DP approach, we iterate in reverse i.e. Bottom-up
        # `i` iterates over len(nums) to 0 (in reverse) 
        for i in range(n, -1, -1):
            # `j` iterates over all elements after the ith index (until `n`)
            for j in range(i+1, n):
                # Check if 'ith' element is lesser than every jth element
                # i.e. check if it fits the increasing sub-sequence
                if nums[i] < nums[j]:
                    # If it does, store the subseq with the longest length
                    # Note: the 1 is added because we include the current 
                    # element in the subsequence
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # Return the length of the longest sequence
        return max(dp)
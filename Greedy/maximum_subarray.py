'''
Question: https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        ''' Approach 1: 
         Kadane's Algorithm: Time Complexity = O(n)
         
         - If the sum of a subarray is positive, it is possible to 
         make the next value bigger, so we keep do it until it turns negative.     
         - If the sum is negative, it has no use to the next element, so we break.
         It is a game of sum, not the elements.
        '''

        if not nums:
            return 0
        
        # for i in range(1, len(nums)):
        #     # Add to current sum only if the value is positive
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]

        # return max(nums)
    
        ''' Approach 2: (same idea) Time Complexity = O(n) '''
        
        # Init current sum to 0 and maxSum to first element
        currSum = 0
        maxSum = nums[0]
        
        # Iterate over the remaining elements
        for n in nums:
            # Add current number to currSum
            currSum += n
            # and compare with existing maxSum
            maxSum = max(currSum, maxSum)
            
            # If currSum goes negative, make the currSum zero
            # since we cannot use a subarray with negative values (larger than currSum)
            # as they will result in a negative sum (obvs won't be max)
            if currSum < 0:
                currSum = 0
            
        return maxSum
    
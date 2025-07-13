'''
Question: https://leetcode.com/problems/maximum-subarray/
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        """
        Approach 1: Kandane's Algorithm

        Iterate through `nums`, adding each element to the `currSum`
        Ensure that `currSum` is never non-zero (negative)

        - If the sum of a subarray is positive, it is possible to 
        make the next value bigger, so we keep doing it until it turns negative.     
        - If the sum is negative, it has no use to the next element, so we break.
        
        It is a game of sum, not the elements!

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        # Empty or invalid case
        if not nums:
            return 0

        # Initialize maxSum as the first element and currSum as 0
        maxSum = nums[0]
        currSum = 0

        # Iterate over all elements in `nums`
        for num in nums:
            # For each iteration, ensure that `currSum` is always non-zero
            if currSum < 0:
                currSum = 0
            
            # Add current element `num` to `currSum`
            currSum += num

            # Update `maxSum` for every iteration
            maxSum = max(maxSum, currSum)
        
        # Return the final `maxSum`
        return maxSum
    
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
    
    def maxSubArray(self, nums: List[int]) -> int:

        """
        Approach 2: Divide and Conquer

        Divide the array into two halves, recursively find the maximum subarray sum in each half,
        and find the maximum subarray sum that crosses the midpoint.

        Time Complexity: O(N log N), since search is done in `log N` time and we iterate through the array in each recursive call
        Space Complexity: O(log N) for storing the recursive stack
        """

        # Empty or invalid case
        if not nums:
            return 0

        # DFS function to find the max sum in each half of `nums`
        def dfs(l, r):

            # Base case: if left index is greater than right, return -infinity (since we want max sum)
            if l > r:
                return float("-inf")

            # Find the mid index to divide `nums` into left and right
            m = (l+r) // 2

            # Init the currSum and leftSum
            # Iterate over the left half starting from mid and going left until leftmost index `l-1` -> `m-1` to `l-1`
            leftSum = currSum = 0
            for i in range(m-1, l-1, -1):
                # Add current elem to `currSum`
                currSum += nums[i]
                # Update leftSum to be the max of current leftSum and currSum
                leftSum = max(leftSum, currSum)
            
            # Same for right half. Iterate from mid+1 and go right until rightmost index `r` -> `m+1` to `r+1`
            rightSum = currSum = 0
            for j in range(m+1, r+1):
                currSum += nums[j]
                rightSum = max(rightSum, currSum)
            
            '''
            Perform recursive calls in left and right halves of the array (similar to Binary Search)
            The function returns MAX between -
                1. Recursive calls from left and right halves (which return max from their respective halves)
                2. Sum of (leftSum, mid element, rightSum), from the current mid index `m`
            '''
            return max(dfs(l, m-1), dfs(m+1, r), leftSum + nums[m] + rightSum)
        
        return dfs(0, len(nums)-1)

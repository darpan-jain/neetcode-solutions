'''
Question: http://www.lintcode.com/en/problem/maximum-product-subarray/
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Approach: Modified Kadane's Algorithm for Maximum Product Subarray

        - Use two variables, `currMax` and `currMin`, to track the maximum and minimum products ending at the current position.
        - Iterate through the array, updating `currMax` and `currMin` at each step.
        - Update the result `res` with the largest product found so far.

        Why track both `currMax` and `currMin`?
            - The array may contain negative numbers. Multiplying a negative number by the current minimum (which could also be negative) can yield a new maximum product.
            - If we only track the maximum, we might miss a larger product that results from two negatives multiplying to a positive.
            - Similarly, multiplying a positive number by the current maximum can also yield a new maximum.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        
        # Init `res` with max value in array, for cases where array length is 1
        res = max(nums)
        # Init variables with 1 (not zero since we are multiplying)
        currMax, currMin = 1, 1

        # Iterate over all the numbers in the array `nums`
        for n in nums:
            '''
            Store the currMax before recomputing it. Why?
            Notice that if we don't, `currMax` will change when being updated, before being used to update `currMin`
                -> currMax = max(currMax * n, currMin * n, n)
                -> currMin = min(currMax * n, currMin * n, n)

            So, we first save the value of `currMax` and then use it for the calculation of `currMin`
            '''
            temp = currMax * n

            # Update currMax and currMin by comparing (n, prev currMax, prev currMin)
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp,        currMin * n, n)
            
            # Save the max value b/w currMax, currMin and result -> this is the largest product so far
            res = max(currMax, currMin, res)
        
        # Return the final max product value
        return res

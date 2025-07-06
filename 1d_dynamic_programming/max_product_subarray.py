'''
Question: http://www.lintcode.com/en/problem/maximum-product-subarray/
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        We maintain a current max and min since we have negative values in the array as well.
        So, a negative multiplied by min value (negative mostly), will result in a positive product.
        If we only maintain the max value (which is mostly positive), we lose that negative product 
        that could become positive (and bigger) with the next `n` in the iterations.

        And vice-versa - a positive value multiplied by a max value (mostly positive), 
        will also give a positive product.

        Time Complexity: O(N)
        '''
        
        # Init `res` with max value in array, for cases where array length is 1
        res = max(nums)
        # currMax and currMin start with value 1 (not zero since we are multiplying)
        currMax, currMin = 1, 1

        # Iterate over all the numbers in the array 'nums'
        for n in nums:
            '''
            Store the currMax before recomputing it. Why?
            Notice if we don't, how `currMax` will change, before being used for `currMin`
            -> currMax = max(currMax * n, currMin * n, n)
            -> currMin = min(currMax * n, currMin * n, n)

            So, we first save the value of `currMax` and then use it for the calculation of `currMin`
            '''
            temp = currMax * n

            # Update currMax and currMin by comparing (n, prev currMax, prev currMin)
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp,        currMin * n, n)
            
            # Save the max value b/w currMax, currMin and result -> this is the maxProduct so far
            res = max(currMax, currMin, res)
        
        # Return the final maxProduct value
        return res

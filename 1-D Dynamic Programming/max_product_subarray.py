'''
Question: http://www.lintcode.com/en/problem/maximum-product-subarray/
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Maintain a current max and min since we have negative values in the array as well.
        So, a negative multiplied by min value (negative mostly), will result in a positive product
        And vice-versa - a positive value multiplied by a max value (mostly positive), will 
        also give a positive product
        '''
        
        # init `res` with max value in array, for cases where array length is 1
        res = max(nums)
        # `currMax` and `currMin` start with value 1 (not zero since we are multiplying)
        currMax, currMin = 1, 1
        
        # Iterate over all the numbers in the array `nums`
        for n in nums:
            '''
            Store the currMax before recomputing it!
            Why? Notice how currMax is changed here, before using for currMin
            
            -> currMax = max(currMax * n, currMin * n, n)
            -> currMin = min(currMax * n, currMin * n, n)
            '''
            
            # So, we save the value of currMax and then use it for the calculation of currMin
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp, currMin * n, n)
            
            # Save the max value b/w currMax, currMin and result -> this is the maxProduct so far
            res = max(res, currMax, currMin, res)
        
        # Return the final maxProduct value
        return res

"""
Question: https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        Approach: Use a prefix and postfix for each element and multiply
        the two values to get the product for the ith element.
        `prefix` -> stores product of all values before current element
        `postfix` -> stores product of all values after current element

        Intuition: prefix[i] * postfix[i] = product of all elements except self[i]

        Time Complexity: O(N), where N is the number of elements in the array `nums`
        Space Complexity: O(1), since we don't create any new arrays for storing prefix and postfix values
        """

        # Store the length of the array since it will be used multiple times
        n = len(nums)
        
        # Init a result array with all 1s
        result = [1] * n
        # Init a prefix value with 1 (Why not `0`? Since we have to find the product!)
        prefix = 1
        
        """ 
        Step 1 - Calculating Prefix of each element and store it in the `result` array. Each element's prefix is stored
        in the next element of the results array, i.e., `result[i]` stores the prefix of `nums[i+1]`
        """
        # Store the prefix of ith element in `i+1` position of results array
        for i in range(n):
            # Store the previous element's prefix in the results array
            result[i] = prefix
            # Update the prefix for the next element
            prefix *= nums[i]
        
        # DEBUG: Now the `result` array has all the prefix values for each element stored.
        # Trying printing this on a few test cases to understand the intuition behind the solution.
        # print(result)

        """ Step 2 - Calculating Postfix and multiplying with prefix """
        # Now, we multiply the postfix of each element with the prefix (stored in `result` array)

        # Again, start with an initial postfix value of 1 (remember: we are finding product)
        postfix = 1
        
        # Iterate in reverse since postfix (since we want every element's POSTfix value, so we start from the end)
        for i in range(n-1, -1, -1):
            # Update and store value in ith position of `res` by multiplying with postfix value
            result[i] *= postfix
            # Update postfix value for the next element
            postfix *= nums[i]
        
        ''' Step 3 - Return final `result` array '''
        return result

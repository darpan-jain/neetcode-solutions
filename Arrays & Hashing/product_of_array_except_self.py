'''
Question: https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        Use a prefix and postfix for each element and multiply 
        the two values to get the product for the ith element.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        
        n = len(nums)
        
        # Init a result array with all 1s
        result = [1] * n
        # Init a prefix value with 1 (Why not `0`? Since we have to find the product!)
        prefix = 1
        
        ''' 1. Calculating Prefix '''
        # Store the prefix of ith element in `i+1` position of results array
        for i in range(n):
            # Store the previous element's prefix in the results array
            result[i] = prefix
            # Update the prefix for the next element
            prefix *= nums[i]
        
        # DEBUG: Now the 'res' array has all the prefix values for each element stored
        # print(result)

        ''' 2. Calculating Postfix and multiplying with prefix '''
        # Now, we multiply the postfix of each element with the prefix (stored in `result` array)

        # Again, start with an initial postfix value of 1 (remember: we are finding product)
        postfix = 1
        
        # Iterate in reverse since postfix (since we want every element's POSTfix value)
        for i in range(n-1, -1, -1):
            # Update and store value in ith position of `res` by multiplying with postfix value
            result[i] *= postfix
            # Update postfix value for the next element
            postfix *= nums[i]
        
        ''' 3. Return final result '''
        # Final result to be returned
        return result
                 
'''
Question: https://leetcode.com/problems/missing-number/
'''

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ 
        Approach 1: Brute force

        1. Create a result array of length `len(nums) + 1` and set all elements to -1
        2. Replace -1 with actual number present in the list. 
        3. Now find the missing number (which will be set to -1)!

        Time Complexity: O(N) -> iterating over the input list
        Space Complexity: O(N) -> storing the result in `res` array
        """
        
        # 1. Initialize array of -1 of len of `nums`
        res = [-1] * (len(nums) + 1)
        
        # 2. Replace -1 with actual number present in the list
        for i in nums:
            res[i] = i

        # 3. Now find the missing number (which will be set to -1)
        for j in range(len(res)):
            
            if res[j] == -1:
                return j
            
        """ 
        Approach 2: Sum of 0..n minus sum of the given numbers is the missing one

        Formula for Sum on all numbers from 0 to n -> ( n * (n + 1) ) // 2


        Time Complexity: O(N) -> iterating over the input list
        Space Complexity: O(1) -> no extra space to store the result
        """

        n = len(nums)

        # Use formula for sum of all numbers from 0 to `n`
        sum_n = ( n * (n+1) // 2 )

        # Subtract the sum of the given numbers from the sum of (0 to `n`) to get the missing number
        return sum_n - sum(nums)
    
        """ 
        Approach 3: Iteratively calculate sum of all numbers instead of using formula from Approach 2

        Time Complexity: O(N) -> iterating over the input list
        Space Complexity: O(1) -> no extra space to store the result
        """

        # Set result to be equal to len of the nums array
        result = len(nums)
        
        # Iterate through each number from 0 to `n`
        for i in range(len(nums)):

            # Add to the result the difference of the the index and the `nums[i]` element
            # This is because the missing number will be the difference between the index and the element at that index
            result += (i - nums[i])

        # All the numbers except the missing number will become zero, and the missing number will be the result
        return result
        
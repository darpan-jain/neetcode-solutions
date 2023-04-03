'''
Question: https://leetcode.com/problems/missing-number/
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' Approach 1: Brute Force O(N) approach'''
        
        # # Initialize array of -1 of len of 'nums'
        # res = [-1] * (len(nums) + 1)
        
        # # Replace -1 with actual number present in the list
        # for i in nums:
        #     res[i] = i
            
        # # Now find the missing number (which will be set to -1)
        # for j in range(len(res)):
            
        #     if res[j] == -1:
        #         return j
            
        ''' Approach 2: Sum of 0..n minus sum of the given numbers is the missing one.'''
        # n = len(nums)
        # # Formula for sum of (0 to n) = ( n * (n + 1) ) // 2
        # sum_n = ( n * (n+1) // 2 )
        # return sum_n - sum(nums)
    
        ''' Approach 3: Same approach as 2 but without formula 
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        # Set result to be equal to len of the nums array
        result = len(nums)
        
        # iterate through each index from 0 to n
        for i in range(len(nums)):
            # Add to the result the index and subtract the nums[i] element
            result += (i - nums[i])
            # All the numbers except the missing number will become zero
        
        return result
        
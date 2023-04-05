'''
Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Use two pointers and take advantage of the array being sorted. 
        i.e. perform a Binary Search on the array.

        Time Complexity: O(n)
        '''

        left, right = 0, len(numbers) - 1
        
        # This condition not needed since we are guaranteed a solution!
        while left < right:
            # Compute the sum using the current positions of `left` and `right`
            currSum = numbers[left] + numbers[right]

            # If the currSum is more than target, we move the `right` pointer to make smaller
            if currSum > target:
                right -= 1
            # Vice-versa of the first condition, we move the `left` pointer to make `currSum` bigger
            elif currSum < target:
                left += 1
            
            # If neither of the above is true, we have found the solution
            else:
                # Remember that answer require 1-indexed solution
                return [left+1, right+1]
        
        return []

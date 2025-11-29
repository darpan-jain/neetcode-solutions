'''
Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Use two pointers and take advantage of the array being sorted, i.e. perform a Binary Search on the array to find the target sum

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        left, right = 0, len(numbers) - 1
        
        # This condition not needed since we are guaranteed a solution!
        while left < right:
            # Compute the sum using the current positions of `left` and `right`
            curr_sum = numbers[left] + numbers[right]

            # If the `curr_sum` is more than target, we move the `right` pointer to make smaller
            if curr_sum > target:
                right -= 1

            # Vice-versa of the first condition, we move the `left` pointer to make `curr_sum` bigger
            elif curr_sum < target:
                left += 1
            
            # If neither of the above is true, we have found the solution
            else:
                # Remember that answer requires 1-indexed solution
                return [left + 1, right + 1]
        
        return []

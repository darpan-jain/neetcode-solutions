"""
Question: https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary to store elements/numbers in `nums` as keys and their indices as value
        d = {}
        
        for idx, num in enumerate(nums):
            # If `target - curr num` is already parsed (and in the dictionary), you have a Two Sum pair!
            if target-num in d:
                return [d[target-num], idx]
                
            # Else, you keep saving the number (as key) and its index (as value)
            d[num] = idx

        # No final return statement needed since a solution is guaranteed (as per the problem statement).

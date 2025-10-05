"""
Question: https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dict to store each element `n` in `nums` as key and its index as value
        d = {}
        
        # Now iterate through `nums`
        for idx, curr_num in enumerate(nums):
            
            # If `target - curr num` is already parsed (and in the dict), 
            # you have a Two Sum pair!
            if target-curr_num in d:
                return d[target-curr_num], idx
                
            # Else, you keep saving the current number `n` and its index in the dict
            d[curr_num] = idx

        # No final return statement needed since a solution is guaranteed (as per the problem statement).

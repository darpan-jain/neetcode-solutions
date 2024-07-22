"""
Question: https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:

    """ Approach 1: Use set since it only holds unique values """

    # If length is 1, then obvs it is a unique number!
    if len(nums) < 2:
        return False

    # The length of `set(nums)` will not change if all elements are unique
    return len(nums) != len(set(nums))

    """ Approach 2: Use hashmap and create counter. Exit when count of a value goes above 1 """
    # counter = {}
    # for i in nums:
    #     if i in counter:  # Number already exists in counter, therefore duplicate
    #         return True
    # # Else add the char and init its counter
    #     else:
    #         counter[i] = 1

    # return False

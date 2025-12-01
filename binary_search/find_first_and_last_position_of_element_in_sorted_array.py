'''
Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''

from typing import List


class Solution:
    """
    Approach: Use Binary Search Twice to find the first and last positions

        Intuition:
            Since nums is a sorted array, use binary search to efficiently find the first and last positions of target
            When the target is found, continue searching (Why? Because there may be multiple occurrences of target in the array)
                - left for the first occurrence (to handle duplicates)
                - right for the last occurrence
    
        Running binarySearch twice, use a flag to indicate whether to search for the first or last occurrence:
            - searchFirst=True: find the first index by shifting the right boundary when target matches (since we need to find the earliest index)
            - searchFirst=False: find the last index by shifting the left boundary when target matches (since we need to find the last possible index)
            If the target is never found, return [-1, -1]

    Time Complexity : O(log N) for each binary search =  O(2 * log N) ~ O(log N)
    Space Complexity: O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.binarySearch(nums, target, searchFirst=True),
            self.binarySearch(nums, target, searchFirst=False)
        ]
    
    def binarySearch(self, nums, target, searchFirst):
        """
        Performs a binary search to find either the first or last occurrence of target
            - If searchFirst is True: when target is found, move right boundary left to find earliest index
            - If searchFirst is False: when target is found, move left boundary right to find latest index
        
        Returns the found index or -1 if target does not exist
        """

        l, r = 0, len(nums) - 1
        target_idx = -1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                # Record index and continue searching towards desired boundary
                target_idx = mid
                if searchFirst:
                    r = mid - 1  # searching first / earliest index, so keep searching left for first occurrence (to encounter the earliest index)
                else:
                    l = mid + 1  # searching last possible index, so keep searching right for last occurrence (to encounter the last possible index)
        
        # Return the found index or -1 if target does not exist
        return target_idx

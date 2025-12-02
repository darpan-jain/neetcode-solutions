'''
Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Use Binary Search to look for the minimum, but keep in mind that array is rotated so movements are opposite.
        
        Time Complexity: O(log N), since binary serach is used
        Space Complexity: O(1)
        """
        
        # Init two pointers to perform Binary Search
        left, right = 0, len(nums) - 1

        # Init result to +infinity (since we are looking for minimum)
        minNum = float('inf')
        
        while left <= right:

            # Edge case - when array is sorted! Just return the min value!
            if nums[left] < nums[right]:
                return min(minNum, nums[left])
            
            # Get the mid index
            mid = (left + right) // 2

            # Update the `minNum` by comparing with mid index element
            minNum = min(minNum, nums[mid])
            
            '''
            ## Check which part you want to search in the rotated array
            If nums[mid] is GREATER than leftmost value -> search the RIGHT portion of array, i.e.,`left = mid+1`
            else mid is SMALLER than leftmost -> search the LEFT portion of array, i.e. `right = mid-1`
            
            NOTE: This is the opposite logic to usual binary search due to the rotated array
            '''
        
            ''' Compare the nums[mid] and nums[left] (leftmost value in the array) '''

            # IF nums[mid] is NOT GREATER than nums[left] (leftmost value),
            # i.e. mid is LARGER, we have Overshot.
            # Usually we search in the left portion (by `r = mid - 1`), 
            # BUT since array is rotated, we search the RIGHT portion as it will have smaller values in the
            # rotated array, by moving left pointer to `mid + 1`

            if nums[mid] >= nums[left]:
                left = mid + 1
            
            # Conversely if nums[mid] is NOT GREATER than nums[left]
            # i.e. mid is SMALLER, we have Undershot. Then we search the LEFT portion 
            # by DECREMENTING the right pointer to `mid-1`
            else:
                right = mid - 1
                
        return minNum

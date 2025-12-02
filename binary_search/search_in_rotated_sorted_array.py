"""
Question: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Time complexity: O(log n)
        Use Binary Search to search with an additional leftmost
        and rightmost arrays (since the array is rotated)
        '''
        
        l, r = 0, len(nums) - 1
        
        # Iterate until both the pointers cross each other
        while l <= r:
            # Get the mid index
            mid = (l + r) // 2
            
            # If the target is equal to the mid value, we have our value!
            if target == nums[mid]:
                return mid
            
            ## Usual Binary search, check if we need to move right or left of `mid`
            
            # Since we have a rotated array, we also need to compare target with the 
            # leftmost values (for nums[l] < nums[mid] case)
            if nums[l] <= nums[mid]:

                # Here, target is greater than mid OR less than `l`
                if target > nums[mid] or target < nums[l]:
                # So, we search the right portion i.e. update the left pointer
                    l = mid + 1
                
                # If not, that means we have to search the left portion
                else:
                # So, update the right pointer
                    r = mid - 1
                
            # Here nums[l] > nums[mid], so we compare it with the rightmost element
            else:
                # Compare `target` with `mid` and rightmost element.
                # Note: the exact opposite conditions of the previous nested `if` statement.
                # if target <= nums[mid] and target >= nums[r]:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1

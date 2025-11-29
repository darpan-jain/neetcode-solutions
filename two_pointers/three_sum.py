'''
Question: https://leetcode.com/problems/3sum/
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute Force Aproach:
            Make combinations of 3 elements and check if the sum is zero for each -> doesn't handle duplicates
            Time Complexity  : O(N ^ 3)
            Space Complexity : O(1)

        Optimized Approach: 
            Sort the array, iterate and for current element, implement same solution as Sorted Two Sum (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
            Time Complexity  : O(N log N) for sorting + O (N ^ 2) for the 3 Sum algorithm = O(N^2)
            Space Complexity : O(N), to store the result in a new array
        """
        
        # Result array
        result = []

        n = len(nums)

        # Sorting taking `N log N` time. Allows us to skip duplicates! (check line 30)
        # `sort()` does in-place sorting, so no extra space used vs. `sorted()` which creates a new sorted array
        nums.sort()
        
        for i, curr_num in enumerate(nums):

            # Skip positive integers as first number (since you want the 3 Sum to be zero)
            if curr_num > 0:
                break
            
            # If duplicate value, go to next iteration
            if i > 0 and curr_num == nums[i-1]:
                # Since duplicate, skip to next iteration of `for` loop
                continue
            
            ''' After selecting first number, problem reduced to Two Sum (but for a sorted array) '''
            
            # Search on only the right side of the current number
            # Use two pointers -> left and right
            l, r = i + 1, n - 1
            
            # Search until left and right don't overlap
            while l < r:

                # Calculate the 3 Sum for current combination
                three_sum = curr_num + nums[l] + nums[r]
                
                # Sum is too big, move right pointer
                if three_sum > 0:
                    r -= 1
                
                # Sum is too small, move left pointer
                elif three_sum < 0:
                    l += 1
                
                # Match found, i.e., `three_sum == 0`, add the combination to result
                else:
                    # Add combination to result
                    result.append([curr_num, nums[l], nums[r]])

                    # Move left pointer to the next number in the list
                    l += 1
                    
                    # But we have to move to the next non-duplicate number
                    # This condition avoids using duplicate values as first number
                    while nums[l] == nums[l - 1] and l < r:
                        # Keep moving `l` until next non-duplicate number
                        l += 1
        
        # Return the final result
        return result

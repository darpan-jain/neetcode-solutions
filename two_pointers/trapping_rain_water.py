'''
Question: https://leetcode.com/problems/trapping-rain-water/
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Use two pointers to keep track of the max height on each end.
        Keep calculating the rain water at each element's position using - `min(leftMax, rightMax) - height at ith index`
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

        # Init the two pointers
        l, r = 0, len(height) - 1
        # Keeps track of the max height on the left and right of current position
        leftMax, rightMax = height[l], height[r]
        total_water = 0
    
        while l < r:
            
            # If leftMax is smaller, we shift the left pointer. Since we need `min(leftMax, rightMax)`
            if leftMax < rightMax:
                # Move the left pointer `l` and update `leftMax`
                l += 1
                leftMax = max(leftMax, height[l])
                # Also, add the water stored in the current element to `total_water`
                # using 
                total_water += leftMax - height[l]

            # Vice-versa if `rightMax < leftMax`
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total_water += rightMax - height[r]
        
        # Return the total rain water trapped
        return total_water
    
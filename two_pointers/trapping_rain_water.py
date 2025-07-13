'''
Question: https://leetcode.com/problems/trapping-rain-water/
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        """
        Approach: Use two pointers to traverse the height array from both ends.

        - Move the pointers towards each other based on the comparison of `leftMax` and `rightMax`
            - If `leftMax < rightMax`, it means the left side is shorter, so we can safely calculate the water trapped at the left pointer and move it to the right (l += 1)
            - If `rightMax < leftMax`, we calculate the water trapped at the right pointer and move it to the left (r -= 1)

        - The water trapped at each position is determined by the formula: `min(leftMax, rightMax) - height[i]`
            - `min(leftMax, rightMax)` since the water level at any position can only be as high as the shorter of the two sides
            - `height[i]` is subtracted because we cannot trap water above the height of the current bar
        - Keep calculating the rain water at each element's position using - `min(leftMax, rightMax) - height[i]`
        
        Time Complexity: O(N)
        Space Complexity: O(1)

        """
        
        # Empty or invalid input case
        if not height:
            return 0

        total_water = 0

        # Initialize two pointers `l` and `r` at the start and end of the `height` array
        l, r = 0, len(height)-1

        # Maintain `leftMax` and `rightMax` to keep track of the maximum heights encountered from the left and right sides
        leftMax, rightMax = height[l], height[r]

        # Traverse the height array until the two pointers meet
        while l < r:

            # Determines which side is shorter, i.e., which pointer to move
            if leftMax < rightMax:

                # Move the left pointer to the right
                l += 1
                # Update the left maximum height
                leftMax = max(leftMax, height[l])
                # Calculate the water trapped at the current left pointer position
                total_water += leftMax - height[l]
            
            # Here, rightMax height is smaller or equal to leftMax
            else:
                # Move the right pointer to the left
                r -= 1
                # Update the right maximum height
                rightMax = max(rightMax, height[r])
                # Calculate the water trapped at the current right pointer position
                total_water += rightMax - height[r]
        
        # Finally, return the total amount of water trapped
        return total_water
        
    
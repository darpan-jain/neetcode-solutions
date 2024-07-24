"""
Question: https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Use Two Pointers -> `left` and `right`, compare the volume of water held by each container and only
        move the pointer with the smaller height to get the most water in the next container.
        Also, keep track of the max volume of water held by any container.

        Time Complexity: O(N)        
        """
        
        # Init the two pointers on opposite ends of the list `height`
        left, right = 0, len(height)-1
        most_water = 0
        
        # Iterate until thw two pointers cross over
        while left < right:
            
            # The max level of water the container can hold depends on the shortest height of the container
            # i.e. min of height[left] or height[right]
            container_height = min(height[left], height[right])

            # Width of current container width will be dist b/w right and left i.e. `right - left`
            container_width = right - left
            
            # Now calculate the water held by current container i.e. calculate the area of container (rectangle)
            curr_water = container_height * container_width
            
            # Update max value of the `most_water` 
            most_water = max(most_water, curr_water)
            
            # Update the left and right pointers for the next iteration.
            # We remove the side with the smaller height (to get most water in the next container)
            # i.e. if 'left' height is less, we move left and vice-versa
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                        
        return most_water
    
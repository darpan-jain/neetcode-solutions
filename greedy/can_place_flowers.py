'''
Question: https://leetcode.com/problems/can-place-flowers/description/
'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Approach: Greedy Approach
        
        Goal is to determine if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule
            - Iterate through the `flowerbed` array
            - For each position, check if a flower can be planted:
                - The current position must be empty (0)
                - The previous position (if exists) must be empty (0)
                - The next position (if exists) must be empty (0)

        Time Complexity: O(N), where N = length of the flowerbed array
        Space Complexity: O(1)
        """

        for i in range(len(flowerbed)):
            # Check if current position is empty
            if flowerbed[i] == 0:
                
                # Check previous position (if exists)
                # Why (i == 0)? -> because if at start, no previous position
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                
                # Check next position (if exists)
                # Why (i == len(flowerbed) - 1)? -> because if at end, no next position
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both previous and next positions are empty, plant a flower here
                if prev_empty and next_empty:
                    flowerbed[i] = 1 # Plant flower
                    n -= 1 # Decrease the number of flowers to plant

                    # If all flowers have been planted, return True
                    if n == 0:
                        return True
        
        # If there are still flowers left to plant, return False
        return False

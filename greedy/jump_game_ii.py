'''
Question: Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/
'''


from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Perform a simplified BFS (since on a 1D array)

        Start from index 0 and keep updating a window with L and R, 
        based on how far you can jump using the elements in that window.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        # Result variable
        min_jumps = 0
        
        # Starting window will be both bounds at 0
        l, r = 0, 0

        # Iterate until right pointer reaches the end of `nums`
        while r < len(nums)-1:
            
            # This tracks the farthest index that can be reached using elements in the current window
            farthest = 0

            # Iterate through the current window from L to R and update farthest
            for i in range(l, r+1):
                # Current jump will be `i + number of available jumps nums[i]`
                # Update farthest if current reach is further
                farthest = max(farthest, i+nums[i])
            
            # After iteration entire window, update L and R
            # L = next index after right bound
            # R = furthest index that can be acheived using elements from last window
            l = r+1
            r = farthest

            # Increment result since one more iteration (jump completed)
            min_jumps += 1
            
        # The BFS while loop breaks when R pointer reaches or crosses end of `nums`, i.e., nums[n-1]
        # Finally, return the result
        return min_jumps

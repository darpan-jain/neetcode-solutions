'''
Question: https://leetcode.com/problems/jump-game/
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy Approach: 
        Iterate in reverse and keep moving the goal post closer to the
        start of the list. If our goal can reach the start of nums i.e., index 0 
        then return `True`
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        
        # Set the goal at the last index where we start iterating
        goal = len(nums) - 1
        
        # We iterate in reverse
        for i in range(len(nums)-1, -1, -1):
            # If we can reach the current goal index using the max steps in the current element `nums[i]`,
            # then update the goal's index, i.e. move it to `i` index
            # Meaning, we move the goal closer to the start of `nums`
            
            # Here we check if we can reach or surpass our goal (since we are iterating in reverse)
            # This is done by checking if the current index `i` + `value at nums[i]` can reach or exceed the current goal index
            # i.e., checking if you are at index `i`, can you reach the goal from that index
            if (i + nums[i]) >= goal:
                # If yes, we can now update goal index to `i`, moving it closer to start of `nums`
                goal = i
                
        # Finally, if goal has reached the start index i.e., 0 then return True
        return True if goal == 0 else False

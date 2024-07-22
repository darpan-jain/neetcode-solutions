'''
Question: https://leetcode.com/problems/jump-game/
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Approach: Iterate in reverse and keep moving the goal
        post closer to the start of the list. If we can reach the 
        start index i.e. 0, then return True
        Time Complexity = O(n)
        '''
        
        # Set the goal as the last index in the list
        goal = len(nums) - 1
        
        # We iterate in reverse
        for i in range(len(nums) - 1, -1, -1):
            '''
            If we can reach the current goal index using the max steps in the current
            element(nums[i]), then update the goal index i.e. move it to the ith index
            
            What does the condition mean? We check the next index we can reach 
            i.e. ith index plus the steps allowed using nums[i]
            So, `i + nums[i]` should be greater than the current goal index we have set!
            '''
            if (i + nums[i]) >= goal:
                goal = i
                
        # Finally, we check if the goal has reached to the start
        # if yes, then we can reach the end of the array
        return True if goal == 0 else False

'''
Question: https://leetcode.com/problems/house-robber/
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Look at the max value you can rob up until the last two nodes of the current node
        rob1, rob2 = 0, 0
        
        # List looks like this -> [rob1, rob2, n, n+1, ...]
        # Remember: cannot rob adjacent houses 
        for n in nums:
            # Save the max value of next robbery in a temp variable (since we need to swap)
            newMaxRob = max(rob1+n, rob2)
            # Move rob1 to value of rob2 AND update rob2 to newMaxRob value!
            rob1 = rob2
            rob2 = newMaxRob
        
        # The final max value is stored in 'rob2' (which has the value of newMaxRob)
        return rob2
            
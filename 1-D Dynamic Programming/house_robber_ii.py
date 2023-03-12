'''
Question: https://leetcode.com/problems/house-robber-ii/
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Similar to Robber 1, but now the list is circular (first and last elements are connected)!
        So, reuse the solution and run the robber 1 method for all values except first and last in the list.
        i.e. exclude nums[1:] and nums[:-1] (since the first and last element are connected! i.e. circular)
        '''
        
        # Edge case - if only one house, then return the value of that house
        if len(nums) == 1:
            return nums[0]
                
        # Just run the rob function excluding the first and last elements in 'nums'
        return max(self.robNonCircular(nums[1:]), self.robNonCircular(nums[:-1]))
    
    # Helper Function to find max rob value for the given list of houses 'arr'
    def robNonCircular(self, arr):
        # Same approach as https://leetcode.com/problems/house-robber/
        rob1, rob2 = 0, 0
        for n in arr:
            newRob = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
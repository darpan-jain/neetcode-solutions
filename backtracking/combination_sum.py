'''
Question: https://leetcode.com/problems/combination-sum/
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' Perform a DFS on the given list of candidates '''
        
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    # Helper function for DFS
    def dfs(self, nums, target, curr_path, res):
        # Base case - Return since target not an exact match
        if (target < 0):
            return
        
        # If target exactly zero, we found a combination
        if (target == 0):
            # Add the current path to the result
            res.append(curr_path)
            # print(f'\nNew Path added -> {res}\n')
            return
        
        # Iterate over the list of nums from i to n
        for i in range(len(nums)):
            # print(f'Curr = {nums[i]}, Nums = {nums}, New Target = {target}, Path = {curr_path}, res = {res}')
            
            # Pass 4 params to the DFS function for each element in 'nums'
            # 1. New candidates will be 'i'th element onwards -> nums[i:]
            # 2. Subtract current number from target -> 'target - nums[i]' before recursive call
            # 3. Add the curr nums to the new potential path -> 'path+[nums[i]]'
            # 4. Pass the result array
            new_target = target - nums[i]
            self.dfs(nums[i:], new_target, curr_path+[nums[i]], res)

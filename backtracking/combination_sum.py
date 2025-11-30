'''
Question: https://leetcode.com/problems/combination-sum/
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Backtracking + DFS

            - Define a helper DFS function that takes 4 parameters:
                1. nums: List of candidate numbers
                2. target: Remaining target sum to achieve
                3. curr_path: Current combination being explored
                4. res: Result list to store valid combinations
            - For each recursive call:
                - If target < 0: return (invalid path)
                - If target == 0: append `curr_path` to res (valid combination found)
                - Then make recursive calls to DFS for each number in nums by passing:
                        - New candidates starting from current index (to allow reuse)
                        - Updated target (target - current number)
                        - Updated `curr_path` (adding current number)
                        - `res` to store the final result combinations

        Time Complexity: O[2 * (T / m)]
            - T is the target value
            - m is the minimum value in candidates
            Why?
                - The maximum depth of the recursion tree can go up to T / m (when we keep choosing the smallest number)
                - At each level, we have at most 2 choices (to include or exclude a number)
                - Thus, the total number of nodes in the recursion tree can be approximated to 2^(T/m) 

        Space Complexity: O(T / m)
        """
        
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    # Helper DFS function for searching combinations
    def dfs(self, nums, target, curr_path, res):
        # Base case - Return since target not an exact match
        if (target < 0):
            return
        
        # If target exactly zero, we found a combination
        if (target == 0):
            # Add the `curr_path` to the result
            res.append(curr_path)
            return
        
        # Iterate over the list of nums
        for i, curr_num in enumerate(nums):
            # print(f'Curr = {curr_num}, Nums = {nums}, New Target = {target}, Path = {curr_path}, res = {res}')
            
            '''
            Pass 4 params for the recursive DFS call for each element in `nums`
                1. New candidates will be 'i'th element onwards -> nums[i:]
                2. Subtract current number from target -> `target - nums[i]` before recursive call
                3. Add the curr nums to the new potential path -> `path + [nums[i]]`
                4. Pass the result array
            '''
            new_target = target - curr_num
            self.dfs(nums[i:], new_target, curr_path + [curr_num], res)

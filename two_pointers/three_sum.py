'''
Question: https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Brute force Approach: Make combinations of 3 elements and check if the sum is zero for each -> doesn't handle duplicates

        Optimal method: Sort the array, iterate and for current element, then implement 
        same solution as Sorted Two Sum!
        
        Time Complexity  : O(n log n) for sorting + O (n ^ 2) for the 3 Sum algorithm = O(n^2)
        Space Complexity : O(n), since we store the result in a new array
        '''
        
        result = []
        n = len(nums)

        # Sorting taking 'n log n' time. Allows us to skip duplicates! (check line 30)
        nums.sort()
        
        for i, curr_num in enumerate(nums):

            # Skip positive integers as first number (since you want the 3 Sum to be zero)
            if curr_num > 0:
                break
            
            # If duplicate value, go to next iteration
            if i > 0 and curr_num == nums[i-1]:
                # Since duplicate, skip to next iteration of `for` loop
                continue
            
            # After selecting first number, problem reduced to Two sum 
            # i.e. Now the solution is same as Two Sum II (two sum but for sorted array)
            
            # Search on only the right side of the current number
            # `l` -> left pointer & `r` -> right pointer
            l, r = i+1, n-1
            
            # Search until left and right don't overlap
            while l < r:
                threeSum = curr_num + nums[l] + nums[r]
                
                # Sum is too big, move right closer
                if threeSum > 0:
                    r -= 1
                
                # Sum is too small, move left closer
                elif threeSum < 0:
                    l += 1
                
                # Match found, store the 3 numbers
                else:
                    result.append([curr_num, nums[l], nums[r]])
                    # Remember to move to the next number in the list
                    l += 1
                    
                    # Once you have found a 3 Sum combination, move to the next
                    # non-duplicate number as the first number.
                    # This condition avoids using duplicate values as first number.
                    while nums[l] == nums[l-1] and l < r:
                        # Keep moving `l` until next non-duplicate number
                        l += 1
                    
        return result
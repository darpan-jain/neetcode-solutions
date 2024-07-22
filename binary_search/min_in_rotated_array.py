'''
Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Use the binary_search, while looking for the minimum.
        Time Complexity: O(log n)
        '''
        
        # Init two pointers to perform binary_search
        start, end = 0, len(nums) - 1

        # Init result to +infinity (since we are looking for minimum)
        minNum = float('inf')
        
        while start <= end:

            # Edge case - when array is sorted! Just return the min value!
            if nums[start] < nums[end]:
                return min(minNum, nums[start])
            
            # Get the mid index
            mid = (start + end) // 2

            # Update the `minNum` by comparing with mid index element
            minNum = min(minNum, nums[mid])
            
            ## Check which part you want to search in the rotated array
            
            # We compare the mid value and the leftmost value

            # If mid is greater (we have overshot), usually we decrement right pointer (i.e. search left part), 
            # BUT since array is rotated, we search the RIGHT portion as it will have smaller values.
            if nums[mid] >= nums[start]:
                start = mid + 1
            
            # Similarly, if not (nums[m] <= nums[l] is satisfied), we have undershot, we search 
            # the LEFT portion (as opposed to usual right portion search), as now that will have smaller values.
            else:
                end = mid - 1
                
        return minNum

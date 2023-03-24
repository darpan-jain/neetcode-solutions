'''
Question: https://leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Notice that a start of a sequence has no number before it.
        So we check start of a seq by checking if there is a number before the element,
        and end by checking if we have a number after the element.
        Time and Space Complexity: O(n)
        '''
        
        # Create a set out of the list of numbers - so that we don't have any duplicates
        numSet = set(nums)
        longest = 0
        
        for curr in nums:
            
            # Check if the current number is the start of a sequence
            # by checking if the `curr-1` number exisits
            if curr-1 not in numSet:
                
                # If not then, then this is the start of a sequence
                # Initialize the length of the current sequence
                seq_len = 1
                
                # Keep incrementing `seq_len` until the next number exists
                while (curr + seq_len) in numSet: 
                    seq_len += 1
                
                # Once you have reached the end of the sequence
                # Update the length of the longest sequence
                longest = max(longest, seq_len)

        return longest                

"""
Question: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Approach: Notice that a start of a sequence has no number before it.
        So we check start of a seq by checking if there is a number before the element,
        and end of sequence by checking if we have a number after the element.
        Do this for all elements in the list and keep track of the longest sequence.

        Time and Space Complexity: O(N)
        """
        
        # Create a set out of the list of numbers - so that we don't have any duplicates
        # This is an important consideration for edge cases, especially when `len(nums)` is extremely large.
        num_set = set(nums)
        longest = 0
        
        for curr in nums:
            
            # Check if the current number is the start of a sequence
            # by checking if the `curr-1` number exists
            if curr-1 not in num_set:
                
                # If not, then this is the start of a sequence
                # Initialize the length of the current sequence
                seq_len = 1
                
                # Keep incrementing `seq_len` until the next number exists
                while (curr + seq_len) in num_set:
                    seq_len += 1
                
                # Once you have reached the end of the sequence (when the `while` loop breaks),
                # Update the length of the longest sequence
                longest = max(longest, seq_len)

        return longest                

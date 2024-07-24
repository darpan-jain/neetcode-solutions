'''
Question: https://leetcode.com/problems/sliding-window-maximum/
'''

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Use a monotonically decerasing deque to keep track of the max value in each window.
        The deque will have the maxValue at the start of the queue (rightmost position).
        
        Sliding window implemented using two pointers.

        Time Complexity: O(n)
        '''

        output = []
        # Pointers for sliding window
        l = r = 0
        # Monotonically decreasing deque (left to right) i.e. max value at index 0 of the queue
        q = collections.deque() # Store the indices NOT the actual value

        # Iterate until the right pointer exceeds length of `nums`
        while r < len(nums):

            # If current number greater than rightmost value in queue, pop values from right until this is False
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            # Then add the current number to the queue, this now adds the new max value to the queue
            # Note: We append indices of the element to the queue, not the value!
            q.append(r)

            # Also, check if the left value is within the window bounds. If not, remove it.
            if l > q[0]:
                q.popleft()
            
            # Check if the window is at size `k` and add the current max (stored in the leftmost pos i.e. index 0) from queue
            if (r + 1) >= k:
                output.append(nums[q[0]])
                # Also increment the left pointer (i.e. move the window to the right)
                l += 1
            
            # Also, do the same for the left pointer
            r += 1

        # Finally, return the `output` array
        return output

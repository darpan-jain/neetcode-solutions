
'''
Question: https://leetcode.com/problems/non-overlapping-intervals/
'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy Approach 1: Sort intervals by starts

        How to check if two intervals overlaps?
            - IF curr_start <= prevEnd, 
            i.e., if the current start interval starts before the previous interval ends
        
        While deleting overlapping intervals, we retain the min of the two intervals' ends, 
        thus deleting the interval with the larger end value
        Why? Since we want to ensure that the same interval does not merge with other intervals and
        also this also helps us MINIMIZE the number of interval deletes
        
        Time Complexity: O(N log N) -> `log N` for sorting, and `N` to iterate list of N `intervals`
        Space Complexity: O(1) -> One single variable `deleted` to store the result
        '''
        
        # Sort the input `intervals` based on start values
        # Done so that we only compare the adjacent intervals.
        intervals.sort(key = lambda pair: pair[0])

        # Result to store the number of interval deletes
        deleted = 0

        # Store the end of the first interval for comparisons
        prevEnd = intervals[0][1]
        
        # Iterate through the remaining intervals
        for curr_start, curr_end in intervals[1:]:
            
            # NO OVERLAP, if the `current start <= previous end`
            if curr_start >= prevEnd:
                # So we just update the `prevEnd` to `curr_end`
                prevEnd = curr_end
            
            # OVERLAPPING, so we have to delete one interval
            # Which one? The one with the larger end value, so keep the minimum end of the two intervals. 
            # Why? Since we want to minimize the number of deletes, and this ensures
            # that the current intervals don't overlap with other intervals in the list
            else:
                prevEnd = min(prevEnd, curr_end)
                deleted += 1
        
        # Return the number of deletes
        return deleted

        """
        Greedy Approach 2: Sort intervals by ends
        Same approach as Approach 1, but sort intervals by ends instead of starts.

        In this approach, since we are sorting by ends, we don't need to check if the current interval overlaps with other intervals in the list.
        This saves us the effort of finding the minimum end of the two intervals.
        How?
        We can simply not update `prevEnd` in this case, and increment the `deleted` counter.
        This is the same as deleting the current interval.

        Time Complexity: O(N log N) -> `log N` for sorting, and `N` to iterate list of N `intervals`
        Space Complexity: O(1) -> One single variable `deleted` to store the result
        """

        # Sort the input `intervals` based on end values
        intervals.sort(key = lambda pair: pair[1])

        # Result to store the number of interval deletes
        deleted = 0

        # Store the end of the first interval for comparisons
        prevEnd = intervals[0][1]

        # Iterate through the remaining intervals
        for curr_start, curr_end in intervals[1:]:

            # OVERLAPPING, since the prevEnd > curr_start, i.e., the current interval starts before the previous interval ends
            # (same as the case for overlap in Approach 1 in the `else` block)
            if prevEnd > curr_start:
                # Here we have to delete one interval, so we increment the `deleted` counter
                # But we do no update `prevEnd` since we have already sorted `intervals`  based on ends so prevEnd is already the smallest end we have seen so far
                # not updating `prevEnd` in this case, is the same as deleting the current interval
                deleted += 1
            
            # NO OVERLAP, so we just update the `prevEnd` to `curr_end`
            else:
                prevEnd = curr_end
        
        return deleted

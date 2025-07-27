'''
Question: https://leetcode.com/problems/insert-interval/
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """ 
        Approach: Three cases for handling `newInterval` when adding to `intervals`
            - To be added before an interval (no overlap)
            - To be added after an interval (no overlap)
            - To be merged with another interval (overlap with another interval)

        For no overlap:
            - IF end of new interval < start of curr interval -> ADD BEFORE
            - IF start of new interval > end of curr interval -> ADD AFTER
        
        For overlap:
            New Interval boundaries = min of starts & max of ends
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        
        res = []
        
        # Iterate through all intervals
        for i in range(len(intervals)):
            
            # Extract the start and end of current interval
            curr_start, curr_end = intervals[i]

            # No Overlap, merge BEFORE current interval
            # Check if the new interval can be merged BEFORE the current interval
            if newInterval[1] < curr_start:
                # We append the newInterval to the result first
                res.append(newInterval)
                # Then add the result (with new and previous intervals) and 
                # all other intervals from ith index to the end.
                # Now we don't need to check, so we return the result
                return res + intervals[i:]
            
            # No Overlap, merge AFTER current interval
            # Checks if the interval can be merged after the end of the current interval
            elif newInterval[0] > curr_end:
                # Here we only add current interval to `res` and keep checking
                # since the newInterval can be merged after or overlap with other intervals too!
                # So we only append the current interval, and keep going forward.
                res.append(intervals[i])
            
            # Overlap, create new merged interval boundaries ->  min of starts and max of ends
            else:
                newInterval = [ min(newInterval[0], curr_start),
                                max(newInterval[1], curr_end) ]
            
        # Finally, add the new merged interval to `res` (outside of the for loop), 
        # since not done during the No Overlap+Merge After and the Overlap+New Interval Boundaries cases
        res.append(newInterval)
        return res

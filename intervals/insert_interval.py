'''
Question: https://leetcode.com/problems/insert-interval/
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach: 
            When inserting, check if they are merging.
            If they are, the new interval is the min of starts and max of ends

        How to check where to add the new interval (in case of no-overlap)?
                                     IF
            - end of new interval < start of curr interval, then add before 
                                  ELSE IF
            - start of new interval > end of curr interval, then add after
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        
        res = []
        
        for i in range(len(intervals)):
            
            # Extract the start and end of current interval
            curr_start, curr_end = intervals[i]

            # No overlap, to be merged before current interval
            # Check if the new interval can be merged BEFORE the current interval
            if newInterval[1] < curr_start:
                # We append the newInterval to the result first
                res.append(newInterval)
                # Then add the result (with new and previous intervals) and 
                # all other intervals from ith index to the end.
                # Now we don't need to check, so we return the result
                return res + intervals[i:]
            
            # No overlap, new to be merged AFTER current interval
            # Checks if the interval can be merged after the end of the current interval
            elif newInterval[0] > curr_end:
                # Here we add the current interval, and keep checking since the newInterval
                # could be merged after other intervals too!
                # So we only append the current interval, and keep going forward.
                res.append(intervals[i])
            
            # Overlap case, so we create the new merged interval using 
            # -> min of starts and max of ends
            else:
                newInterval = [ min(newInterval[0], curr_start),
                                max(newInterval[1], curr_end) ]
            
        # We add the new merged interval to the result (for elif and else cases)
        res.append(newInterval)
            
        return res

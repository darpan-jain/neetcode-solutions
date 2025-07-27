'''
Question: https://leetcode.com/problems/merge-intervals/
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: To determine if two interval `i1` and `i2` are overlapping, i.e., can be merged, 
        compare their outer and inner boundaries.

                     i1_end >= i2_start 
                      ---------------
                      |             |
        [i1_start, i1_end]      [i2_start, i2_end]
            |                                |                      
             ---------------------------------
                    i2_end >= i1_start

        Only Two conditions for overlap:
            - i1_end >= i2_start 
            - i2_end >= i1_start
        
        When two such intervals found, new boundaries are
            `new start` = min of starts
            `new end` = the max of ends
        -> [min(i1[0], i2[0]), max(i1[1], i2[1])]
        
        Why sort the input `intervals`?
            Sorting ensures that we just compare adjacent pairs of intervals,
            instead of restarting the iteration everytime we merge two intervals and then restart until 
            we find no more overlapping intervals. This approach would lead to O(N^2) time complexity.
        
        Also, by sorting, one of the conditions for determining overlap 
        is already satisfied -> `i2_end >= i1_start`
        
        Time Complexity: O(N log N) -> `log N` for the sorting and `N` to merge
        Space Complexity: O(N) (since saving the result in a new list)
        """
        
        # Sort input based on start value to compare only adjacent intervals (optimizes the solution)
        intervals.sort(key = lambda pair: pair[0])

        # Maintain a list of sorted and merged intervals
        # First interval added to the `merged` list to avoid edge cases.
        merged = [intervals[0]]
        
        for curr_start, curr_end in intervals:
            
            # Extract the end of the last interval in the result `merged`
            lastEnd = merged[-1][1]

            # After sorting we only check current start being <= than last interval's end
            if curr_start <= lastEnd:
                # If overlapping, we merge the intervals by updating the last interval of the sorted `merged` list
                # new end = max of the two ends
                merged[-1][1] = max(lastEnd, curr_end)
                
            # If no overlap, then we just add the current interval to the end of the result `merged`
            else:
                merged.append([curr_start, curr_end])
        
        return merged
    
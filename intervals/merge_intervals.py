class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        '''
        Two intervals i1 and i2 overlap only if i1[1] >= i2[0] and i2[1] >= i1[0] or vice-versa.
        i.e. Both intervals' ENDS >= STARTS
        
        So, whenever we find two such intervals, we need to merge them as -
        new `start` is min of the starts, and the new `end` is the max of the ends!
        -> newLimits = [min(i1[0], i2[0]), max(i1[1], i2[1])]

        Sorting ensures that we just compare adjacent pairs of intervals,
        instead of restarting the iteration everytime we merge two intervals and then restart until 
        we find no more overlapping intervals. This approach would lead to O(n^2) time complexity.
        
        By sorting, one of the condition of overlap is already satisfied -> i2[1] >= i1[0] (the second condition for merging!)
        i.e. End of second interval will always be greater that the start of the first.
        
        Time Complexity = O(n log n) -> 'log n' for the sorting and 'n' to merge
        Space Complexity = O(n) (since saving the result in a new list)
        '''
        
        # Sort based on START limit to compare only adjacent intervals
        intervals.sort(key = lambda pair: pair[0] )
        # Maintain a list of sorted and merged intervals
        merged = [intervals[0]]
        
        # After sorting we only check current STARTs being less than the last interval's end.
        for start, end in intervals[1:]:
            
            lastEnd = merged[-1][1]
            # If overlapping, we merge the intervals by updating the last interval of the sorted list
            if lastEnd >= start:
                # the new `end` is the max of the two ends
                merged[-1][1] = max(lastEnd, end)
                
            # If no overlap, then we just add the current interval to the end of the sorted list
            else:
                merged.append([start, end])
        
        return merged
    
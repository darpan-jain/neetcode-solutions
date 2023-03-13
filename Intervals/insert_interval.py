'''
Question: https://leetcode.com/problems/insert-interval/
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ''' 
        When inserting, check if they are merging.
        If they are, the new interval is the `min of starts` and `max of ends`

        How to check where to add the new interval (in case of no-overlap)?
                                        IF
        - end of new interval < start of curr interval, then add before 
                                      ELSE IF
        - start of new interval > end of curr interval, then add after
        
        Time Complexity = O(n) 
        '''
        
        res = []
        
        for i in range(len(intervals)):
            # No overlap, to be merged before current interval
            if newInterval[1] < intervals[i][0]:
                # Here, we don't need to check, so we return the result
                res.append(newInterval)
                return res + intervals[i:]
            
            # No overlap, new to be merged after current interval
            elif newInterval[0] > intervals[i][1]:
                # Here we add the current interval, and keep checking since the newInterval
                # could be merged AFTER other intervals too!
                res.append(intervals[i])
            
            # Overlap case, we create the new merged interval - min of starts and max of ends
            else:
                newInterval = [ min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1]) ]
            
        # We add the new merged interval to the result (for elif and else cases)
        res.append(newInterval)
            
        return res

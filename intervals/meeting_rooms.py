'''
Question (Leetcode Premium): https://leetcode.com/problems/meeting-rooms/
Neetcode Version: https://neetcode.io/problems/meeting-schedule
'''

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Greedy Approach:
        
        Sort based on start values and compare two adjacent meetings (meet 1 and meet 2)
        If meeting 2 starts before meeting 1 ends (i.e., meet1.end > meet2.start), there's a conflict and return False.

        Time Complexity: O(N log N) -> sorting in `log N` and iterating `N` meetings in input list
        Space Complexity: O(1) -> no extra space to store the result
        """

        # Sort the input `intervals` based on start values
        intervals.sort(key = lambda i: i.start)

        # Iterate the intervals in pairs
        for i in range(1, len(intervals)):
            
            meet1 = intervals[i-1]
            meet2 = intervals[i]

            # CONFLICT OR OVERLAP if meeting 2 starts before meeting 1 ends
            if meet1.end > meet2.start:
                return False
        
        # If for loop completes with no conflicts, possible to attend all meetings
        return True

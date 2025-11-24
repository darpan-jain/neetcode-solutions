'''
Question (Leetcode Premium): https://leetcode.com/problems/meeting-rooms-ii/
Neetcode Version: https://neetcode.io/problems/meeting-schedule-ii
'''

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Approach: Maintain two counters 
            - `s` -> tracks the number of ongoing / started meetings
            - `e` -> tracks the number of finished / ended meetings
            - `occupied` -> tracks the current number of occupied rooms

        1. Each time a meeting starts (start < end), occupy a room and increment `s`
        2. Each time a meeting ends, unoccupy the room and increment `e`
        3. Maintain a maxRooms variable that keeps track of the max number of room occupied during each iteration.

        Time Complexity: O(N log N) -> `log N` for sorting the start and end values, `N` to iterate through the input `intervals`
        Space Complexity: O(N) -> to store the `N` starts and ends from the input interval
        """

        # Store sorted values of starts and ends of meetings in `intervals`
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        # Maintain an occupied counter and a result to store the max number of occupied rooms for each iteration
        occupied, maxRooms = 0, 0

        # Maintain `s` and `e` counters for tracking
        # num of meetings started and ended
        s, e = 0, 0

        # Iterate through both the lists of start and end times
        # We're checking `s` as the end condition, since the starts will 
        # always be before the end times.
        while s < len(intervals):

            # 1. Check if a meeting has started by checking 
            # if the start time of the current meeting is before the end time of the previous meeting
            if starts[s] < ends[e]:
                # If started -> Increment `s` and occupy a room
                s += 1
                occupied += 1
            
            # 2. Check if a meeting has end
            else:
                # If ended -> Increment `e` and unoccupy room
                e += 1
                occupied -= 1
            
            # 3. Update `maxRooms` based on current number of rooms occupied
            maxRooms = max(maxRooms, occupied)

        # The result in `maxRooms` will have the max number of rooms required to be occupied for the given schedule in `intervals`
        return maxRooms

'''
Question: https://leetcode.com/problems/high-access-employees/
'''


from typing import List
from collections import defaultdict


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        """
        Approach:
          1. Group access times by employee
          2. Convert HHMM strings to integers and sort per employee
          3. For each consecutive triple, if times[i+2] - times[i] < 100 mark employee

        Why '< 100' works:
          Access time is represented in HHMM = HH * 100 + MM
          Let `start = HH1*100 + MM1`, `end = HH2*100 + MM2`

            Case 1: HH2 == HH1 -> end - start = MM2 - MM1 (< 100 implies < 60 real minutes)
            Case 2: HH2 == HH1 + 1 -> end - start = 100 + (MM2 - MM1)
                For this to be < 100 we need (MM2 - MM1) < 0
                Real minutes difference = 60 + (MM2 - MM1) < 60
          
          So end - start < 100 guarantees strictly less than 60 actual minutes without conversion

        Examples (triples where first and third determine the window):
          - Same hour: 0800, 0830, 0855 -> 0855 - 0800 = 55 (<100) => 55 minutes
          - Crossing hour: 0955, 1005, 1008 -> 1008 - 0955 = 53 (<100) => 13 minutes
          - Crossing hour (minute decreases): 0955, 1001, 1003 -> 1003 - 0955 = 48 (<100) => 8 minutes

        Edge note:
          Exactly 60 minutes apart (e.g. 0959 ... 1059) gives difference 100 (not <100) and is excluded
          If an inclusive 60-minute window is required, convert HHMM to total minutes and use <= 60

        Time Complexity: O(N log N), due to sorting access times per employee
        Space Complexity: O(N), for storing access times
        """

        # Dict to group access times by employee
        access_times = defaultdict(list)

        # Populate the dictionary with access times for each employee
        for v in access_times:
            a, b = v
            access_times[a].append(int(b))

        # Result list to store employees with high access frequency
        res = []

        # Iterate through each employee and their access times
        for emp, times in access_times.items():
            
            k = len(times) # number of access times
            times.sort() # sort access times
            flag = False # flag to indicate if employee meets high access criteria

            # Check for consecutive access times within 100 minutes
            for i in range(k - 2):
                flag |= times[i + 2] < times[i] + 100
            
            if flag:
                res.append(emp)
            
        return res

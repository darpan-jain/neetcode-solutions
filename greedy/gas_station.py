'''
Question: https://leetcode.com/problems/gas-station/
'''

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Greedy Approach: 
        Iterate through the list and keep track of the total gas and cost. 
        If at any point, the total gas is less than the total cost, then we cannot start from that index.
        We can reset our starting point to the next index and continue iterating until we find a valid starting point.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        # Edge case: If total gas is less than total cost for all routes, not possible 
        # to make the round trip, so we return -1
        if sum(gas) < sum(cost):
            return -1
        
        # Define the variable `remaining_gas` that maintains the total gas available so far in our trip
        remaining_gas = 0

        # Result variable to track the ideal starting index
        start_index = 0

        # Now iterate through all start positions, i.e., indices in `gas`
        for i in range(len(gas)):

            # At every step of the trip, the `remaining_gas` would be the difference of 
            # the available gas at the current index (gas[i]) and the cost to the next point (cost[i])
            remaining_gas += (gas[i] - cost[i])

            # If at any point, we get negative `remaining_gas`, we can't start from the current index `i`
            if remaining_gas < 0:
                # Reset `remaining_gas` and move set the result `start_index` to the next one
                remaining_gas = 0
                start_index = i + 1

        # The question mentions that we have always have a solution, so after completion of for loop, 
        # we'll end up at the right `start_index`         
        return start_index

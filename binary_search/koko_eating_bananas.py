'''
Question Link: https://leetcode.com/problems/koko-eating-bananas/
Neetcode Link: https://neetcode.io/problem/koko-eating-bananas
'''

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Approach: Frame the problem as a Binary Search problem
        
        Search for minimum/optimal `k` such that koko can eat all bananas from `piles` in `h` hours

        Time Complexity: O(N log M),
                - N = number of piles
                - M = maximum number of bananas in a pile
        
        Space Complexity: O(1), since no extra space is used other than a few pointer variables
        """

        # Constraints for binary search (i.e., the value of k), which would be between 1 and the maximum number of bananas in a pile
        l, r = 1, max(piles)
        optimal_k = r  # Initialize the result to the maximum possible value of `k` i.e., max(piles)

        # Iterate until the left pointer is less than or equal to the right pointer
        while l <= r:

            # Calculate the mid-point of the current search space, which represents the current eating speed `k`
            k = (l + r) // 2

            # Calculate the total time taken to eat all bananas at the current eating speed `k`
            # But it's a possible solution, so we store the value to `optimal_k`
            total_time = 0
            for p in piles:
                # To go through a pile of size `p` at speed `k`, it would take `ceil(p / k)` hours 
                # (since Koko can only eat in whole hours and can't move to the next pile until the current pile is fully finished)
                total_time += math.ceil(p / k)
            
            ''' Now, Compare the current `total_time` with `h` to decide how to adjust our search space (to calculate a new `k`) '''

            # total_time < h means Koko is eating too fast, so we can try a smaller `k` (move the right pointer to mid - 1)
            if total_time <= h:
                optimal_k = k  # Update the optimal_k to the current valid `k`
                r = k - 1 # Update the right pointer to `k - 1`, i.e., search for a potentially smaller valid `k`
                # Note: this could be the optimal_k, but we don't return it yet, because there might be a smaller `k` that also works
            
            # If total_time > h, that means Koko is eating too slow, so we need to increase `k` (by moving left pointer `l` to mid + 1)
            else:
                l = k + 1

        # Finally, we return the optimal_k found, either stored from the `if total_time <= h` condition, or the initial value of `max(piles)` if no valid `k` was found
        return optimal_k

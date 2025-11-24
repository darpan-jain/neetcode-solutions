'''
Question Link: https://leetcode.com/problems/hand-of-straights/
'''

from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Brute Force Approach: 
            - Sort the hand and iterate through it
            - For each card, try to create a straight hand of size `groupSize` starting from that card
                - If at any point, we cannot create a straight hand, return False
                - If we can create a straight hand for all cards, return True

        Time Complexity: O(N log N)
        Space Complexity: O(N) for the Counter and memory for sorting
        """

        # Edge case: If len(hand) % groupSize, i.e. not 0 (interpreted as False), 
        # then not possible to create the hand of straights
        if len(hand) % groupSize:
            return False
    
        # Create a Counter of all values in `hand`
        count = Counter(hand)
        
        # Also sort hand so that we are always moving in increasing order of card values
        hand.sort()

        # Iterate through all card values in `hand` (now sorted in increasing order)
        for num in hand:

            # If the card with the value still exists in the `count`
            if count[num]:
                
                # Start creating the consequtively increasing straight hand
                for i in range(num, num + groupSize):
                    # If at any point, the chain breaks, then immediately return False
                    if not count[i]:
                        return False

                    # If at least 1 count for current number `i` exists, 
                    # then just deduct 1 from the count[i] and move to next number in the straight hand
                    count[i] -= 1
        
        # If the function doesn't return False at any point in the above loop, 
        # then we have a solution!
        return True

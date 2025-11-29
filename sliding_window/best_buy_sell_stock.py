"""
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach: Sliding Window
            
            - Set first element as starting buy price
            - Maintain a result variable `profit` to keep track of max profit
            - Iterate over the prices starting from 2nd element
                - If current price is less than buy price, update buy price
            - For every iteration, update profit as max of (current price - buy price) and previous profit
        
        Time Complexity: O(N), where N is number of prices
        Space Complexity: O(1)
        """

        # Choose first element as buy price and initial profit as 0
        buy, profit = prices[0], 0
        
        # Iterate over the prices but skip first element since that is assigned to current buy price
        for curr_price in prices[1:]:
            
            # If you find a lower price than current buy price, that's your new buy price
            if curr_price < buy: 
                buy = curr_price
                
            # Keep updating profit to 'max b/w (curr buy price - previous buy price) and profit'
            profit = max((curr_price - buy), profit)

        return profit

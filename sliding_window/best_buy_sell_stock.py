"""
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
'''
Question: https://leetcode.com/problems/coin-change/
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 
        Approach: Bottom Up Dynamic Programming

        1. Create a DP array of size `amount + 1` (to include 0 to amount) and initialize each value to a max value (i.e. `amount + 1` or infinty)
        2. Set the base case dp[0] = 0, since amount 0 requires 0 coins
        3. Iterate over each amount from 1 to amount
        4. For each amount, we iterate over each coin in coins
        5. If the current amount minus the coin value is non-negative, we update the dp array at the current amount index with the minimum of its current value and `1 + dp[amount - coin]`
        6. Finally, check if `dp[amount]` is still the max value, if so, we return -1 (indicating no solution), otherwise return `dp[amount]` which will have the min coins required
        
        Time Complexity = O(amount * num of coins)
        Space Complexity = O(amount)
        """
        
        # Init `dp` of size `amount` with each initial set at max (can use either infinity or amount + 1 for this)
        dp = [amount + 1] * (amount + 1)
        
        # Base case - amount 0 will require zero coins
        dp[0] = 0
        
        # Iterate over the amount, starting at 1 (bottom-up)
        for a in range(1, amount + 1):
            
            # Also iterate over the coins available
            for c in coins:
                ''' For each (a, c) combination, check if we have a match and 
                store the min value so far (for the amount `a`) in the dp '''
                
                # If the current amount 'a' minus the current coin value is valid (i.e. greater than or equal to 0),
                # then we store the minimunm number of coins required in the DP
                if a - c >= 0:
                    # Update the value in `dp[a]`
                    # `1` is added since we used the current coin `c` for getting the current result
                    # So `dp[a]` will store the value of the min of itself and the new value
                    # i.e. `1 + dp[a-c]` (using the previous value from the DP)
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # Check if `dp[amount]` is still the max value, if so, we return -1 (indicating no solution), 
        # otherwise return `dp[amount]` which will have the min coins required
        return dp[amount] if dp[amount] != amount + 1 else -1

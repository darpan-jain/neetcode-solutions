'''
Question: https://leetcode.com/problems/coin-change/
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ''' Use a bottom up approach i.e. DP approach -> Time Complexity = O (amount * num of coins)'''
        
        # Init `dp` of size `amount` with each initial set at max (can use either infinity or amount + 1 for this)
        dp = [amount+1]*(amount+1)
        
        # Base case - amount 0 will require zero coins
        dp[0] = 0
        
        # Iterate over the amount, starting at 1 (bottom-up)
        for a in range(1, amount+1):
            # Also iterate over the coins available
            for c in coins:
                ''' For each (a, c) combination check if we have a match and store the 
                min value so far (for the amount `a`) in the dp '''
                
                # If the current amount 'a' minus the current coin value is valid (i.e. not less than 0),
                # then we store the minimunm number of coins required in the dp
                if a - c >= 0:
                    # Update the value in 'dp[a]'
                    # `1` is added since we use the current coin `c` for getting the current result.
                    # So dp[a] will store the value of the min of itself and the new value 
                    # i.e. 1+dp[a-c] (using the previous value from the DP)
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    
        # Return the solution stored in dp[amount] only if it is not the default value we had saved,
        # cause if default value in dp[amount], then we could not find a solution so we return -1
        return dp[amount] if dp[amount] != amount + 1 else -1

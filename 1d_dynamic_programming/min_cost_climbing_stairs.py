'''
Question: https://leetcode.com/problems/min-cost-climbing-stairs/
'''

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """

        Approach: Use bottom-up dynamic programming

            - Define a DP array, where dp[i] represents the minimum cost to reach the i-th step
            - Iterate through the cost array, starting from the 2nd step
            - Fill the dp[i] taking the minimum of dp[i-1] + cost[i-1] and dp[i-2] + cost[i-2], 
              i.e., the cost of taking one step from the previous step (dp[i-1] + cost[i-1]) or two steps from the step before that (dp[i-2] + cost[i-2])
            - The final answer will be at dp[n], where n is the length of the cost array, since we can either take one or two steps to reach the top / end of the stairs

        Time Complexity: O(N)
        Space Complexity: O(N) - to store the dp array
        """

        
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])
        return dp[n]
    
        """
        Space Optimized Approach: Use top-down dynamic programming

            - Similar approach as above, but instead of using a DP array, we update the values of the `cost` array in place to store the minimum cost to reach each step
            - Iterate backwards, starting with len(cost) - 3 down to 0 (starting with third last element so that we can start updaing the cost array considering the last two elements)
                - At each step, update cost[i] which will be the minimum of cost[i+1] and cost[i+2]
            - Final answer will be the min of either the first or second element of the cost array (since we can start from either step 0 or step 1)
        
        Time Complexity: O(N)
        Space Complexity: O(1) - since we are modifying the input array in place
        """

        n = len(cost)

        # Iterate backwards, starting with the third last element down to the first element
        for i in range(n - 3, -1, -1):
            # At every step, we update the cost of reaching that step by taking the min of the cost between taking the next step or the step after that
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # Final result is the min of the cost between the first two steps (since we can start from either step 0 or step 1)
        return min(cost[0], cost[1])

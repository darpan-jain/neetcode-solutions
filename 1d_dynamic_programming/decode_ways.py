'''
Question: https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        '''Approach 1: Brute force - more space complexity'''
#         # Split into subproblems
#         dp = {len(s) : 1}
        
#         def dfs(i):
#             # Base case 1 - already in dp
#             if i in dp:
#                 return dp[i]
            
#             # Base case 2 - invalid string
#             if s[i] == "0":
#                 return 0
            
#             # Check for next digit only
#             res = dfs(i+1)
            
#             # We also have to check if we can take the next two digits
#             # Conditions - i+1 exists, and the two digits problem is between 10 to 26 
#             if (i+1 < len(s)) and (s[i] == "1" or 
#                 s[i] == "2" and s[i+1] in "0123456" ):
#                 # If yes, then check for the two digits problem
#                 res += dfs(i+2)
            
#             # Remember to store the result in the dp
#             dp[i] = res
#             return res
        
#         # Run the dfs starting from index 0
#         return dfs(0)

        '''Approach 2: Use Dynamic Programming'''
        # Split into subproblems, save in a DP of size = len(s), init all values to 1
        dp = {len(s) : 1}
        
        # Here we iterate in reverse (solve subproblems) and store the results in dp, building up to index 0
        for i in range(len(s)-1, -1, -1):
            
            # Base cases where the answer is "0" i.e. invalid character
            if s[i] == "0":
                dp[i] = 0
                
            # Here, check for one digit case (only one char)
            # Save the value stored dp (from a previous subproblem - memoization)
            else:                
                dp[i] = dp[i+1]
                
            # Also, check for the two digit problem
            # Conditions - i+1 should exist, and if two digits problem is between 10 to 26 (since we have only 26 alphabets)
            # so anything 27 onwards is not an alphabet (will be an invalid character/two chararcter string)
            if (i+1 < len(s)) and (s[i] == "1" or 
                s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        
        # Return the result stored in dp at index 0 (since we iterate in reverse, result will be saved in dp[0] in the end)
        return dp[0]

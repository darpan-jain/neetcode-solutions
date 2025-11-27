'''
Question: https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Approach 1: Use Bottom-up Dynamic Programming

            - Maintain a DP dictionary, where the key is the index of the string, and the value is the number of ways to decode the string starting from that index
            - Iterate through the string in reverse, and save the results of subproblems in a DP dictionary
            - For each index, check for the one digit case and the two digit case, and save the results in the DP dictionary for the current index `i`
            - Finally, return the result stored in the DP dictionary at index 0, which will give us the total number of ways to decode the entire string

        Time Complexity: O(N) - we iterate through the string once
        Space Complexity: O(N) - store the DP dictionary
        """

        # DP dictionary to store the results of subproblems, 
        # key = an index of the string and value = number of ways to decode the string starting from that index
        dp = {len(s) : 1}
        
        # Iterate in reverse (bottom-up) and update the dp[i] with the number of ways to decode the string starting from index i
        for i in range(len(s) - 1, -1, -1):
            
            # Base case: s[i] is "0", so no ways to decode the string from that index
            if s[i] == "0":
                dp[i] = 0
                
            # Update for one-digit case - here the value of dp[i] will be the same as dp[i+1], since we are referencing the value stored from the previous subproblem (i+1)
            else:
                dp[i] = dp[i+1]
                
            # Also need to check for the two-digit case (since we can take two digits together to decode a character)
            # Conditions -> i+1 should exist, 
            #               the two digits should be between 10 to 26 (since we have only 26 alphabets)
            #               (so anything 27 onwards is not an alphabet and thus will be an invalid character/two chararcter string)
            if ( i + 1 < len(s)) and \
                (s[i] == "1" or s[i] == "2" and \
                 s[i+1] in "0123456"):
                # Here, we can form a number between 10 to 26 using the character at i + 2 (two-digit case), we also add the value of dp[i + 2] to dp[i]
                dp[i] += dp[i + 2]
        
        # Finally, after reverse (bottom-up) iteration and updated to DP, the result will be stored at dp[0]
        return dp[0]
    
        """

        Approach 2: Space Optimized Bottom-up Dynamic Programming

            - Instead of using a DP dictionary, we can just use two variables to keep track of the last two results (for one-digit and two-digit cases)
            - Rest of the approach is the same
            - This way, we can achieve O(1) space complexity

        Time Complexity: O(N) - we iterate through the string once
        Space Complexity: O(1) - we only use two variables to store the results of
        """

        # Initialize two variables to store the results of the last two subproblems
        dp = dp2 = 0

        # Also init dp1, which will hold the final result
        dp1 = 1

        # Iterate in reverse (bottom-up) and update `dp` at every step
        for i in range(len(s) - 1, -1, -1):

            # Base case where current character is "0"
            if s[i] == "0":
                dp = 0
            
            # One digit case, so we update `dp` which will get the value from last subproblem `dp1`
            else:
                dp = dp1
            
            if ((i + 1 < len(s)) and \
                (s[i] == "1" or s[i] == "2") and \
                 s[i] in "0123456"):
                dp += dp2

            # Update all dp values by assigning dp1 -> dp, dp2 -> dp1. Also, `dp` is set to 0 for next iteration
            dp, dp1, dp2 = 0, dp, dp1

        # Final result is stored in `dp1` which represents the first value of the DP dictionary (the number of ways to decode the entire string) from Approach 1
        return dp1

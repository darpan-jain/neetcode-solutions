'''
Question: https://leetcode.com/problems/word-break/
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ''' Use DP i.e. bottom-up approach to solve this '''
        
        # DP stores the possibility of solution at every index in the string
        dp = [False] * (len(s) + 1)
        
        # Base case where if we reach the end of the string, then we can segment the given string 
        # (iteration starts in reverse) so after this i.e. from `len(s) - 1`
        dp[len(s)] = True
        
        # Iterate bottom-up (i.e. in reverse)
        for i in range(len(s)-1, -1, -1):

            # Iterate over every word in 'wordDict'
            for w in wordDict:
                
                # Check if `ith index + word length` is within the string bounds
                # AND if it matches the word in the dict
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # If it does, then you make the `index+word len` equal to dp[i] i.e. True
                    dp[i] = dp[i + len(w)]
                    
                # We can move to the next word in 'wordDict', if we 
                # at least one word broken for curr 'w' at index 'i'
                if dp[i]:
                    break
        
        # Check if we can word break at index 0, where the final boolean value is saved (since we iterated in reverse)
        return dp[0]

'''
Question: https://leetcode.com/problems/word-break/
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        
        Use bottom-up dynamic programming to solve 
        
        Time Complexity: O(N * M) 
            where, 
            `N` is the length of the string `s`
            `M` is the number of words in `wordDict`

        Space Complexity: O(N) for storing the DP array
        '''
        
        # DP stores the possibility of solution at every index in the string. 
        # The extra 1 is added for our base case (remember that `len` is zero-indexed in Python)
        dp = [False] * (len(s) + 1)

        '''
        Base case which assumes that if we get to the end of the string, then the string can be segmented.
        This is needed since we iterate in reverse (bottom-up DP), i.e., from `len(s)-1` to 0, 
        so we start with the base case (at len(s)) being True (Remember that `len` is zero-indexed in Python)
        '''
        dp[len(s)] = True
        
        # Iterate bottom-up (i.e. in reverse)
        for i in range(len(s)-1, -1, -1):

            # Inner loop to iterate over every word in `wordDict` for the current index `i`
            for w in wordDict:
                
                # Check if `ith index + word length` is within the string bounds
                # AND if it matches the current word from the wordDict
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:

                    # If it does, then you make the update value of `i` in the DP,
                    # which would be setting `dp[i]` to the same value as `dp[i+len(w)]` i.e., True
                    dp[i] = dp[i + len(w)]
                    
                    # If dp[i] already set True for one of the words in `wordDict`, can break and move to the next index in `s`
                    if dp[i]:
                        break
        
        # Check if we can word break at index 0, where the final boolean value is saved (since we iterated in reverse)
        return dp[0]

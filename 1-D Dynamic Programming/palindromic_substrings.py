'''
Question: http://www.lintcode.com/en/problem/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Approach 1: Count even and odd in different loops and combine the results from both
        Time Complexity: Linear O(n) (recheck but pretty sure it's correct!)
        '''
        numPalis = 0
        n = len(s)
        
        # Count odd length palidromes
        for i in range(n):
            # For odd length palindromes -> l == r == i
            numPalis += self.countPalindromes(i, i, s)
            # For even length palindromes -> l = i and  r = i+1
            numPalis += self.countPalindromes(i, i+1, s)
            
        return numPalis
    
    # Helper function to find palindromes between two pointers `l` and `r`, given a string `s`
    def countPalindromes(self, l, r, s):
        count = 0
        # Start at the same midpoint and expand outwards (in opposite directions)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count
    
        '''
        Approach 2: Count even and odd length palindromes in the same loop - Same logic, seems a little more complicated
        '''
#         N = len(s)
#         result = 0
        
#         # Iterate through all substrings of `s`
#         # Why 2N?
#         for i in range(2*N-1):
#             # Find the mid of the current substring and move in opposite directions
#             left = i // 2 # mid
#             right = left + (i % 2) # mid + 1 for even string, and mid for odd string
        
#             # Loop to find palindrome strings using `left` and `right` i.e. mid and mid-1
#             while left >= 0 and right < N and s[left] == s[right]:
#                 result += 1
#                 left -= 1
#                 right += 1
        
#         # Result is the total number of palindrome substrings
#         return result
    
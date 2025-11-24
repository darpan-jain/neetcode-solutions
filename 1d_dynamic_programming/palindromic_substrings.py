'''
Question: http://www.lintcode.com/en/problem/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Approach 1: Same approach as https://leetcode.com/problems/longest-palindromic-substring/,
        but instead of keeping track of the longest palindrome, we just count the number of palindromes we find.
        Remember that there are multiple palindromes that can be formed by expanding outwards from the same midpoint, so we need to keep track of all of them
        Eg. "aaa" -> "a", "a", "a", "aa", "aa", "aaa" -> 6 palindromic substrings
        
        Time Complexity: O(N^2) - we are iterating through all the characters in the string and for each character, we are expanding outwards to find palindromes
        Space Complexity: O(1) - we are not using any extra space, just a few variables to keep track of the count and pointers
        """
        
        # Result variable to keep track of the number of palindromic substrings
        num_palindromes = 0
        
        # Count odd length palidromes
        for i in range(len(s)):

            # For odd length palindromes -> l == r == i
            num_palindromes += self.count_palindromes_by_expansion(i, i, s)

            # For even length palindromes -> l = i and  r = i+1
            num_palindromes += self.count_palindromes_by_expansion(i, i+1, s)
            
        return num_palindromes
    
    # Helper function to find palindromes between two pointers `l` and `r`, given a string `s`
    def count_palindromes_by_expansion(self, l, r, s):
        count = 0
        
        # Start at the same midpoint and expand outwards (in opposite directions)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        # Final count contains all possible palindromes formed by expanding outwards from `l` and `r`
        return count

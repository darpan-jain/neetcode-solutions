'''
Question: https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach: 
        
            - Check for palindrome at each position in the string, starting in the middle and expanding outwards
            - Done by considering mid as the ith index in the string ('i' is each char in the string), where i is the current position in string's iteration
            - Have to Remember to check for both odd and even length palindromes, i.e. when the middle element is same and when the middle element is different (i.e. two middle elements)

        Time Complexity: O(N^2) -> We are iterating through the string and for each character we are checking for palindrome by expanding outwards
                                   In worst case, we will check for all characters in the string
        Space Complexity: O(1) -> We are using constant space to store the longest palindrome string
        """
        
        # Define the longest palindrome string variable to store the result
        longest = ""
        
        for i in range(len(s)):
            # Consider `i`th index as the middle element and check if palindrome by moving outwards
            # We consider both cases, i.e. `i` is odd and `i` is even
            
            # For odd length palindromes -> l == r == i, i.e. same middle element
            odd = self.palindrome_by_expansion(i, i, s)
            
            # For even length palindromes -> l = i and  r = i+1
            even = self.palindrome_by_expansion(i, i + 1, s)
            
            # Update the `longest` palindrome string from odd and even checks
            longest = max(longest, even, odd, key=len)            
            
        # Return the result
        return longest
    
    # Helper method to find the longest palindrome between two pointers `l` and `r` in string `s`, by expanding outwards from the middle
    def palindrome_by_expansion(self, l, r, s):

        # Iterate with two pointers outwards, until the characters don't match i.e. end of palindromic substring
        # Start in the middle and move pointers in opposite directions
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        # When the comparison stops, you return longest palidrome string using current `l` and `r` 
        # i.e. the string in between `l` and `r` pointers (which are now at the ends of the palindromic substring)
        # Excludes the last location of l and r, i.e, l+1 and r-1 
        return s[l + 1:r]

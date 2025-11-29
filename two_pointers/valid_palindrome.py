'''
Question: https://leetcode.com/problems/valid-palindrome/
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Approach: Two Pointers
            - Use two pointers at the start and end of the string. 
            - Keep comparing until the letters are alphanumeric (use ASCII values) and equal.
            - If they are not, return false!
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        # Left pointer is at the start and right pointer is at the end of the string
        l, r = 0, len(s) - 1

        # Keep checking until the two pointers don't cross each other
        while l < r:

            # Keep moving left pointer under the left char is alphanumeric (l += 1)
            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            # Keep moving right pointer under the right char is alphanumeric (r -= 1)
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1

            # If the characters on two pointers are not equal, not a Palindrome string.
            # Remember to convert both chars to lower, since the string is case insensitive
            if s[l].lower() != s[r].lower():
                return False

            # If all above conditions satisfied, we update 
            # both the pointers for next iteration
            l, r = l + 1, r - 1

        # If all goes well, it is a Palindrome string
        return True

    def isAlphaNum(self, c: chr) -> bool:
        """
        Method to check if a given character is alphanumeric 
        by checking ASCII values.
        
        'ord' gives the ASCII value of a character. 
        Check if the current character 'c' lies between 
        A-Z, a-z, 0-9 i.e. alphanumeric
        """

        return (ord('A') <= ord(c) <= ord('Z') or \
                ord('a') <= ord(c) <= ord('z') or \
                ord('0') <= ord(c) <= ord('9'))

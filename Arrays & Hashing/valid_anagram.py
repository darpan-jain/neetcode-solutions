'''
Question: https://leetcode.com/problems/valid-anagram/
'''

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''Approach 1: Compare the count of the characters in each string'''

        # If lengths don't match, then not anagrams
        if len(s) != len(t):
            return False
            
        # Define defaultdict to store count of each letter
        count = defaultdict(int)
        
        # Iterate through first string `s` and add count each letter's occurence
        for i in s:
            count[i] += 1
            
        # Iterate through second string `t` and decrement for each count of the letter
        for j in t:
            count[j] -= 1
            
            # If any count < 0, that means that it didn't occur in 1st string
            # This would be a dealbreaker i.e. the string are not anagrams
            if count[j] < 0:
                return False
        
        # If all goes well, then they are anagrams!
        return True
        
        '''Approach 2: Same as 1, but use collections.Counter'''
        # return collections.Counter(s) == collections.Counter(t)
        
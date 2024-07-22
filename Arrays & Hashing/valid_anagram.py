"""
Question: https://leetcode.com/problems/valid-anagram/
"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ Approach 1: Compare the count of the characters in each string """

        # If lengths don't match, then `s` and `t` definitely won't be anagrams
        if len(s) != len(t):
            return False

        # Define `defaultdict` to store count of each letter
        # Note: using `defaultdict(int)` will have a default value of integer zero if a key does not exist.
        count = defaultdict(int)

        # Iterate through first string `s` and add count each letter's occurrence
        for i in s:
            count[i] += 1

        # Iterate through second string `t` and decrement for each count of the letter
        for j in t:
            count[j] -= 1

            # If any character's count < 0, that means that it didn't occur in 1st string (`s`)
            # This would be a deal-breaker i.e. the strings are not anagrams!
            if count[j] < 0:
                return False

        # If all goes well (the for loop through `t` completes), then they are anagrams!
        return True

        """ 
        Approach 2: Same as 1, but using `collections.Counter`
        `collections.Counter` returns a dictionary with elements as keys and their counts as values.
        If `s` and `t` are anagrams, then the count of each character in both strings will be the same, and hence the equality will be True! 
        """
        # return collections.Counter(s) == collections.Counter(t)

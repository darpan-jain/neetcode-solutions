'''
Question: https://leetcode.com/problems/group-anagrams/
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        Group strings which have the same letter counts. Similar approach to 'Valid Anagrams' problem.
        Time complexity -> O (m * n) 
        where, m = number of strings
               n = average length of a string
        '''
        
        # Dict to map character counts to list of Anagrams
        # Why defaultdict? If key doesn't exist, it creates one. The default value for 'res' is a 'list'
        result = defaultdict(list)

        for s in strs:
            # List for char count for each of the 26 letters
            count = [0] * 26

            # Populate character frequency for current string
            for c in s:
                # Increment counter for current character using (ASCII of current letter) - (ASCII of 'a')
                char_idx = ord(c) - ord("a")
                count[char_idx] += 1

            # Add strings with similar counts to the result dict
            # Why 'tuple(count)'? Since Python doesn't allow lists as keys
            result[tuple(count)].append(s)

        # Return only the values of the result dict i.e. the groups of anagrams
        return result.values()
    
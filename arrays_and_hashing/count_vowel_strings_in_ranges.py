'''
Question: https://leetcode.com/problems/count-vowel-strings-in-ranges
'''

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        Approach: Use Prefix Sum to maintain the cumulative count of vowel strings at each index in the `words` list

        Time Complexity : O(N + Q), where N is the number of words and Q is the number of queries
        Space Complexity: O(N) for the prefix sum array
        """

        n = len(words)
        # Build prefix sum array where prefix[i] represents the count of vowel strings from words[0] to words[i-1]
        prefix = [0] * (n + 1)
        # Define vowels for easy checking
        vowels = ['a', 'e', 'i', 'o', 'u']

        # Build the prefix sum array
        for i in range(n):
            # Carry forward the previous count (since the prefix sum is cummulative)
            prefix[i + 1] = prefix[i]
            # Check if the current word starts and ends with a vowel
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1 # Increment the count for vowel strings
        
        # Now, process result for each query by a simple lookup in the prefix sum array
        result = []
        for query in queries:
            # The total count in the query range is the difference between the prefix sums at the end and start indices
            # Note: prefix is 1-indexed, so we access prefix[query[1] + 1]
            matching_count = prefix[query[1] + 1] - prefix[query[0]]
            result.append(matching_count)

        # Return the final result list containing vowel string counts for each query range
        return result

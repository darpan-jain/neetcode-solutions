"""
Question: https://leetcode.com/problems/top-k-frequent-elements/
"""

import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Use Bucket Sort - create `dict` with key as the frequency and the values as the elements that
        occurred index number of times.

        Time complexity : O(N)
        Space complexity: O(N)
        """
        
        # Create a `defaultdict` with default value as a `list`.
        # In this, we store the element count as `key and the values as list of all elements with that
        # count or frequency of occurrence.
        freq = collections.defaultdict(list)
        
        # Count the frequency of elements in `nums` and store in the dict (as defined above)
        # If the interviewer permits, you can also use `collections.Counter` to get the same result.
        for key, count in collections.Counter(nums).items():
            freq[count].append(key)
        
        # Now we go through the frequency list and iterate until we have the top K frequent elements
        result = []
        
        # We iterate in reverse since we need the top most occurring element first
        # Why iterate over `len(nums)`? Since the max freq of an element can't be 
        # more than the length of the list
        for num_occurrence in reversed(range(len(nums)+1)):
            # Extend adds the element at index 0 instead of the end of the list
            # The element being added is the element that occurs `num_occurrence` times
            result.extend(freq[num_occurrence])
            # print(f"{num_occurrence}: {res}")
    
            # We stop once we have the top-K elements
            if len(result) >= k:
                return result[:k]
            
        return result[:k]
    
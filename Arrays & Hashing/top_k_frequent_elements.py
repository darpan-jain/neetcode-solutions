'''
Question: https://leetcode.com/problems/top-k-frequent-elements/
'''

from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Use Bucket Sort - create dict with key as the frequency and the values as the elements that 
        occurred index number of times.
        Time & Space complexity -> O(n) i.e. linear time 
        '''
        
        # Create a defaultdict with default value as a `list`
        # In this, we store the element count as `key and the values as list of all elements with that
        # count or frequency of occurence.
        frq = defaultdict(list)
        
        # Count the frequency of elements in `nums` and store in the dict (as defined above)
        for key, count in Counter(nums).items():
            frq[count].append(key)
        
        # Now we go through the frequency list and iterate until we have the top K frequent elements
        result = []
        
        # We iterate in reverse since we need the top most occurring element first
        # Why iterate over `len(nums)`? Since the max freq of an element can't be 
        # more than the length of the list
        for num_occurence in reversed(range(len(nums)+1)):
            # Extend adds the element at index 0 instead of the end of the list
            # The element being added is the element that occurs `num_occurence` times
            result.extend(frq[num_occurence])
            # print(f"{num_occurence}: {res}")
    
            # We stop once we have the top-K elements
            if len(result) >= k:
                return result[:k]
            
        return result[:k]
    
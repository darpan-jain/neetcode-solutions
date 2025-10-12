"""
Question: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Approach: 
            Use Sliding window approach with two pointers. 
            
            Both pointers start from element 0 and the right pointer is moved further right,
            untilwe meet the condition where -> number of replacements required in current window <= `k`
        
            Here, the number of replacements required should be less than the max allowed replacements (i.e. `k`),
            which is calculated using "current window size - count of most occuring character in the window"
                -> `(r - l + 1) - max(count.values())`

            # Why is `max(count.values())` used?
                -> Since we can replace any ONE character `k` times, so we consider the 
                   most occuring character in the window for the replacements
        
        Time complexity: O(N)
        Space complexity: O(1) - since the count dict will have at most 26 characters
        """
        
        # Dict `count` to store the frequency of the characters in the current window
        count = {}
        
        # Result variable to store the max length of valid window found
        max_len = 0
        
        # Left pointer starting at index 0
        l = 0

        # Right pointer, also starting at zero but moves to the right, expanding the sliding window
        for r, curr_char in enumerate(s):
            
            # Increment the frequency of the current character by 1 in the `count` dict
            count[curr_char] = 1 + count.get(curr_char, 0)
            
            # Make the window valid if it's not, by moving the left pointer (after considering the possible replacements)
            # `k` possible replacements are also considered using `(windowLen - max occuring char in the window)` is <= k
            while (r - l + 1) - max(count.values()) > k:

                # If not valid window, we remove the character at the left pointer,
                # remove it from the `count` dict and increment the left pointer position
                count[s[l]] -= 1
                l += 1

            # Update the max_len by comparing with current window size
            max_len = max(max_len, r-l+1)
                   
        return max_len

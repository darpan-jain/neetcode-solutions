'''
Question: https://leetcode.com/problems/longest-repeating-character-replacement/
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window approach with two pointers. 
        The pointers start from element 0 and right pointer is moved right everytime until
        we meet the condition -> number of replacements required in current window <= k
        
        Here, the number of required to replace should be less than the max allowed replacements (i.e. k)
        calculated using -> (window_size - count of most occuring character in the window)
        
        Time complexity: O(n)
        '''
        
        # Dict 'count' to store the frequency of the characters in the current window
        count = {}
        
        max_len = 0
        
        # Left pointer that stays
        l = 0

        # Right pointer moves to the right, expanding the sliding window
        for r, curr_char in enumerate(s):
            
            # Increment the frequency of the current character by 1
            count[curr_char] = 1 + count.get(curr_char, 0)
            
            # Check if the `(windowLen - max occuring char in the window)` is <= k
            # i.e. check if this is a valid window maximizing the sequence length
            # Using this we check if the required replacements are
            # less than the allowed 'k' replacements
            while (r - l + 1) - max(count.values()) > k:

                # If not, then move the left pointer to the right (and decrement the
                # count of the char that was taken out of the window by moving 
                # the left pointer) and make the window valid again
                count[s[l]] -= 1
                l += 1

            # Update the max_len by comparing with current window size
            max_len = max( max_len, r-l+1 )
                   
        return max_len

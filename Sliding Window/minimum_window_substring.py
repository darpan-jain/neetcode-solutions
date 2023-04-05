'''
Question: https://leetcode.com/problems/minimum-window-substring/
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Sliding window with two pointers - 
        
        1. Count the frequency of characters in `t`
        2. Maintain two counters - `have` & `need`
        3. Sliding window over the main string `s` and keep moving right pointer `r`
            3.1. For each char in `s`, check if belongs to `t`. If it does, increment `have` counter
            3.2  Also check if the `have` what we `need` i.e. if have == need
            3.3 If they do, update result by taking a `min`.
            3.4 Start popping characters from the left to make the window smaller and keep checking if `have == need`
        4. Repeat until you go over all the characters in `s`

        So, we move `right` pointer in `have != need` (the for loop at line 43) and `left` pointer if `have == need` (line 56)
        
        Time complexity: O(n)
        '''
        
        # Edge case
        if not t: 
            return ""
        
        countT, window = {}, {}
        
        ## 1. Populate the frequency count for string `t` - the substring we need to find the window for
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        ## 2. 'have' is the current window, and 'need' is for the string `t`
        have, need = 0, len(countT)
        left = 0
        
        # Indices are set to -1 and result length set to infinity
        res, resLen = [-1, -1], float('inf')
        
        ## 3. Iterate over the main string `s`
        # Left pointer stays while right pointer moves - expanding the sliding window
        for right, c in enumerate(s):

            # Increment frequency of `c` in the 'window' dict
            window[c] = 1 + window.get(c, 0)
            
            ## 3.1 If the current char `c` is the char we need (i.e. a part of string `t` i.e. `countT`)
            # and the count of the char is equal in the current window and `countT`
            # then `have` counter is incremented by 1
            if c in countT and window[c] == countT[c]:
                have += 1
                
            ## 3.2 check if `have` what we `need` i.e. if `have == need`
            # So update result and move the left pointer!
            while have == need:
                if (right - left + 1) < resLen:
                    ## 3.3 Update only if current window smaller than current `resLen`
                    res = [left, right]
                    resLen = (right - left + 1)
                
                ## 3.4 Now pop characters from the left (to check other windows) and find the smallest window.
                # Before incrementing left pointer (moving to the right), update count values 
                # and check if `have` counter needs to be updated
            
                # Decrement the count of the char being removed from the window
                left_char = s[left]
                window[left_char] -= 1
                
                # Also, decrement `have` by removing the character that we took out of the sliding window (by moving right)
                if s[left] in countT and window[left_char] < countT[left_char]:
                    have -= 1
                
                # Finally, increment the left pointer
                left += 1
        
        ## Finally, at the end of the for loop, extract the left and right indices for the minimum window (stored in `res`)
        l, r = res
        
        # Check if `resLen` actually exists or else return empty string
        return s[l:r+1] if resLen != float('inf') else ""

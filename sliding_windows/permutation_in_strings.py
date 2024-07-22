'''
Question: https://leetcode.com/problems/permutation-in-string/
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Use a sliding window to compare the count of the characters in each string.
        Time Complexity = O(26) + O(n) = O(n)
        '''
        
        # Length of `s1` needs to be less than length of `s2`
        if len(s1) > len(s2):
            return False

        # Counters for the characters in each string
        s1Count, s2Count = [0]*26, [0]*26

        # Populate the character count arrays - only need to do it for the length of `s1`
        for i in range(len(s1)):
            # Get the index of the character in the `count` array
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Now check the number of matches of characters in `s1Count` and `s2Count`
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Now, sliding window over the remaining characters of `s2` to find the permutation string
        # Sliding window implemented using two pointers (left at 0 and right moves from 0 to end)
        # Note: window start at len(s1), since we already checked the characters 
        # from 0 to len(s1) - 1 in the previous (initial) window
        l = 0
        for r in range(len(s1), len(s2)):
            
            # Return if the current window is a perfect match between `s1` and permutation in `s2`
            if matches == 26:
                return True

            ## Add the right character (at index `r`) into the window and update the `matches` counter
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # If adding the character makes the count in both counters equal, increment `matches`
            if s1Count[index] == s2Count[index]:
                matches += 1
            # But if adding the character makes the count in s1Count one less than s2Count, 
            # then we created a mismatch, so decrement `matches`
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            ## Same operation for left character, but here we are removing a character (since the sliding window moves to the right)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Same condition check as done for left character
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Here, if removing the left character, made the s1Count of the index one less than s2Count
            # we created a mismatch, so we decrement `matches`
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Remember to update the left pointer!
            l += 1
        
        # Finally, check if the matches are 26, then permutation exists, else doesn't!
        return True if matches == 26 else False

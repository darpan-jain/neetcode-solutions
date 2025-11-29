'''
Question: https://leetcode.com/problems/permutation-in-string/
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Overall Approach: 
            Use a sliding window to compare the count of the characters in each string.
            This is similar to Finding Anagrams in a string, but order doesn't matter here since we are looking for permutations.
        
        Brute Force:
            Create the character count of `s1` and then for each substring of length `len(s1)` in `s2`,
            create the character count and compare with `s1`'s character count.

        Time Complexity: O(26 * N) = O(N)
        Space Complexity: O(N)
        
        Optimized (implemented below):
            Maintain a variable `matches` that keeps track of how many characters have the same count in both `s1` and `s2`
            Then use a sliding window of size `len(s1)` to traverse through `s2` and update the character count and `matches` variable accordingly.
            If at any point `matches` becomes 26, then we have found a permutation of `s1` in `s2`
            
        Time Complexity: O(26) + O(N) = O(N) - which is better than brute force approach
        Space Complexity: O(1) - since we are using fixed size arrays of size
        """
        
        # Edge case where `s1` is longer than `s2`, so No permutations of `s1` can exist in `s2`
        if len(s1) > len(s2):
            return False

        # Arrays to keep count of characters in `s1` and current window in `s2`
        s1Count, s2Count = [0] * 26, [0] * 26

        # Populate the character count for `s1` and the only first window in `s21 of size `len(s1)`
        for i in range(len(s1)):
            # Increment the count of the character at index `i` in both strings
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # For the first window in `s2`, count how many characters have the same count in both `s1` and `s2`
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Now, we run a sliding window with two pointers (l and r) over the remaining characters of `s2`
        # Remember that the first window in `s2` is already considered above and the `matches` are calculated
        l = 0

        # Right pointer starts at len(s1) to len(s2) 
        # (the for loop for the first window stopped at `len(s1)` but did not include it)
        for r in range(len(s1), len(s2)):
            
            # First check if all characterss from the last window matched, if yes, return True
            if matches == 26:
                return True

            # If not, we slide the window to the right by one position
            # So we need to add the character at index `r` and remove the character at index `l`
            # And Update the counts and `matches` accordingly

            ''' Add the right character and update `matches` '''
            # 1. Find the index of the character to be added
            index = ord(s2[r]) - ord('a')

            # 2. Increment the count of the character in `s2Count`
            s2Count[index] += 1

            # 3. Update `matches`

            # 3,1 If after adding the right character, the count in both `s1Count` and `s2Count` are same,
            if s1Count[index] == s2Count[index]:
                matches += 1
            
            # 3.2 But if before adding the character, the count was same (i.e. now after adding it, they are not same),
            # then we created a mismatch, so decrement `matches`
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            ''' Remove the left character and update `matches` '''
            # 1. Find the index of the left character to be removed
            index = ord(s2[l]) - ord('a')

            # 2. Decrement the count of the character in `s2Count`
            s2Count[index] -= 1

            # 3. Update `matches`
            # 3.1 If after removing the left character, the count in both `s1Count` and `s2Count` are same,
            if s1Count[index] == s2Count[index]:
                matches += 1

            # 3.2 But if before removing the character, the count was same (i.e. now after removing it, they are not same),
            # we created a mismatch, so we decrement `matches`
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Finally, remember to update the left pointer as well (right is updated by the for loop)
            l += 1
        
        # At the end of the for loop, we finally check if all characters are matched in `s1count` and `s2count`
        # (i.e. if matches == 26)
        return True if matches == 26 else False

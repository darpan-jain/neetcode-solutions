"""
Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """ 
        Approach 1: Sliding window with two pointers. Maintain a character set representing all the
        characters inside the window. If character repeats in a window, move the left pointer until
        the window is valid again i.e., no repeating characters in the window.
        """
        
        # Charset to maintain the non-repeating sequence in the sliding window
        charSet = set()
        
        # Left pointer that does not move until we encounter a duplicate character
        l = 0
        
        max_len = 0
        
        # Move the right pointer while the left stays constant for the sliding window
        for r in range(len(s)):
            
            # If we encounter a duplicate character, increment the left pointer
            # `while` loop, since we keep shrinking the window until it becomes valid again
            # (i.e., no duplicate characters in the window)
            while s[r] in charSet:
                # Remove the char at left pointer and increment the left pointer by 1
                charSet.remove(s[l])
                l += 1
                # We move the left pointer until we reach a non-duplicate character 
                # i.e. until the window is valid again
                
            # If not duplicate, then add `s[r]` to the `charSet`
            charSet.add(s[r])
            
            # Update the max length of the subseq so far
            curr_len = r-l+1
            max_len = max(max_len, curr_len)
                
        return max_len
        
        
        """ Approach 2: Also sliding window approach: O(n) time complexity """
        
#         # Init two pointers - 'start' stays constant (represents start of the current substring), 
#         # and 'j' moves to the right checking to compare the characters and trying to
#         # build the longest substring
#         start = 0
#         # Dict that stores the last seen index of the characters in the string
#         chars = {}
#         # Stores the max length of the non-repeating substring
#         max_len = 0
        
#         # 'j' moves from start to end of the string
#         for j, c in enumerate(s):
#             # Checks if the current char has been repeated or not
#             if c in chars:
#                 '''
#                 If repeated, move 'start' to the right.
#                 Why do 'max'? Because 'start' should always move to the right and doing
#                 a 'max' ensures that (since it'll always pick the bigger value i.e. to the right)
#                 '''
#                 start = max ( start, chars[c] + 1 )
            
#             # If curr character is not repeated, then calculate the new 'max_len'
#             max_len = max( max_len, j - start + 1 )
#             # and also add the curr character to the used 'chars' dict with 
#             # the index of latest occurrence
#             chars[c] = j
            
#         return max_len        
        
        
        """ Approach 3: Same approach 2, more concise implementation """
        
#         # Dict to store the index of each character while iterating the input string
#         chars = {}
#         # 'start' is the start index of the current longest substring (slow pointer), 
#         # 'maxLen' is well self-explanatory
#         start = max_len = 0
        
#         for j, c in enumerate(s):
#             if c in chars and start <= chars[c]:
#                 # Here instead of using 'max' to update start when we see a repeated character,
#                 # we use the conditon 'start <= chars[c]' to ensure that start moves to the right only!
#                 start = chars[c] + 1
#             else:
#                 # If not repeated char, check if curr substring length greater than max_len and update
#                 max_len = max(max_len, j-start+1)
            
#             # In either case, update the index of the occurence of the current character
#             chars[c] = j

#         return max_len

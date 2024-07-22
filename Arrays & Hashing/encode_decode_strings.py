'''
Question: https://leetcode.com/problems/encode-and-decode-strings/ (Leetcode Premium) 
                                OR 
          https://www.lintcode.com/problem/659/ (Free by Lintcode)
'''

class Solution:

    def encode(self, input_str: str):
        """
        Encode the individual strings as a single string by adding an integer and delimiter to the start of each string.

        The integer indicates number of characters in the current string, 
        and the delimiter ('#') will separate the integer and the actual string.
        
        Eg. ["lint","code","love","you"] will become "4#lint4#code4#love3#you" as the encoded string.
        """

        encoded_str = ""

        for s in input_str:
            encoded_str += str(len(s)) + '#' + s

        return encoded_str

    def decode(self, encoded_str: str):
        """
        We decode the encoded string as described in the `encode` method.
        """

        decoded_str = []
        # We use pointer `i` to keep track of where we are in the encoded str
        i = 0

        # Keep iterating until you go through the entire encoded string
        while i < len(encoded_str):
            # Introduce another pointer to find the delimiter we encoded
            j = i
            
            while encoded_str[j] != '#':
                # We keep incrementing `j` until we find the delimiter
                j += 1
            
            # Here, we have encountered a delimiter. So we start decoding...

            # Get the length of the current string
            length = int(encoded_str[i:j])
            # Splice the encoded string and append the extracted string to `decoded_strs`
            decoded_str.append(encoded_str[j+1: j+1+length])
            
            # Once you have the string extracted, update `i` to resume from the next string
            i = j+1+length

        return decoded_str
            
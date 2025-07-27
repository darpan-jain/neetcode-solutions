'''
Question: https://leetcode.com/problems/reverse-bits/
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Approach: Use logical AND operator 

        Use a mask to extract the bits from the input number `n` and then shift them to the correct position in the `result` 

        Time Complexity: O(1) -> iterating over 32 bits
        Space Complexity: O(1) -> no extra space to store the result
        """

        result = 0

        # Iterate over the 32 bit input `n`
        for i in range(32):

            # Extract the bit value from `ith` index by doing a logical AND operation
            # >> left shifts the bits by `i` positions
            bit = (n >> i) & 1

            # Store the extracted bit value in the `ith` position in the result
            # This is done using right shift and then performing a logical OR
            # `(31 - i)` ensures that the bit is saved in the `ith` position of the result
            result = result | (bit << (31 - i))

        return result

'''
Question: https://leetcode.com/problems/reverse-bits/
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        # Iterate over the 32 bit input `n`
        for i in range(32):

            # Extract the bit value from `ith` index by doing a Logical AND operation
            # >> left shifts the bits by i locations
            bit = (n >> i) & 1

            # Store the extracted bit value in the `ith` position in the result
            # This is done using right shift and then performing a Logical OR
            # `(31 - i)` ensures that the bit is saved in the `ith` position of the result
            result = result | (bit << (31 - i))

        return result

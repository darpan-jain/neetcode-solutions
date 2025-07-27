'''
Question: https://leetcode.com/problems/sum-of-two-integers/
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Approach 1: Use bitwise operations to calculate the sum of two integers in binary form

        Time Complexity: O(1) -> iterating over 32 bits
        Space Complexity: O(1) -> no extra space to store the result
        """

        carry = 0
        result = 0

        # Initialize mask to 0xFFFFFFFF which is 32 1s in binary
        mask = 0xFFFFFFFF

        # Iterate over 32 bits
        for i in range(32):

            # For each bit, extract the bit value from `ith` index by doing a logical AND operation
            # >> left shifts the bits by `i` positions, `& 1` extracts the bit value at `ith` index
            # `a_bit` and `b_bit` are the bits at `ith` index of `a` and `b` respectively
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            # Calculate the current bit value by XORing the bits of `a` and `b` and the carry
            cur_bit = a_bit ^ b_bit ^ carry

            # Calculate the carry by adding the bits of `a` and `b` and the carry
            # If the sum is greater than or equal to 2, then the carry is 1, otherwise it is 0
            # Why 2 instead of 9? Since we are using binary, 2 is the max sum of two bits
            carry = (a_bit + b_bit + carry) >= 2

            # If the current bit is 1, then set the `ith` index of `result` to 1 using bitwise OR operation and left shift by `i` positions
            if cur_bit:
                result |= (1 << i)
            
        # If the result is greater than 0x7FFFFFFF, then it is a negative number
        # So we need to flip the bits and add 1 to get the actual value
        if result > 0x7FFFFFFF:
            result = ~(result ^ mask)

        # Finally, return the result
        return result

        """
        Approach 2: Similar to 1 but without using the `result` variable and more compact

        Time Complexity: O(1) -> iterating over 32 bits
        Space Complexity: O(1) -> no extra space to store the result
        """

        # Initialize mask to 0xFFFFFFFF which is 32 1s in binary
        mask = 0xFFFFFFFF

        # Initialize max_int to 0x7FFFFFFF which is 31 1s in binary
        max_int = 0x7FFFFFFF

        # Iterate until `b` is 0 (i.e., until there is no carry)
        while b != 0:

            # Calculate the carry by doing a bitwise AND operation between `a` and `b` and then left shift by 1 position    
            carry = (a & b) << 1

            # Calculate the sum by doing a bitwise XOR operation between `a` and `b` and then applying the mask
            a = (a ^ b) & mask

            # Calculate the carry by doing a bitwise AND operation between `carry` and the mask
            b = carry & mask
        
        # If the result is greater than 0x7FFFFFFF, then it is a negative number
        # So we need to flip the bits and add 1 to get the actual value (i.e., 2's complement)
        # which is done using XOR on `a` and `mask` and `~` to flip the bits
        return a if a <= max_int else ~(a ^ mask)

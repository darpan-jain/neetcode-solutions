'''
Question: https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Approach 1: Use mod 2 ( % 2) to get the value of the last bit
        Shift the values by 1 bit on the right (n >> 1) after each iteration to get the next bit
        """

        count = 0
        
        # While `n` does not become 0
        while n:
            # Perform mod 2 operation and add the value (either 1 or 0) to the count
            count += n % 2

            # Shift the values by 1 bit on the right
            # Can also be done  -> n = n / 2 (but bit shifting is more efficient)
            n = n >> 1
        
        return count
        
        """
        Approach 2: Use bitwise AND(&) operator
        
        AND operator = 1 if both bits are 1, else 0
        
        Eg. 
            n = 1000 (binary)
            n - 1 = 0111 (binary)
            n & (n - 1) = 0000 (binary)

        n & (n - 1) will be 0000, which is just remove the last significant 1
        
        Consider n and n-1 -> compared with n,n-1 has one bit-place difference 
        which makes a 1 in n becoming 0 in n-1

        And with counting recursively, we get all 1s canceled (while incrementing count), and then return count
        """
        
        count = 0

        # While `n` does not become 0
        while n:
            # Perform bitwise AND operation and remove the last significant 1
            n &= n-1

            # Increment the count by 1
            count += 1

        return count
    
        """
        Approach 3: Use inbuilt `bin()` function to convert the number to binary and count the number of 1s
        """

        return bin(n).count("1")

'''
Question: https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        ''' Approach 1: Use mod 2 ( % 2) to get the value of the last bit '''
        count = 0
        
        # While `n` does not become 0
        while n:
            # Do a `mod 2` operation and add the value (either 1 or 0) to the count
            count += n % 2
            # Shift the values by 1 bit on the right
            n = n >> 1
            # Can also do `n = n / 2` (but bit shifting is more efficient)
        
        # Finally return the result
        return count
        
        '''
        Approach 2: & bit operator is: 1 if both bits are 1, else 0
        
        Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. 
        n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
        
        Consider n and n-1 -> compared with n,n-1 has one bit-place difference 
        which makes a 1 in n becoming 0 in n-1.

        And with counting recursively, we get all 1s canceled 
        (while incrementing count), and then return count.
        '''
        
        # count = 0
        # while n:
        #     n &= n-1
        #     count += 1
        # return count

'''
Question: https://leetcode.com/problems/powx-n/
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Approach: Divide and conquer by Binary Exponentiation (using Recursion)
        Instead of calculating all the powers of the `x`, split in half and multiply with itself.

        Have to handle cases where exponent is even or odd. Eg. 
        2 ^ 4 = (2 ^ 2) * (2 ^ 2)
        2 ^ 5 = 2 * (2 ^ 2) * (2 ^ 2) [Note the extra multiply by 2 needed]

        Time Complexity: O(log n)
        Space Complexity: O(log n) for the recursion stack
        """

        def helper(x, n):

            if x == 0: 
                return 0
            if n == 0: 
                return 1

            # Recursive call with exponent being divided by 2
            res = helper(x * x, n // 2)
            # Add an extra `x` if exponent is odd, else return `res` directly
            return x * res if n % 2 else res

        # Only send absolute (+) values of exponent `n`
        res = helper(x, abs(n))
        
        # Handle negative exponent values in final return
        # Negative exponent means the (x^n) term goes in the denominator
        return res if n >= 0 else 1 / res

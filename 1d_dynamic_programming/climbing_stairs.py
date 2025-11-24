'''
Question: https//leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach: Use bottom-up dynamic programming, i.e., solve subproblems until you reach the end
        
        This is basicially a Fibonacci series (1, 1, 2, 3, 5, 8, 13, ...), the number of ways to climb `n` stairs is the sum of the ways to climb `n-1` and `n-2` stairs.
        Create the series for `n` iterations and then the result is in the first variable. 

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        
        # Start with both values as 1
        a, b = 1, 1
        
        for _ in range(n):
            # Assign new 'a' to last value  i.e. 'b' and 
            # now 'b' to 'a+b' (to create fibonacci series)
            a, b = b, a+b
        
        # The number of distinct ways to climb the stairs is stored in 'a'
        # How? 
        return a
    
        """ 
        Another way to write the same code
        """
#         one, two = 1, 1
    
#         for i in range(n - 1):
#         # Doesn't matter how you swap, as long as it is consistent
#             one, two = one + two, one 
        
#         return one
        
            
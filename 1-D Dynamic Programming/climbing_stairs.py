'''
Question: https//leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        ''' Solve using DP Bottom up approach. i.e. solve subproblems until you reach the end.
        This is basicially a Fibonacci series. Create it for n iterations and then the result is in the first variable. 
        '''
        
        # Start with both values as 1.
        a, b = 1, 1
        
        for _ in range(n):
            # Assign new 'a' to last value  i.e. 'b' and 
            # now 'b' to 'a+b' (to create fibonacci series)
            a, b = b, a+b
        
        # The number of distinct ways to climb the stairs is stored in 'a'
        # How? 
        return a
    
        ''' Another way to write the same code '''
#         one, two = 1, 1
    
#         for i in range(n - 1):
#         # Doesn't matter how you swap, as long as it is consistent
#             one, two = one + two, one 
        
#         return one
        
            
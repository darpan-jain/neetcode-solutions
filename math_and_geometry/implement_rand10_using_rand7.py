'''
Question: https://leetcode.com/problems/implement-rand10-using-rand7/
'''

import math

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self) -> int:
        """
        Approach: Rejection Sampling
            - Within a while loop, we will keep generating random numbers until we get a valid number in the desired range
                - Use the rand7() function to generate a uniform distribution over a larger range (1 to 49)
                    How? By treating two calls to rand7() as a two-dimensional grid
                        - First call gives the row (1 to 7)
                        - Second call gives the column (1 to 7)
                        - This results in 7 * 7 = 49 possible outcomes

                - If the generated number is <= 40, we can map it to 1 to 10 and return the result
        
        Note: This can be generalized to implement any function randN() using an existing randM() function, where N > M
        """

        while True:
            ''' Generate a number in the range 1 to 49 '''
            # Use two independent rand7() calls to form a 7x7 grid of outcomes (49 equally likely possibilities)
            # Treat the first call as the "row" (0-based by subtracting 1) and the second as the "column"
            # Map (row, column) to a single number in [1, 49]:
            #   row in [0..6] -> contributes multiples of 7: 0, 7, 14, ..., 42
            #   column in [1..7] -> adds 1..7 within each block
            num = (rand7() - 1) * 7 + rand7()  # Uniform over 1..49

            # Check if the number is within the acceptable range of <= 40
            if num <= 40:
                # Map the number to 1 to 10 and return
                return (num - 1) % 10 + 1
            
            # If num is greater than 40, we reject and try again


    def randN(self, N: int, M: int = 7) -> int:
        """
        Generalized Approach: Rejection Sampling to implement randN() using a function randM()
            - Determine the smallest k such that M^k >= N
            - Generate a number in the range 1 to M^k using k calls to randM()
            - If the generated number is <= floor(M^k / N) * N, map it to 1 to N and return
            - Otherwise, reject and repeat
        
        For the current case, let's assume M = 7  # Since we have rand7()
        """

        k = math.ceil(math.log(N) / math.log(M))  # Smallest k such that M^k >= N
        max_range = M ** k
        acceptable_range = (max_range // N) * N  # Largest multiple of N less than or equal to M^k

        while True:
            # Generate a number in the range 1 to M^k
            num = 0
            for i in range(k):
                num = num * M + (rand7() - 1)  # Build the number in base M

            num += 1  # Convert to 1-based index

            # Check if the number is within the acceptable range
            if num <= acceptable_range:
                return (num - 1) % N + 1  # Map to 1 to N
            # Otherwise, reject and try again
            
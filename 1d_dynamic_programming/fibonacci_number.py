'''
Question: https://leetcode.com/problems/fibonacci-number/
'''

from typing import List


class Solution:

    def fib(self, n: int) -> List:
        """
        Approach 1: Using bottom-up dynamic programming with space optimization
            - Done using two variables to store only the last two Fibonacci numbers and no recursion
            - Also applied for https//leetcode.com/problems/climbing-stairs/

        Time Complexity: O(N),
        Space Complexity: O(1), we only use two variables instead of a list to store the entire Fibonacci sequence
        """

        # Base case
        if n == 0: 
            return 0
        
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1

        # Iterate from 2 to n and update the last two Fibonacci numbers
        for _ in range(2, n+1):
            # Swap the last two terms to update the Fibonacci sequence (a -> b, b -> a + b)
            a, b = b, a + b
        
        # The final result is stored in b (the Nth number in the Fibonacci sequence)
        return b

        """
        Approach 2: Using bottom-up dynamic programming with memoization

        Time Complexity: O(N), we save time by computing each fibonacci number only once (as compared to the repeated calculations in Approach 1)
        Space Complexity: O(N), for the recursion stack and the memoization list
        """

        # Initialize a list to store the Fibonacci sequence
        fiq_seq = [0, 1]

        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Check if the Fibonacci number for n-1 is already computed
        if n-1 not in fiq_seq:
            # If not computed, recursively compute it and store it in the list
            fiq_seq[n - 1] = self.fib(n - 1)

        # Same for n - 2 position
        if n-2 not in fiq_seq: 
            fiq_seq[n - 2] = self.fib(n - 2)
        
        # Return the sum of the two preceding Fibonacci numbers (the Nth number in the Fibonacci sequence)
        return fiq_seq[n - 1] + fiq_seq[n - 2]


        """
        Approach 3: Naively using Recursion 

        Time Complexity : O(2^N), since each call generates two more calls
        Space Complexity: O(N), for the recursion stack
        """

        # Base cases
        if n < 0:
            print("N should be a non-negative integer (>= 0)")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Recursive call to get the Nth number in the Fibonacci sequence
        else:
            return self.fib(n - 1) + self.fib(n - 2)

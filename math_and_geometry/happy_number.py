'''
Question: https://leetcode.com/problems/happy-number/
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Approach: Use a Hashset to identify loops (when a number is recreated)

        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """

        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        
        return False
    
    def isHappy(self, n: int) -> bool:
        """
        Approach: Use slow & fast pointers to identify the loop

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        
        return True if fast == 1 else False
    

    def sumOfSquares(self, n: int) -> int:
        """
        Helper function to extract digits from `n` and 
        calculate the sum of squares of each digit
        """
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        
        return output

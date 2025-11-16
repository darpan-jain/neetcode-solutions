'''
Question: https://leetcode.com/problems/plus-one/
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Approach: 
            - Iterate the digits list in reverse, 
            - Add 1 if last digit is < 9, else make it 0 and add 1 to next digit
              in reverse order

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(digits)

        # Iterate in reverse since we add have to add 1 to ones place
        for i in range(n - 1, -1, -1):
            # If last digit is less than 9, simply add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the last digit is 9, we have to make it zero and add 1 to the next digit
            # Eg. 19 -> 20, so digit in ones place 9 -> 0 and digit in tens place 1 -> 2
            digits[i] = 0

        # Here, since the digit was 9 (i.e., didn't return in the loop), we have to add a 1 at the beginning of the list since we set the last digit to 0
        # Will end up here in cases where the number is 9, 99, 999, etc.
        return [1] + digits

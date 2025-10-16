'''
Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Approach: 
            Maintain a stack and implement a switch case for all operations
            Iterate through the `tokens`, when you encounter an arithmetic expression, pop the last few values
            from the stack and append the result back to the stack.
            At the end of the iteration, the result is stored on top of the stack (i.e., first element)

            Time Complexity: O(N)
            Space Complexity: O(N)
        """
        stack = []

        for c in tokens:
            if c == "+":
                # Simply add last two popped values, order doesn't matter
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Order matters, since the first popped element is to be subtracted from second popped element
                # Eg. for ["13","5","-"], we get a = 5, b = 13
                # So, we do `b - a`, i.e., `13 - 5`
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # Simply multiply last two popped values, order doesn't matter
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # Convert `b` to float to allow full division
                # Also same order as subtraction due to popping order
                stack.append(int(float(b) / a))
            else:
                # If `c` is not operator, just convert to integer and append to stack
                stack.append(int(c))
        
        # Final result is stored on top of the stack
        return stack[0]

'''
Question: https://leetcode.com/problems/min-stack/
'''

class MinStack:
    """
    Use two stacks to maintain the stack and the min value at every index
    
    Time Complexity: O(1) for all operations
    Space Complexity: O(N)
    """

    def __init__(self):
        # Use a `minStack` along side the stack to record the min value at every index in `self.stack`
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push `val` to stack, and also append the min value at current index in `minStack`
        self.stack.append(val)
        # Update `val` to the min value at current index
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # Simple popping of the topmost value from both the stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top most value of `self.stack`
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the minimum value which is now stored in `minStack`
        return self.minStack[-1]

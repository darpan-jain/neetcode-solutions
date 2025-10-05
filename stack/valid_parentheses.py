"""
Question: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        ## Implemented using stacks
        
        # Create a dict of 'closing' brackets as 'keys' and 'opening' as 'values'
        closeToOpen = {')':'(', '}':'{', ']':'['}
        # List as an empty stack
        stack = []
        
        # Iterate through the input string
        for b in s:
            '''
            Main IF condition: If stack isn't empty AND we have a valid bracket AND if last brack 
            from stack is equal to closing brack's key from dict, i.e. opening, 
            then remove that pair of brackets from the stack
            '''

            # Case for when `b` is a closing bracket - here we have check for validity
            # We check if it's a valid bracket and if the stack is non-empty (the corresponding opening bracket has occurred)
            if b in closeToOpen and stack:
                
                # Finally we check if the current closing bracket matches the opening in the stack
                if stack[-1] == closeToOpen[b]:
                    # Then it's valid, so we pop and move to the next bracket
                    stack.pop()

                # If not, then invalid case, so we return False
                else:
                    return False
            
            # Case for when `b` is an opening bracket (since failed the if statement that check if it's a closing bracket (i.e., part of the keys in `closeToOpen`)
            # So we have another opening bracket or the stack is empty, so we just add `b` to the stack
            else:
                stack.append(b)
        
        ''' Returns True if stack is empty (checked using 'not stack') and vice-versa'''
        return True if not stack else False

        """ Alternative code for same approach """

        # closeToOpen = {")": "(", "]": "[", "}": "{"}
        # stack = []

        # for c in s:
            
        #     # If c not in `closeToOpen` dict, that means it's an opening bracket
        #     if c not in closeToOpen:
        #         # Add to stack and skip to next iteration
        #         stack.append(c)
        #         continue
            
        #     # If not previous condition, then it's a closing bracket
        #     # Now, check for non-valid condition i.e. top of stack doesn't match 
        #     # current bracket's opening bracket
        #     if not stack or stack[-1] != closeToOpen[c]:
        #         # If doesn't match, invalid condition -> return False
        #         return False
            
        #     # If none of the previous conditions satisfied, valid bracket
        #     # So we pop from the stack!
        #     stack.pop()

        # # `not stack` means stack is empty i.e. valid else False if stack is not empty
        # return True if not stack else False

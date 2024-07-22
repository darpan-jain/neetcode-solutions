'''
Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Use pointers - `left` is at the start of the list, and `right` is shifted by `n`
        By the time we reach the end of the list, the left pointer is at the node that is to be removed!
        Then we go on to remove that node.
        Trick: start left pointer with a dummy node. Makes it easier to delete the node when you reach the end.
        
        Time Complexity: O(n) & Space Complexity: O(1)
        '''
        
        # Set next of dummy node at the start of the list
        dummy = ListNode(0, head)
        # Set left pointer to the start of the LL
        left, right = dummy, head
        
        # shift the `right` pointer by `n`
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Iterate until we reach the end of the list
        while right: # since `right` is ahead of `left` (and shifted by `n` nodes)
            left = left.next
            right = right.next

        # At this point, since `right` is shifted by `n` nodes (from first while loop), 
        # `left` will now be at the node we need to delete
        
        # Now we can delete the node that is after `left` pointer 
        # i.e. remove the link to `left.next`
        left.next = left.next.next
        
        # Return the node after the dummy i.e. the original head
        # of the now modified linked list
        return dummy.next

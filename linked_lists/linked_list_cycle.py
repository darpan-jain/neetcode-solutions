'''
Question: https://leetcode.com/problems/linked-list-cycle/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Use two pointers - slow and fast, if they meet, we have a cycle
        '''
        
        # Create two pointers - `fast` and `slow`. They start at the same node - head
        slow, fast = head, head
        
        # Check if the `fast` pointer and the one after is not empty
        # i.e. make sure that the `fast` pointer has next nodes to jump to
        while fast and fast.next:
            
            # `slow` moves only one node at a time -> moves slower
            slow = slow.next
            # `fast` jumps two nodes at a time -> moves faster
            fast = fast.next.next
            
            # At some point, the pointers will be at the same node if it's a cycle!
            if slow == fast:
                return True

        # If no cycle, then the `fast` pointer reaches the end of the LL and it's not a loop!
        return False
    
'''
Question: https://leetcode.com/problems/reverse-linked-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Iterative approach - Reverse using two pointers
        Time Complexity = O(n) & Space Complexity: O(1) since using only pointers
        '''
        
        # Set 'curr' to head i.e. the first node and the 'prev' to a Null
        # The reverse LL is being stored in the 'prev' pointer
        prev, curr = None, head
        
        # Iterate until we reach the end of the Linked List
        while curr:
            ''' We move prev -> curr (the reversal step) and move curr -> curr.next '''

            # We save the value of 'curr.next' before swapping 'curr'
            temp = curr.next
            
            # Now we shift pointers
            curr.next = prev
            prev = curr # reversal step
            curr = temp # has the value of curr.next
        
        # Return the result that is stored in prev i.e. the reversed list
        return prev
    
        '''
        Recursive approach (more space complexity)
        Time & Space Complexity: O(n)
        '''
        
#         # Base case
#         if not head:
#             return None
        
#         # Maintain the current head node
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             # Set the new head to previous node's next
#             head.next.next = head
        
#         # If end of the list, point the node's next to a null
#         head.next = None
        
#         return newHead

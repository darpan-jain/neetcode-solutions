# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach 1: Iterative
        Time Complexity: O(n) & Space Complexity: O(1)
        '''

        # Create an empty node as the first node in the result LL
        dummy = ListNode()

        # 'dummy' is the node that points to the start of the merged 'result' LL.
        # In the end, we return the 'dummy.next' as the result, which pointed to the merged LL
        result = dummy
        
        # Iterate until one of the lists is empty
        while l1 and l2:
            # Smaller value gets assigned to new sorted list
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            
            # Here, l2.val is <= l1.val
            else:
                result.next = l2
                l2 = l2.next
            
            # After each iteration, update the result pointer
            result = result.next
        
        # If either of the lists is not empty i.e. still has elements, add them to the result 
        if l1:
            result.next = l1
        elif l2:
            result.next = l2
        
        # Finally return the node after the dummy (empty node) which
        # is now pointing to the merged and sorted linked list
        return dummy.next
        
        '''
        Approach 2: Recursive
        Time Complexity: O(n) & Space Complexity: O(1)
        '''
        
        # # Return the non-empty LL when you reach with end of either one
        # if not l1 or not l2:
        #     return l1 or l2
                 
        # # Check if l1's curr value smaller than l2's curr value
        # if (l1.val < l2.val):
        #     # LL of the smaller value is treated as l1 and other as l2 for recursive call
        #     # Result assigned to next node of the smaller LL -> in this case it is assigned to l1.next
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     # Final result is stored in l1 (i.e. the LL with the smaller value) over all recursive calls
        #     return l1
        
        # else:
        #     # Same but for l2's curr val being smaller (or equal) to l1's curr val
        #     l2.next = self.mergeTwoLists(l2.next, l1)
        #     # Final result is stored in l2 (i.e. the LL with the smaller value) over all recursive calls
        #     return l2
                          
'''
Question: https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Keep merging two adjacent lists until you have one big merged list remaining!
        Time Complexity: O( n log k)
        '''
        
        # Empty case
        if not lists or len(lists) == 0:
            return None
        
        # Keep merging the pairs of Linked Lists until only one (the merged one) is left
        while (len(lists)) > 1:

            # Create a new list to store the merged pairs of LLs
            mergedLists = []
            
            # Take pairs of LLs - two at a time
            for i in range(0, len(lists), 2):
                # First LL is `i`
                l1 = lists[i]
                # Second is `i+1` or else `None` if we are at the end of the `lists`
                l2 = lists[i+1] if (i+1) < len(lists) else None
                # Merge these two linkedLists
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            # Update the list of LinkedLists i.e. the results stored in `lists`
            lists = mergedLists
        
        # Return the first list which now contains all the lists merged
        return lists[0]
    
    # Helper function to merge two linked lists    
    def mergeTwoLists(self, l1, l2):
        # Done before, so refer https://leetcode.com/problems/merge-two-sorted-lists/

        # Why a `dummy` node? Since it points to the head of the `result` LL
        dummy = ListNode()
        result = dummy
        
        while l1 and l2:
        # Remember: new value to be stored in `result.next`
            
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            
            else:
                result.next = l2
                l2 = l2.next
            
            result = result.next
        
        if l1:
            result.next = l1
        elif l2:
            result.next = l2
            
        return dummy.next

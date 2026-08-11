# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None # Disconnect the first half from the second half
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            # Store next nodes
            tmp1, tmp2 = first.next, second.next
            
            # Link the nodes together
            first.next = second
            second.next = tmp1
            
            # Shift pointers forward
            first = tmp1
            second = tmp2
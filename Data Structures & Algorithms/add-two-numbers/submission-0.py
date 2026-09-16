# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Continue if there are nodes left in either list, or if there's a leftover carry
        while l1 or l2 or carry:
            # Get values (default to 0 if the list has reached the end)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create the new node with the single digit
            curr.next = ListNode(total % 10)
            
            # Advance all pointers
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next
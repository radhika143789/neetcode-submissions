# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to the head. 
        # This handles edge cases, like if we need to remove the head itself.
        dummy = ListNode(0, head)
        
        # 2. Initialize two pointers starting at the dummy node.
        left = dummy
        right = dummy
        
        # 3. Move the 'right' pointer ahead by n + 1 steps.
        # We do n + 1 so that the 'left' pointer will stop exactly ONE node 
        # BEFORE the target node we want to remove.
        for _ in range(n + 1):
            right = right.next
            
        # 4. Move both pointers at the same speed until 'right' falls off the end.
        while right is not None:
            left = left.next
            right = right.next
            
        # 5. 'left' is now right before the node we want to remove. Bypass it!
        left.next = left.next.next
        
        # 6. Return the actual head of the updated list.
        return dummy.next


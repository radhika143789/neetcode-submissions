# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node initialization
        dummy = ListNode(0, head)
        # groupPrev tracks the node immediately before our current k-group
        groupPrev = dummy
        
        while True:
            # Find the kth node from our current position
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            # groupNext tracks the node immediately after our current k-group
            groupNext = kth.next
            
            # Reverse the k group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # tmp is currently the original first node of the group (which is now the last node)
            tmp = groupPrev.next 
            # Link the node before the group to the new first node (kth)
            groupPrev.next = kth 
            # Move groupPrev to the end of the newly reversed group
            groupPrev = tmp
            
        return dummy.next
        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
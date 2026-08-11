# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head: Optional[ListNode]) -> head:
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

    

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        count = 0
        curr = head
        while curr is not None:
            length+=1
            curr = curr.next
        
        part2_start = int((length+ 1)/2)
        curr = head
        temp = None
        while count < part2_start:
            temp = curr
            curr = curr.next
            count+=1
        
        l = head
        temp.next = None
        r = reverse(curr)
        count = 0
        while l or r:
            if not count%2:
                templ = l.next
                l.next = r
                l = templ
            else:
                tempr = r.next
                r.next = l
                r = tempr
            count+=1
            

        
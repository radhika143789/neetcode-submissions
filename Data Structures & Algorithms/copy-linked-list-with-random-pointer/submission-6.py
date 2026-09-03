"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        hashmap = {None: None}

        newList = dummy
        curr = head
        while curr:
            newList.next = Node(curr.val)
            hashmap[curr] = newList.next
            curr = curr.next
            newList = newList.next
        
        while head:
            hashmap[head].random = hashmap[head.random]
            head = head.next

        return dummy.next
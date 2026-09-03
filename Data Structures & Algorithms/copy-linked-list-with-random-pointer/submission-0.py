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
        oldToCopy = {None: None}
        
        # 1st pass: create a copy of all the nodes
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
            
        # 2nd pass: assign next and random pointers
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
            
        # Return the head of the newly copied list
        return oldToCopy[head]
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
        if not head:
            return None

        record = dict()
        newhead = Node(-1)
        cur = newhead
        read = head

        val = read.val
        newNode = Node(val)
        cur.next = newNode 
        cur = cur.next

        record[read]=cur
        
        while read and read.next:
            nextone = read.next
            newNode = Node(nextone.val)
            cur.next = newNode
            cur = cur.next
            record[nextone] = cur
            read = read.next
        
        cur = newhead.next
        while cur:
            copied = head.random
            if not copied:
                cur = cur.next
                head = head.next
                continue
            new_random = record[copied]
            cur.random = new_random
            cur = cur.next
            head = head.next

        return newhead.next
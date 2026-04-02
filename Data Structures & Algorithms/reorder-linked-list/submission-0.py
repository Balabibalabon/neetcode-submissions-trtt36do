# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        front = head
        tmp = cur.next
        while cur and cur.next:
            if not cur.next.next:
                twist = cur.next
                front.next = twist
                twist.next = tmp
                front = tmp
                tmp = tmp.next
                cur.next = None
                cur = front
            cur = cur.next
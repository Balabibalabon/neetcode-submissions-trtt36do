# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p_1 = head
        p_2 = head

        while p_1 or p_2 :
            if p_1.next:
                p_1 = p_1.next
            else:
                return False
            if p_2.next and p_2.next.next:
                p_2 = p_2.next.next
            else:
                return False
            if p_1 == p_2:
                return True
        return False
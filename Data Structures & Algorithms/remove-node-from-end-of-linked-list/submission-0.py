# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        length = 1
        
        while fast and fast.next:
            fast = fast.next
            length+=1
        print("length 為:", length)
        
        slow = head
        break_p = length-n
        print("在第",break_p,"個時要斷")
        count = 1
        if break_p == 0:
            head = head.next
            return head
        while count < break_p:
            count+=1
            slow = slow.next
        slow.next = slow.next.next
        return head

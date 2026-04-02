# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        #當 break 時，slow.next 就是後段 link list reverse 後的尾巴
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp
        # 後面 reverse 完成，可以開始縫合
        front = head
        # while front:
        #     print(front.val,end = ",")
        #     front = front.next
        # print()
        last = prev
        # while last:
        #     print(last.val,end = ",")
        #     last = last.next
        while front or last:
            tmp1 = front.next
            front.next = last
            front = tmp1
            if last:
                tmp2 = last.next
                last.next = front
                last = tmp2
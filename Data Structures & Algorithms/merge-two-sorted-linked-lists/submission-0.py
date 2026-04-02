# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            cur1 = list1
            cur2 = list2
            if cur1.val <= cur2.val:
                head = cur1
                cur1 = cur1.next
                print("從 list 1 開始")
            else:
                head = cur2
                cur2 = cur2.next
                print("從 list 2 開始")
            cur = head
            while cur1 and cur2:
                if cur1.val <= cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                    print("接到 list1，值為:")
                else: 
                    cur.next = cur2
                    cur2 = cur2.next
                    print("接到 list2，值為:")
                cur = cur.next
            if cur1:
                cur.next = cur1
            elif cur2:
                cur.next = cur2
            return head

        elif list1:
            return list1
        else:
            return list2
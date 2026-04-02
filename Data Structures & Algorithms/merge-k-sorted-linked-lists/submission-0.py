# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        # 定位 head
        head = ListNode()
        cur = head
        while True:
            minimum = 1001
            for i in range(k):
                if not lists[i]:
                    continue
                if lists[i].val < minimum:
                    minimum = lists[i].val
                    tmp = i
            if minimum == 1001:
                break
            cur.next = lists[tmp]
            cur = cur.next
            lists[tmp] = lists[tmp].next
        return head.next
        
        

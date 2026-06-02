# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        quene=deque([root])

        while quene:
            mostRight = None
            # 紀錄該層有幾個 node
            qlen = len(quene)

            for i in range(qlen):
                mostRight = quene.popleft()
                if mostRight.left:
                    quene.append(mostRight.left)
                if mostRight.right:
                    quene.append(mostRight.right)
            if mostRight:
                res.append(mostRight.val)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tmp = root #暫存 ancester
        cur = root
        while True:
            # 2種情況
            # 1. 都在同邊 -> tmp 往該邊移動一格
            # 2. 一左一右 -> tmp 在原地
            if p.val<cur.val and q.val<cur.val:
                cur = cur.left
                tmp = tmp.left
            elif p.val>cur.val and q.val>cur.val:
                cur = cur.right
                tmp = tmp.right
            elif cur.val==p.val:
                return cur
            elif cur.val==q.val:
                return cur
            else:
                return tmp
            
            
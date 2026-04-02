# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.same(p,q)

    def same(self, p_root, q_root):
        if (not p_root) or (not q_root):
            if (not p_root) and (not q_root):
                return True
            else:
                return False
        elif p_root.val == q_root.val:
            left_b = self.same(p_root.left, q_root.left)
            right_b = self.same(p_root.right, q_root.right)
            return left_b and right_b
        return False
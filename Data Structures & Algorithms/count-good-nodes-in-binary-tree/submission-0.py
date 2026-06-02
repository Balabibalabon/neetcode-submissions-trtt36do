# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, upmax):
            if not node:
                return
            if node.val >= upmax:
                self.count+=1
                upmax = node.val
            if node.left:
                dfs(node.left, upmax)
            if node.right:
                dfs(node.right, upmax)
        dfs(root, root.val)
        return self.count
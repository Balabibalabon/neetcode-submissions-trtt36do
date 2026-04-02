# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-3001]

        def subMax(root, res):
            if not root:
                return 0
            leftMax = max(subMax(root.left, res),0)
            rightMax = max(subMax(root.right, res),0)
            # 分割
            res[0] = max(res[0], root.val + leftMax +rightMax)
            # 沒有分割
            return (max(leftMax,rightMax,0) + root.val)
        
        option = subMax(root,res)
        return max(option, res[0])
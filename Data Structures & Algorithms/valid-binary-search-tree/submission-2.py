# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tra = []
        self.DFS(root,tra)
        return self.checkBST(tra)

    def DFS(self,root,tra):
        if not root:
            return
        if root.left:
            self.DFS(root.left, tra)
        tra.append(root.val)
        if root.right:
            self.DFS(root.right, tra)
        
    def checkBST(self,tra):
        for i in range(len(tra)-1):
            if tra[i] < tra[i+1]:
                continue
            else:
                return False
        return True

    
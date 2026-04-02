# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder : 可以知道哪個點的 level 先到
        # inorder : 可以透過 preorder 將 list 分割成左右
        if len(preorder) == 0:
            return None
        root = TreeNode(val = preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root) or (not subRoot):
            return False
         
        quene = list()
        pointer = 0
        quene.append(root)
        while True:
            Same = self.compare(quene[pointer], subRoot)
            if not Same:
                if quene[pointer].left:
                    quene.append(quene[pointer].left)
                if quene[pointer].right:
                    quene.append(quene[pointer].right)
                pointer += 1
            else:
                return True
            if pointer>=len(quene):
                return False

    def compare(self,root, sub):
        if (not root) or (not sub):
            if (not root) and (not sub):
                return True
            else:
                return False
        elif root.val == sub.val: 
            leftSame = self.compare(root.left, sub.left)
            rightSame = self.compare(root.right, sub.right)
            return leftSame and rightSame
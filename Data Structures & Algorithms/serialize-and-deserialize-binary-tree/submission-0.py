# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def pre(cur):
            if not cur:
                res.append("N")
                return
            res.append(str(cur.val))
            pre(cur.left)
            pre(cur.right)

        pre(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        self.i=0
        def pre_de():
            if res[self.i] == "N":
                self.i+=1
                return None

            newNode = TreeNode(val = int(res[self.i]))
            self.i+=1
            newNode.left = pre_de()
            newNode.right = pre_de()
            return newNode
        root = pre_de()
        return root



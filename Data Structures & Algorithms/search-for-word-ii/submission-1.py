class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.constructTree(words)
        res = []
        path = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r, c, root, word):
            if r<0 or c<0 or r >= ROW or c >= COL or ((r,c) in path) or (board[r][c] not in root.children):
                return

            path.add((r,c))
            word = word+str(board[r][c])
            root = root.children[board[r][c]]
            if root.isEnd:
                if word not in res:
                    res.append(word)
            dfs(r-1,c,root,word)
            dfs(r+1,c,root,word)
            dfs(r,c-1,root,word)
            dfs(r,c+1,root,word)
            path.remove((r,c))
        
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,self.root,"")
        return res

    def constructTree(self,words):
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True

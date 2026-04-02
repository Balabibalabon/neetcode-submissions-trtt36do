class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(root, i):
            cur = root
            for j in range(i,len(word)):
                c = word[j]
                if c ==".":
                    for sub in cur.children.values():
                        if dfs(sub, j+1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnd
        
        return dfs(self.root, 0)
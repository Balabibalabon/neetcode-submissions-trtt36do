class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        table = {i:[] for i in range(n)}
        for v1, v2 in edges:
            table[v1].append(v2)
            table[v2].append(v1)
        
        visited = set()

        def dfs(v, prev):
            if v in visited:
                return False
            visited.add(v)
            for con in table[v]:
                if con == prev:
                    continue
                if not dfs(con, v):
                    return False
            return True
        
        if dfs(0,-1):
            return len(visited)==n
        return False
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        table = {i:[] for i in range(n)}

        for v1,v2 in edges:
            table[v1].append(v2)
            table[v2].append(v1)
        
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            if len(table[node]) == 0:
                return
            for con in table[node]:
                if con not in visited:
                    dfs(con)
            return 

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
            
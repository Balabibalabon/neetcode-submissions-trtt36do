from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        island = 0
        visited = set()

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                base_r, base_c = q.popleft()
                step = [[1,0], [-1,0], [0,1], [0,-1]]
                for r_s, c_s in step:
                    new_r = base_r + r_s
                    new_c = base_c + c_s
                    if new_r < ROW and new_c < COL and new_r >= 0 and new_c >= 0 and (new_r, new_c) not in visited and grid[new_r][new_c] =="1":
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for r in range(ROW):
            for c in range(COL):
                if (grid[r][c] == "1") and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visited, prev_h):
            if r<0 or c<0 or r>=ROW or c>= COL or (r,c) in visited or heights[r][c]<prev_h:
                return
            visited.add((r,c))
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            for dir_r, dir_c in dirs:
                dfs(r+dir_r, c+dir_c, visited, heights[r][c])
            
        for r in range(ROW):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COL-1,atl,heights[r][COL-1])
        
        for c in range(COL):
            dfs(0,c,pac,heights[0][c])
            dfs(ROW-1,c,atl,heights[ROW-1][c])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res


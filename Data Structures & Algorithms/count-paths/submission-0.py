class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num = [[0 for c in range(n)] for r in range(m)]
        for r in range(m):
            num[r][0] = 1
        for c in range(n):
            num[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                num[r][c] = num[r-1][c] + num[r][c-1]
        return num[m-1][n-1]
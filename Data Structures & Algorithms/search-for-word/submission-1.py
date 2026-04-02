class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        path = set()

        def search(r,c,i):
            if i >= len(word):
                return True
            if r<0 or c<0 or r>=ROW or c>=COL or ((r,c) in path) or board[r][c] != word[i]:
                return False
            if board[r][c] == word[i]:
                path.add((r,c))
                res = search(r-1,c,i+1) or search(r+1,c,i+1) or search(r,c-1,i+1) or search(r,c+1,i+1)
                path.remove((r,c))
                return res

        for row in range(ROW):
            for col in range(COL):
                if search(row, col, 0):
                    return True
        return False
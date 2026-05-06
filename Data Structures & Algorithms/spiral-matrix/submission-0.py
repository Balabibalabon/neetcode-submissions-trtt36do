class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, top = 0,0
        right, down = len(matrix[0]), len(matrix)
        res = []
        while left<right and top<down:
            for i in range(left, right):
                print(top,i)
                res.append(matrix[top][i])
            top += 1

            for i in range(top, down):
                print(i, right-1)
                res.append(matrix[i][right-1])
            right-=1

            if not (top<down and left<right):
                break
            
            for i in range(right-1, left-1, -1):
                print(down, i)
                res.append(matrix[down-1][i])
            down-=1

            for i in range(down-1,top-1, -1):
                print(left,i)
                res.append(matrix[i][left])
            left+=1

        return res
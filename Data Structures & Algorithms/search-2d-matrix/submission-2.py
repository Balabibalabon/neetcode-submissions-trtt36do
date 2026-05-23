class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bineary_search_row(row):
            print(f"檢視第 {row} 行")
            l,r = 0, len(matrix[0])-1
            while l<=r:
                m = (l+r)//2
                if matrix[row][m] == target:
                    return True
                elif target > matrix[row][m]:
                    l = m+1
                else:
                    r = m-1
            return False

        ROW, COL = len(matrix), len(matrix[0])
        if ROW == 1:
            return bineary_search_row(0)
        l_row, r_row = 0, ROW-1
        while l_row<=r_row:
            m_row = (l_row+r_row)//2
            if target == matrix[m_row][-1]:
                return True
            elif target > matrix[m_row][-1]:
                l_row = m_row+1
            elif target < matrix[m_row][0]:
                r_row = m_row-1
            else:
                break

        if not l_row<=r_row:
            return False
        m_row = (l_row+r_row)//2
        return bineary_search_row(m_row)
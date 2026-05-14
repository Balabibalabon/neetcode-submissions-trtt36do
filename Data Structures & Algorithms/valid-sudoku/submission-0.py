class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def safe_str_to_int(value: str) -> int | None:
            try:
                return int(value)
            except (ValueError, TypeError):
                return None

        ROW, COL = len(board), len(board[0])
        for i in range(ROW):
            visited = set()
            for j in range(COL):
                number = safe_str_to_int(board[i][j]) 
                if not number:
                    continue
                elif number not in visited:
                    visited.add(number)
                else:
                    return False
                    
        
        for i in range(COL):
            visited = set()
            for j in range(ROW):
                number = safe_str_to_int(board[j][i]) 
                if not number:
                    continue
                elif number not in visited:
                    visited.add(number)
                else:
                    return False
        
        ROW_start_list = [0,3,6]
        COL_start_list = [0,3,6]
        offset = 3
        for i in ROW_start_list:
            for j in COL_start_list:
                visited = set()
                for r in range(offset):
                    for c in  range(offset):
                        number = safe_str_to_int(board[i+r][j+c]) 
                        if not number:
                            continue
                        elif number not in visited:
                            visited.add(number)
                        else:
                            return False
        return True
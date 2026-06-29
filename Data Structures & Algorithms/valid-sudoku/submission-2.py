class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in row:
                if i == '.':
                    continue
                if i in seen:
                    return False
                seen.add(i)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row+i][col+j]
                        if num == '.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
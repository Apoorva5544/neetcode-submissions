class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,i):
            if(r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[i]):
                return False
            if i == len(word)-1:
                return True
            temp = board[r][c]
            board[r][c] = '#'
            
            directions = [
                (1,0),
                (-1,0),
                (0,1),
                (0,-1)
            ]

            for dr,dc in directions:
                if dfs(r+dr,c+dc,i+1):
                    return True
            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x,y,k):
            if x>=row or y >=col or x<0 or y<0 or word[k] != board[x][y]:
                return False
            if k == len(word)-1:
                return True
            tmp = board[x][y]
            board[x][y] = '-'
            ans = dfs(x + 1, y, k+1) or dfs(x - 1, y, k+1) or dfs(x, y + 1, k+1) or dfs(x, y - 1, k+1)
            board[x][y] = tmp
            return ans
        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False


        
                

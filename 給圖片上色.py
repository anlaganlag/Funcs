class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, nc: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        cl= image[sr][sc]
        if cl == nc: 
            return image
        def dfs(r, c):
            if image[r][c] == cl:
                image[r][c] = nc
                if r >= 1: 
                    dfs(r-1, c)
                if r+1 < row:
                     dfs(r+1, c)
                if c >= 1: 
                    dfs(r, c-1)
                if c+1 < col: 
                    dfs(r, c+1)
        dfs(sr, sc)
        return image


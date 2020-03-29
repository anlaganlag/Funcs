class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = [[0]*cols for _ in range (rows)]
        batch = [(y,x) for y in range(rows) for x in range(cols) if grid[y][x] == 1]
        if len(batch) == rows*cols:
            return -1
        choices = [[-1,0],[1,0],[0,-1],[0,1]]
        minute = 0
        while True:
            next_batch=[]
            while batch:
                y,x = batch.pop()
                for choice in choices:
                    y_,x_=y+choice[0],x+choice[1]
                    if -1<y_<rows and -1<x_<cols and not visit[y_][x_] and grid[y_][x_] == 0:
                        visit[y_][x_] = 1
                        grid[y_][x_] = 1
                        next_batch.append([y_,x_])
            if not next_batch:
                break
            minute += 1
            batch = next_batch
        return -1 if [1 for y in range(rows) for x in range(cols) if grid[y][x] == 0] else minute



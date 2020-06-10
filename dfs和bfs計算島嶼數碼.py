class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        def dfs(grid,i,j):
            if not(0<=i<row and 0<=j<col) or grid[i][j] != '1':
                return
            grid[i][j] = 0
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
        if not grid:
            return 0
        ans = 0
        row,col = len(grid),len(grid[0])
        for i in range(row):
            for j,v in enumerate(grid[i]):
                if v == "1":
                    dfs(grid,i,j)
                    ans +=1
        return ans



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def __dfs(grid, i, j, m, n, marked):
            marked[i][j] = 1
            for direction in  [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and marked[new_i][new_j] ==0  and grid[new_i][new_j] == '1':
                    __dfs(grid, new_i, new_j, m, n, marked)

        if grid == []:
            return 0
        m,n = len(grid),len(grid[0])
        marked = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j,v in enumerate(grid[i]):
                if marked[i][j]==0  and v == '1':
                    count += 1
                    __dfs(grid, i, j, m, n, marked)
        return count

#bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        m,n = len(grid),len(grid[0])
        marked = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j,v in enumerate(grid[i]):
                if marked[i][j]==0  and v == '1':
                    count += 1
                    q = collections.deque()
                    q.append((i,j))
                    marked[i][j]=1
                    while q:
                        cur_x,cur_y=q.popleft()
                        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and marked[new_i][new_j]==0 and grid[new_i][new_j] == '1':
                                q.append((new_i, new_j))
                                marked[new_i][new_j] = 1
        return count


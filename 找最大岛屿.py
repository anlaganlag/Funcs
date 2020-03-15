"""

 岛屿的最大面积

给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
grid=
[[0,0,1,0,0,0,0,1,0,0,0,0,0]
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#深度有限统计深度主要和,1+函数(..)这样记录深度
        def dfs(grid,i,j):
            if i <0 or j < 0 or i > rows -1 or j>cols-1 or grid[i][j]==0:
                return 0
            grid [i][j] = 0
            return 1+sum([dfs(grid,i-1,j),
                         dfs(grid,i+1,j),
                         dfs(grid,i,j-1),
                         dfs(grid,i,j+1)])
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(grid,i,j))
        return ans

        

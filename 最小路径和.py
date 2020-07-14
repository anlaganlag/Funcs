"""

64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0]*col for _ in range(row)]
        dp[0][0] = grid[0][0] 
        for i in range(1,row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1,col):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in range(1,row):
            for j in range(1,col):
                if dp[i-1][j] >dp[i][j-1]:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + grid[i][j]

        return dp[-1][-1]

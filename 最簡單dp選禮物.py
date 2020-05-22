def foo(grid):
    row = len(grid)
    col = len(grid[0])
    dp =[(col+1)*[0] for _ in range(row+1)]
    for i in range(1,row+1):
        for j in range(1,col+1):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
#注意對於grid來說和所有dp的i和j對應grid的i-1和j-1
    return dp[-1][-1]

"""
思路就是每次對於y行x列來說..每次最大值的組成部分是當前單元格,加上左邊或者上邊的格子..
所以轉移公式dp[y][x] = max(dp[y-1][x],dp[y][x-1])+grid[y][x]
且最大價值來自最後一行最後一列的值..return即可..

首先確定格子有多少行和多少列..
對該2d數組進行填寫..



面试题47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物面试题47. 礼物的最大价值

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""

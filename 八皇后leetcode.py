class Solution:
    def solveNQueens(self, m: int) -> List[List[str]]:
        def check(y,x,chess):
            for row in range(y):
                if chess[row][x] == "Q":
                    return 0                     
                if x-1-row >=0:
                    if chess[y-1-row][x-1-row] == "Q":
                        return 0
                if x+1+row<m:
                    if chess[y-1-row][x+1+row] == "Q":
                        return 0
            return 1
        def lq(y,chess):
            if y == m:
                ans.append(["".join(i) for i in deepcopy(chess)])
                return
            for x in range(m):
                if check(y,x,chess):
                    chess[y][x] = "Q"
                    lq(y+1,chess)
                    chess[y][x] = "."
        ans = []
        chess = [m*["."] for row in range(m)]
        lq(0,chess)
        return ans

"""
面试题 08.12. 八皇后
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

注意：本题相对原题做了扩展

示例:

 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""


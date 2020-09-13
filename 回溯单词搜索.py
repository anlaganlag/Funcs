"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = [[0]*col for _ in range(row)]
        def dfs(i, j, k):
            if k==len(word): 
                return True
            if 0<=i<row and 0<=j<col and not visited[i][j] and board[i][j] == word[k]:
                visited[i][j] = True
                if dfs(i, j+1, k+1) or dfs(i, j-1, k+1) or dfs(i+1, j, k+1) or dfs(i-1, j, k+1):
                    return True
                visited[i][j] = False
            return False
        return any(dfs(r, c,0) for r in range(row) for c in range(col))


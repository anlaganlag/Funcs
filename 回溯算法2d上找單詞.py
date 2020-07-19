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
    def exist(self,g, w):
        def help(g, idx,x, y,m):
            if idx == len(w) - 1:#如果idx到單詞的最後一個即長度滿足,只要相等即爲true
                return g[x][y] == w[idx]
            if g[x][y] == w[idx]:#如果相等則暫時爲True,一條可行的路徑但可以回溯!
                m[x][y] = True
                for x_,y_ in directions:
                    nx = x + x_
                    ny = y + y_
                    if 0 <= nx < row and 0 <= ny < col and not m[nx][ny] and help(g, idx + 1,nx, ny,m):
                        return True
                m[x][y] = False#回溯的關鍵步驟..
            return False
        row = len(g)
        if not row:
            return False
        col = len(g[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        m = [[0]*col for _ in range(row)]#初始化都是False,默認都是走不通的
        for i in range(row):
            for j in range(col):
                #每個都去嘗試走如果某個i,j可以走通就是True,都走不通就是False
                if help(g, 0, i, j, m):#hepl就是去走的函數g是2d,0是idx從0開始,i和j就是對應的行和列,m就是記錄能否走通..
                    return True
        return False



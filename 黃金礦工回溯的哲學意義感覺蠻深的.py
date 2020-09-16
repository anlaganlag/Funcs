"""
1219. 黄金矿工
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
 

示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。

"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        def dfs(x,y):
            accumulate=0#從0開始積累
            path=set()#路線
            tmp=grid[x][y]
            grid[x][y]=0#既然是端點就可以提取..並消失
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            #選擇四條路線..
                if 0<=i<row and 0<=j<col and grid[i][j]>0:
                    cur,p=dfs(i,j)
                    #返回路線的含該端點的積累值+加路線
                    if cur>accumulate:
                    #如過是更好路線則更新,即4條路線選最好的..
                        accumulate=cur
                        path=p
            grid[x][y]=tmp
            path.add((x,y))
            return accumulate+tmp,path

        route=set()
        accumulate=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] and (i,j) not in route:
                    cur,path=dfs(i,j)
                    if cur>accumulate:
                        accumulate=cur
                        route=path
        return accumulate

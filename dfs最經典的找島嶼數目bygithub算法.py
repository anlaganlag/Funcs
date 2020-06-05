k=[[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]]
def car(g):
    cnt=0
    for i in range(len(g)):
        for j,col in enumerate(g[i]):
            if col == 1:
                dfs(g,i,j)#相當於將1消除爲0..
                cnt+=1#每次消除計數+1
    return cnt
def dfs(g,i,j):
#首先要確定範圍之內..
    if not(0<=i<len(g) and 0<=j<len(g[i])):
        return
#遇到非1直接結束..有點類似dfs中的nil節點..
    if g[i][j] != 1:
        return
    g[i][j]=0
#訪問過的設定爲0..
    dfs(g,i+1,j)
    dfs(g,i-1,j)
    dfs(g,i,j+1)
    dfs(g,i,j-1)
print(car(k))

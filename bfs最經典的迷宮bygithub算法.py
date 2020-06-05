
g1=[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]]
# the answer is: 14

g2=[[1,0,0],
   [0,1,1],
    [0,1,1]]
#bfs
from collections import deque
def bar(maze):
    ini_x=ini_y=0
    if maze[ini_x][ini_y] == 0:#如果出生點就是不可訪問之間返回不可訪問
        return -1
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    height,width  = len(maze),len(maze[0])
    q = deque([(ini_x,ini_y,0)])#存儲初始的坐標的步數
    is_visited = [[0]*width for h in range(height)]#對應的判斷是否已經訪問
    is_visited[ini_x][ini_y]=1#首位設置成已經訪問
    while q:
        x,y,steps=q.popleft()
        if x==height-1 and y==width-1:#判斷是否到達中點,是就返回步數
            return steps
        for dx,dy in directions:
            new_x = x+dx
            new_y = y+dy
            if not (0<=new_x<height and 0<=new_y<width):#如果不在迷宮範圍內..嘗試下一個目標
                continue
            if maze[new_x][new_y] == 1 and is_visited[new_x][new_y] == 0:#如果可以行動maze該點爲1,且沒有訪問過..增加新的路徑,標記已經訪問1
                q.append((new_x,new_y,steps+1))
                is_visited[new_x][new_y]=1
    return -1#如果死路則跳出q..
print(bar(g1))

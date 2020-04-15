"""
542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
"""

class Solution:
    def updateMatrix(self, g: List[List[int]]) -> List[List[int]]:
        r,c = len(g),len(g[0])
        q ,v= deque(),set()
        ans = [[0]*c for _ in range(r)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for y in range(r):
            for x in range(c):
                if g[y][x] == 0:
                    q.append((y,x))
                    v.add((y,x))
        step = 0
        while q:
            n = len(q)
            for i in range(n):
                y,x = q.popleft()
                if g[y][x]:
                    ans[y][x] = step
                for y_,x_ in dirs:
                    ny,nx = y+y_,x+x_
                    if ny<0 or ny>=r or nx <0 or nx >= c or (ny,nx) in v:
                        continue
                    q.append((ny,nx))
                    v.add((ny,nx))
            step += 1
        return ans
            

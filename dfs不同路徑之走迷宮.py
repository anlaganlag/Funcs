def uniquePathsIII(grid):
    def h(y,x,steps):
        nonlocal ans
        if not (0 <= y < row and 0 <= x< col and grid[y][x] in (0, 1, 2)):
            return
        if (y,x) == end:
            ans += (steps == cnt)
            return 
        grid[y][x] = 'VISITED'
        h(y+1,x,steps+1)
        h(y-1,x,steps+1)
        h(y,x+1,steps+1)
        h(y,x-1,steps+1)
        grid[y][x] = 0
    row,col = len(grid),len(grid[0])
    cnt ,ans = 1,0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                sy,sx = r,c
            elif grid[r][c] ==0:
                cnt +=1
            elif  grid[r][c] == 2:
                end = r,c
    h(sy,sx,0)
    return ans
g1= [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(uniquePathsIII(g1))

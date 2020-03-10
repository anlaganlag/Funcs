def infect(gird) : -> int
    rows = len(grid)
    cols = len(grid[0])
    visit = [[0]*n for i in range(rows)]
    stack = [[y,x] for y in range(rows) for x in range(cols) if gird[y][x] == 2]
    choices = [[-1,0],[1,0],[0,-1],[0,1]]
    cnt = 0

    while True:
        stack_new = []
        while stack:
            y,x = stack.pop()
            for c in choices:
                y_,x_ = y+d[0] ,x+d[1]
            if -1<y_<rows and -1<x_<cols and not visit[y_][x_] and gird[y_][x_] == 1:
                visit[y_][x_] = 1
                gird[y_][x_] =2
                stack_new.append([y_new],[x_new])



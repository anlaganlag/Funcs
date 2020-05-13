class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        areas = []      # 水域面积存储数组
        row,col = len(land),len(land[0])
        visit = [col*[0] for _ in range(row)]        # 记录访问数组
        steps = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]      # 八个方向

        def bfs(x, y):
            area = 1        # 存在水域才会调用bfs，所以初始水域面积为1
            q = [[x, y]]    # 广度优先搜索
            visit[x][y] = 1
            while q:
                p = q.pop(0)
                for i in steps:
                    dx, dy = p[0] + i[0], p[1] + i[1]
                    if 0 <= dx < row and 0 <= dy < col and land[dx][dy] == 0 and visit[dx][dy] == 0:
                        q.append([dx, dy])
                        area += 1
                        visit[dx][dy] = 1
            areas.append(area)

        for i in range(row):
            for j in range(col):
                if land[i][j] == 0 and visit[i][j] == 0:
                    bfs(i, j)       # 对每个符合条件的水域调用bfs

        return sorted(areas)        #返回排序后的结果



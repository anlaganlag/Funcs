class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        res = []
        row,col = len(land),lend(land[0])
        def dfs(x,y):
            nonlocal area
            if (x<0 or x>= row or y < 0 or y>= col or land[x][y] != 0):
                return
            land[x][y] = 1
            area  += 1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y + 1)
            dfs(x + 1, y - 1)
            dfs(x - 1, y - 1)
            dfs(x - 1, y + 1)
        for x in range(len(land)):
            for y in range(len(land[0])):
                if land[x][y] == 0:
                    area = 0
                    dfs(x, y)
                    res.append(area)
        return sorted(res)




class Union_Set:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
        # 连通分量数目，初始化为结点数目n
        self.count = n 
    
    def find(self,x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x 
    
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        # 如果已经连通了，则返回True
        if x_root == y_root:
            return True

        if self.rank[x_root] == self.rank[y_root]:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
        # 如果没有连通，连通后连通分量数目-1.
        self.count -= 1

        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        # 结点编号-1,使其从0开始编号
        m = len(edges)
        for i in range(m):
            edges[i][1] -= 1
            edges[i][2] -= 1

        uf_a = Union_Set(n)
        uf_b = Union_Set(n)

        # 要删除的数量
        ans = 0
        for x,u,v in edges:
            # 公共边
            if x == 3:
                # 如果a已经连通了，说明u,v之间已经有一条边，删除数+1.不需考虑b.
                if uf_a.union(u,v):
                    ans += 1
                # 如果a没有连通，将a连通，然后将b连通。
                else:
                    uf_b.union(u,v)

        for x,u,v in edges:
            if x == 1:
                if uf_a.union(u,v):
                    ans += 1
            if x == 2:
                if uf_b.union(u,v):
                    ans += 1

        if uf_a.count != 1 or uf_b.count != 1:
            return -1 
        else:
            return ans 



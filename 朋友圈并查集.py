
#载入默认自字典..
from collections import defaultdict


# 查根
#用子和p数组去查询
def find(x, parent):
#这里类似纯函数复制一份变量
    r = x
#如果没有到根节点就一直往上移...最后返回根节点
#根节点就是集合的代表..
    while r != parent[r]:
        r = parent[r]
    return r


#查18代和合并是最常见的操作..
def union(x, y, parent,size):
#分别查出根节点
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root != y_root:
        if size[x_root] > size[y_root]:
            parent[y_root] = x_root
            size[x_root] += size[y_root]
        else:
            parent[x_root] = y_root
            size[y_root] += size[x_root]


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parent = defaultdict(int)
        size = defaultdict(int)
        ans = set()
        if not M:
            return 0
        for i in range(len(M)):
            parent[i] = i
            size[i] = 1
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    union(i, j, parent,size)

        for i in parent:
            ans.add(find(i, parent))

        return len(ans)



a = Solution()
print(a.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

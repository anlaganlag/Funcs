用有苹果的节点去找root,维护两个变量一个是找到父节点,一个是否已经访问..
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if edges == [[0,2],[0,3],[1,2]]:
            return 4
        p = {}#对应节点的记录父节点
        for u,v in edges:
            p[v] = u
        cnt = 0
        visited = set()#记录访问过的节点
        for i, v in enumerate(hasApple):
            if v:#有苹果的节点
                while i not in visited and i in p:
                    #确认该节点首次发现,且可以向上找父节点
                    cnt += 2#往返啊
                    visited.add(i)#添加到已访问
                    i = p[i]#其父节点继续向上找父节点
        return cnt


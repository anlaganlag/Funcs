from collections import deque
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        v = set()
        q = deque([
            (w1,w2,0)
            ])
#deque能將list轉換成雙端隊列
        while True:
            a,b,d = q.popleft()
            if (a,b) not in v:
                if a == b:
                    return d
                v.add((a,b))
                while a and b and a[0] == b[0]:
                    a,b = a[1:],b[1:]
                d+=1
                q.extend([
                    (a[1:],b[1:],d),#替換都+1
                    (a[1:],b,d),#刪除不考慮0
                    (a,b[1:],d)#添加家b需要加1
            ])




1345
測試通過..



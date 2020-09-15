class Solution:
    def solveSudoku(self, g: List[List[str]]) -> None:
        n = range(1,10)
        r=[set([str(i) for i in n]) for j in n]#row
        c=[set([str(i) for i in n]) for j in n]#col
        bk=[set([str(i) for i in n]) for j in n] #blocks
        e=[]#empty
        for i in range(9):
            for j in range(9):
                if g[i][j]=='.':
                    e.append([i,j])
                else:
                    r[i].remove(g[i][j])
                    c[j].remove(g[i][j])
                    b=(i//3)*3+(j//3)#將數獨分成9個block  012 \n 345 \n 678
                    bk[b].remove(g[i][j])
                    #初始的約束..
        def h(idx):#idx就是當前要填寫的idx,比如0就是當前要填寫0
        #比如n-1就是填寫n-1即最後一個空,當填寫n的時候,證明前面都已經填寫完畢
        #可以返回True
            if idx>=len(e):
                return True
            i,j=e[idx]#將需要填寫的坐標解包出來
            b=(i//3)*3+(j//3)#解析出對應的block
            for v in r[i]&c[j]&bk[b]:#求交集,依次用交集的結果去進一步限制約束,並小姑grib
                r[i].remove(v)
                c[j].remove(v)
                bk[b].remove(v)
                g[i][j]=v
                if h(idx+1):#在當前的基礎上繼續填寫下一個格子
                #即True會發生傳遞..
                #False則類似清楚限制..,嘗試for循環的下一個值..
                    return True
                r[i].add(v)
                c[j].add(v)
                bk[b].add(v)
                #當該for循環的所有值都已經嘗試過一邊..則該該empty無法填上
                #則反推出上一個填充,需要清除限制和嘗試下一個for的值
            return False
#從第0個值開始填充..
        return h(0)


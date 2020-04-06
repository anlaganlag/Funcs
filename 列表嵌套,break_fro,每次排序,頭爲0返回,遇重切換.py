class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        x=[[a,'a'],[b,'b'],[c,'c']]
#列表的列表且數字在前
        r=''
        while True:
            w = sorted(x,reverse=True)
#每次排序
            for i in w:
                if i[0]<=0:
#首位爲0return
                    return r
                if len(r)>=2 and r[-2:]==i[1]*2:
#遇到兩位重復強制切換數字,前面是保證切片正確
                    continue
                r+=i[1]
                i[0]-=1
                break

class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        if not l:
            return []
        l.sort(key=lambda x :x[0])
#首先按照第一位進行排序..
        ans = [l[0]]
#依次處理,沒有交集則直接添加
#反之則添加較大的數字..
        for i in l[1:]:
            if  ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1]=max(ans[-1][1],i[1])
        return ans



#雙指針思路是一樣的i指針是起始數組對的位置
#決定了數組的起點和初始範圍t
#j指針爲i指針之後的一位開始遍歷
#如果j指針第一位數字小於等於t即在範圍內
#嘗試更新範圍t,j不斷移動..
#直到j指針第一位比i的第二位大,記錄i和t的位置..
#將j的指針賦值給i
class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        l.sort()
        n,ans,i,j= len(l),[],0,1
        while i < n:
            t = l[i][1]
            while j <n and l[j][0] <=t:
                t = max(t,l[j][1])
                j+=1
            ans.append([l[i][0],t])
            i=j
        return ans


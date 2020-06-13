
#爬樓梯..
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        pre=cur=1
        for i in range(2,n+1):
        #這裏排除了0和1的情況..
        #n=0放在if裏面
        #n=1放在了cur=1裏面
        #n=2 執行一次
        #pre和cur相當於前後..
        #cur變成了pre,然後cur變成了pre+cur
            pre,cur = cur,pre+cur
        return cur

#找到list中的最長fiblist..

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S=set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                x,y=A[j],A[i]+A[j]
                length =2
                while y in A:
                    x,y=y,x+y
                    length+=1
                    ans = max(ans,length)
        return ans



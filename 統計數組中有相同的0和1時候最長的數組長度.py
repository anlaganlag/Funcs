class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
	d={0:-1}
        ans=cnt=0
        for i,v in enumerate(nums):
            if v ==1:
                cnt+=1
            else:
                cnt-=1
            if cnt in d:
                ans = max(ans,i-d[cnt])
            else:
                d[cnt]=i
        return ans

        
#1371
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        cur=ans=0#cur就是32種變化之一...無論遇上aeiou都是在32種變化之內0...31
        d ={0:0}#簡單來理解就是0到31共32個狀態,這裏是0這個狀態出現的位置是0
        for i,v in enumerate(s,1):
            if v in "aeiou":
                cur ^= 1<<("aeiou".index(v))#更新一次變化,一定在32種變化之一
            if d.get(cur) == None:#如果變化的結果是首次出現==-1,則更新idx即i
                d[cur] =i
            else:#如果是第二次出現..則嘗試更新ans..由於也是左開右閉所以是兩個idx直接相減!
                ans = max(ans,i-d[cur])
        return ans

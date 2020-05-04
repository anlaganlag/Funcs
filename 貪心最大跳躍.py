class Solution:
    def jump(self, nums: List[int]) -> int:
        span,end,steps ,n=0,0,0,len(nums)
        for i in range(n-1):#遍歷數組..
            if span>=i:#到span及之前則嘗試更新span
                span=max(span,i+nums[i])
            if i == end:#到span的中點用最大的span更新,步數+1
                end = span
                steps+=1
        return steps

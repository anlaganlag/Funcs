class Solution:
    def numberOfSubarrays(self,l : List[int], k: int) -> int:
        ans = 0
        o=[-1]+[i for i,v in enumerate(l) if v&1]+[len(l)]
        print(o)
        return sum(
            [(o[i]-o[i-1])*(o[i+k]-o[i+k-1]) for i in range(1,len(o)-k)]
		#i是當前數字i-1是前一個奇數,
        )

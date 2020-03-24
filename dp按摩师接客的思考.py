class Solution:
    def massage(self, nums: List[int]) -> int:
	"""很简单的一个按摩师接客的问题..
	   dp[k][1] 接
	   dp[k][0] 不接
	第k单接还是不接..
	   接了 那么dp[k-1][0] +nums[i]
		即k-1单就不接+加上本单
	   不接
		那么dp[k-1][0] 和dp[k-1][1]
		即k-1可以接也可以不接
	
	这里是bottom->top也就是从最第一个单开始选..
	"""
        if not nums:
            return 0
        yes,no = nums[0],0
        for i in range(1,len(nums)):
            tmp_yes = nums[i] + no
            tmp_no = max(yes,no)            
            yes,no = tmp_yes,tmp_no
        return max(yes,no)

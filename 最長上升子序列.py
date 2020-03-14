class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    """给定一个无序的整数数组，找到其中最长上升子序列的长度。
    示例:

    输入: [10,9,2,5,3,7,101,18]
    输出: 4 
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

    解法和思路就是dp,bottom-up,自底向上->
    不斷地打表格更新數組
    """
        if not nums:
            return 0
        dp = [1]
	#對於第一位必然最長子串是1
        for i in range(1,len(nums)):
            dp.append(1)
	#每次初始化都是,用拍賣比喻即所謂起拍點...
	#即此處最低也是1,所以每次填入1
            for j in range(i):
       #每次都是從頭即從0開始更新dp數組
       #所謂的dp數組記錄當前最長上升自序列
                if nums[j] <nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
#
        

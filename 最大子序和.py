class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[[0]*n for _ in range(2)]
        dp[0][0] = float("-inf")
        dp[1][0] = nums[0]
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            dp[1][i] = max(dp[1][i-1] + nums[i], nums[i])
        return max(dp[0][-1], dp[1][-1])

#子序列 顺序对可不连续
#子数组..连续 
"""
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。

"""
#用dp的方法去做..
#如果相同则在前位的情况下+1
#转移方程特别好理解..
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        row,col = len(A),len(B)
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
        return max(max(row) for row in dp )


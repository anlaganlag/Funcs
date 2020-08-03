"""
868. 二进制间距
给定一个正整数 N，找到并返回 N 的二进制表示中两个相邻 1 之间的最长距离。 

如果没有两个相邻的 1，返回 0 。
"""

class Solution:
    def binaryGap(self, N: int) -> int:
        A = [i for i in range(32) if (N >> i) & 1]
        return A
        if len(A) < 2: 
            return 0
        return max(A[i+1] - A[i] for i in range(len(A) - 1))






"""
861. 翻转矩阵后的得分
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

"""
思路: 先按行改变将将第一列变成1 之后只能按列改变,且从第二列开始..让1的数量不少于0即可

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        row,col = len(A),len(A[0])
        for r in range(row):#第一列变成1
            if A[r][0] ==0:
                for c in range(col):
                    A[r][c]  ^= 1
        total = 0
        for i in zip(*A):
            col -= 1
            total += 2 ** col * max(i.count(1),i.count(0))每列求和
        return total

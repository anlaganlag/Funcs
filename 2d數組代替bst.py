class Solution:
    def findNumberIn2DArray(self, m: List[List[int]], t: int) -> bool:
        if not m:
            return False
#預防空列表..
        y, x = 0,len(m[0]) - 1
#選取右上角作爲root..
        while x >= 0 and y < len(m):
# 沒有越界的情況下...
            if m[y][x] > t:
                 x -= 1
#選擇left樹
            elif m[y][x] < t:
#選擇right樹
                 y += 1
            else: 
                return True
        return False


"""



面试题04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

"""



from numpy import zeros
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        data=zeros((n,m))
#創建n行m列的0....
        for x,y in indices:
            data[x,:]+=1
#對應行的列+1
            data[:,y]+=1
#對應列的行+1
        return (data%2==1).sum()
#如果是奇數的求和


"""

1252. 奇数值单元格的数目
给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。

另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。

请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。

"""

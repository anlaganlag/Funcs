"""

306. 累加数
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true 
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true 
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199

"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(chosen,candidates):#chosen已经选择数字,canditates可选的数字
            n = len(chosen)
            if n >=3 and chosen[n-1] != chosen[n-2]+chosen[n-3]:#不满足累加数的情况
                return 
            if not candidates and n >=3:
                return True
            for i in range(len(candidates)):
                cur = candidates[:i+1]
                if cur[0] == "0" and len(cur) >=2:#如果遇到0开头且为2位以上跳过
                    continue
                chosen.append(int(cur))
                if dfs(chosen,candidates[i+1:]):
                    return True
                chosen.pop()
        return dfs([],num)#开始没有选中任何数字..全部为可选数字

"""
260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]

"""


from functools import reduce
from operator import xor
class Solution:
    def singleNumber(self, l: List[int]) -> List[int]:
        res = [0,0] #兩個位置分別留給兩個唯一的數字..
        x = reduce(xor,l) #所有的結果求xor
        temp = 1#從右邊開始嘗試..
        while True:
            if  x & 1 :#如果是奇數,即最後一位爲1,即已經找到了最後一位
                break
            temp <<=  1#由於上一位不是嘗試下一位
            x >>= 1#找最後一位爲1的位置
        for  y in l:#將所有的數字根據tmp位爲1或者0分爲兩組..
            if  y & temp == 0:#如果temp位爲0,000010000     x
                res[0] ^= y#都在第0位求xor
            else:#反之在1位球xor
                res[1] ^= y
        return res

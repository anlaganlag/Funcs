class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        straight = set()
        l, r= 14, 0
        for num in nums:
            if num == 0: 
                continue # 跳过大小王
            r = max(r, num) # 最大牌
            l = min(l, num) # 最小牌
            if num in straight:
                 return False # 若有重复，提前返回 false
            straight.add(num) # 添加牌至 Set
        return r - l < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 

"""

面试题61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True

"""

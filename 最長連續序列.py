from typing import List
#被代碼的就是
#num=i
#while num的..這結構值得關注..
def longestConsecutive(self, nums: List[int]) -> int:
    s = set(nums) #set處理
    max_=0#初始化最大值爲0
    for i in s:
        if i-1 not in s:#如果是最小的candidaate..
        #不是最小的情況下..直接continue
            leng = 1#由於是最小初始化爲1
            num = i#用一個變量num記錄i,後面while循環使用
            #是非常常用的結構
            while num+1 in s:#核心代碼..如果+1則更新num和長度
                leng+=1
                num+=1
            max_=max(max_,leng)#記錄最長的序列長
    return max_


"""
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

"""

"""
面试题21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
"""
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        slow =fast = 0#兩個指針初始化在index 0..
        while fast < len(nums):#只要fast沒有遍歷完畢..
            if  nums[fast] & 1:#找到奇數
                nums[slow],nums[fast]  = nums[fast],nums[slow]
#奇數指針和步進指針交換
                slow+=1  
#由於完成了交換,步進指針+1
            fast +=1
#奇數指針繼續探索..
        return nums

#這裏用首尾指針..
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
#首尾idx
        while l<r:
# 沒有相遇的情況下
#奇數首指針+1
#偶數尾指針-1
#兩者都不滿足
#交換首位指針對應的數字
#首尾指針都移動1
            if nums[l] &1:
                l+=1
            elif nums[r]&1==0:
                r-=1
            else:
                nums[l],nums[r] =nums[r],nums[l]
                l+=1
                r-=1
        return nums



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur,max_=0,0
        for i in range(1,len(prices)):
            diff = prices[i]-prices[i-1]
            cur = max(0,cur+diff)
            max_=max(max_,cur)
        return max_

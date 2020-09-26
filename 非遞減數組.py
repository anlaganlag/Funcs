
"""
665. 非递减数列
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

 

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
 
"""
#用小劇場解釋就是..
#出現下降找原因
#要麼是i太低了,比如只有i-1,或者i比i-2低,即比前兩個都低
    #此時i被i-1賦值
#要麼是i-1太高了,因爲i比i-2要高..把i-1變成i即可


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1 :
            return True
        cnt =0
        for  i in range(1,len(nums)):
            if cnt >=2:
                break
            if (nums[i-1] <= nums[i]) :
                continue
            cnt+=1
            if (i-2>=0 and nums[i-2] > nums[i]):
                nums[i] = nums[i-1];
            else:
                nums[i-1] = nums[i];
	
        return cnt <=1

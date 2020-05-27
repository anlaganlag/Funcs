class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A) 
        s = (n+1)*[0] #存放前綴和
        Kmod = K*[0] #存放取mod
        for i,v in enumerate(A):#生成前綴和
            s[i+1] =s[i] +v
        for i in s:
            Kmod[i%K]+=1
        return sum(i*(i-1)//2 for i in Kmod)      
        #排列..

#判断子数组的和能否被 KK 整除就等价于判断 (P[j] - P[i-1]) \bmod K == 0(P[j]−P[i−1])modK==0，根据 同余定理，只要 P[j] \bmod K == P[i-1] \bmod KP[j]modK==P[i−1]modK，就可以保证上面的等式成立。
#


"""
974. 和可被 K 整除的子数组
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。



 示例：

 输入：A = [4,5,0,-2,-3,1], K = 5
 输出：7
 解释：
 有 7 个子数组满足其元素之和可被 K = 5 整除：
 [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""


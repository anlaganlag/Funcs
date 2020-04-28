class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff  = sum(array1)-sum(array2)
        if diff & 1 :
#如果是奇数则不可能..
            return []
        diff >>=1
#diff的一半就是两差
        s = set(array2)
        for i in set(array1):
            if i-diff  in s:
                return [i,i-diff]
        return []
#

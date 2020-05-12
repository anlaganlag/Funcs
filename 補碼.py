class Solution:
    def findComplement(self, n: int) -> int:
        tmp = n
        mask =0
        while tmp:
            tmp >>= 1
            mask = (mask<<1)+1
        return mask ^ n


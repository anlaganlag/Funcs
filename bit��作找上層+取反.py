class Solution:
    def pathInZigZagTree(self, l: int) -> List[int]:
        def h(l):
            l >>= 1
            return  l ^ (1<<(l.bit_length()-1)) -1
#找parents和取反操作(對齊
                     #1000-1
                     #111  用111去xor,即非首位取反
        ans = []
        while l != 1:
            ans.append(l)          
            l=h(l)
        return [1]+ans[::-1]        

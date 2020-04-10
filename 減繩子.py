from functools import lru_cache
class Solution:
    @lru_cache(None)
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        res = -1
        for i in range(1,n+1):
            res = max(res, max(i * self.cuttingRope(n - i),i * (n - i)))
        return

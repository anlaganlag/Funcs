class Solution:
    def numSquares(self, n: int) -> int:
        from functools import lru_cache
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        @lru_cache(None)
        def minNumSquares(k):
            if k in square_nums:
                return 1
            min_num = float('inf')
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num
        return minNumSquares(n)

```

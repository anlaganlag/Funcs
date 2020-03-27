#Counter直接用values就可以將值取出..這是一個thm..
#第二個是連續求gcd 可以使用reduce

from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, l: List[int]) -> bool:
        return reduce(gcd,Counter(l).values())>=2

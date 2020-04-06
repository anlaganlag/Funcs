import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern= re.compile(r'^(\s)*([+-]?\d+)')
        aim = pattern.search(s)
        if aim:
            ans = int(aim.group(2))
            if ans  >=2**31-1:
                return 2**31-1
            elif ans <= -2**31:
                return  -2**31
            else:
                return ans
        return 0
        
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern= re.compile(r'^\s*([+-]?\d+)')
        aim = pattern.search(s)#返回的是str
        if not aim:
            return 0
        return max(min( int(aim.group()),2**31-1),-2**31)

#甚至可以只用一個組


"""
min max 夾值的操作是真的牛逼

r'^(\s)*     開頭有0到多個空格,記得\s才是空格
  ([+-]?\d+) 可選有沒有+-多個數字
  ')
  
"""

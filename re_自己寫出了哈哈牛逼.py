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
        aim = pattern.search(s)#���ص���str
        if not aim:
            return 0
        return max(min( int(aim.group()),2**31-1),-2**31)

#��������ֻ��һ���M


"""
min max �Aֵ�Ĳ��������ţ��

r'^(\s)*     �_�^��0�������ո�,ӛ��\s���ǿո�
  ([+-]?\d+) ���x�Л]��+-��������
  ')
  
"""

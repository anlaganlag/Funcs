class Solution:
    def longestValidParentheses(self, s: str) -> int:
        q = [-1]#所谓-1就是哨兵
        ans = 0#记录有效括号的长度
        for i,v in enumerate(s):
            if v == "(":#如果是是(
                q.append(i)#就是candidate..
            else:
                q.pop()#遇到)就是表明凑成一个有效括号,由于有哨兵
#无需担心pop空,且早pop后为空会不少)的index相当于添加了新的哨兵..
                if q:
                    ans = max(ans,i-q[-1])
                else:
                    q.append(i)
        return ans
#可以将(理解为库存..)理解为兑现..
#库存尽管放入..兑现么次每次更新..,
#少并记录)开头位置,初始烧饼即)出现在-1的位置..
#)相当于替换初始的-1或者前面一个)




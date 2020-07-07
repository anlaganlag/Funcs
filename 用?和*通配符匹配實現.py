"""
44. 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def h(c1,c2):
	"""對應匹配或者?是全能匹配wildcard"""
            return c2=="?" or c1==c2 
        if (not s and not p) or   (not s and p=="*"):
	#都空或者一個星號匹配全部..
            return True
        if not s or not p:
            return False
	#空和有匹配不上..
        m,n = len(s),len(p)
        i=j=0#相當於對應字符串的idx..
        start_idx=-1#記錄星號的位置..
        match =0#匹配的idx..
        while i<m:#s不能越界..
            if j<n and p[j] !="*" and h(s[i],p[j]):
	#正常匹配
                i+=1
                j+=1
            elif j<n and p[j] == "*":
	#星號要處理j讓j可以下論記錄繼續匹配也要記錄好星號出現的位置..
	#要確認星號已經匹配的idx..雙狀態..
	#有點類似分身又合並..
                match = i
                start_idx =j
                j+=1#保證了遇到星號就會跳過,,一直跳到第一個無星的位置..
            elif start_idx !=-1:
                j =start_idx+1
#鎖死p的位置爲星號+1
                match+=1
                i = match
#自動+1,
            else:
                return False
        while j < n and p[j] =="*":
            j+=1
        return j==n

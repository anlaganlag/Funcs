class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_, n = '', len(s)
        if len(set(s))==1:
            return s
        A=lambda s,l,r:A(s,l-1,r+1) if l-1>=0 and r+1<n and s[l-1]==s[r+1] else s[l:r+1]    
        for i in range(n):
            t1 = A(s,i,i) if i+1<n  else ''          
            t2 = A(s,i,i+1) if i+1<n and s[i]==s[i+1] else ''  
            max_ = max(max_,t1,t2,key=len)
        return max_

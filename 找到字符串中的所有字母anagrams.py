class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m,n = len(s), len(p)
        if m < n:
            return []
        az = 26*[0]
        ans= []
        for i in range(n):
            az[ord(p[i])-97]+=1
            az[ord(s[i])-97]-=1
        if az == 26*[0]:
            ans.append(0)
        for i in range(n,m):
            az[ord(s[i])-97]-=1
            az[ord(s[i-n])-97]+=1
            if az ==26*[0]:
                ans.append(i-n+1)
        return ans
        


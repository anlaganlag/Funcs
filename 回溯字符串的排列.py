
"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
"""

def p(s):
    ans = []
    def backTrack(s,tmp):
        if not s:
            ans.append(tmp)
        d = []
        for i,v in enumerate(s):
            if v in d:
                print(s,tmp,d)
                
            else:
                backTrack(s[:i]+s[i+1:],tmp+v)
                d.append(v)
#                 print(s,tmp,d)
    backTrack(s,"")
    return ans if ans else []
p("abb")


